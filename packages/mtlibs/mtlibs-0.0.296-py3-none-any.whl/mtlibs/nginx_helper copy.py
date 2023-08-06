
import os,sys,time
import subprocess
from subprocess import run,Popen, PIPE
from pathlib import Path
import shutil
import logging
logger = logging.getLogger(__name__)


def renew_cert(domain, exist_ok=True) -> bool:
    """重新获取ssl证书"""
    cert_dir = f"/etc/letsencrypt/live/{domain}"
    if exist_ok and os.path.exists(cert_dir):
        logger.info(f"ssl证书`{domain}`已经存在，跳过获取")
        return cert_dir
    else:
        run(f"sudo apt install -y certbot python3-certbot-nginx", shell=True, check=True)
        # 使用nginx插件的形式获取证书，这个问题在于，需要nginx首先配置成为http的方式（即没有使用https的情况下）才行，考虑到容器经常重置的问题，这个方式不妥。
        # run(f"sudo certbot certonly --non-interactive --agree-tos --nginx -d {domain} -m a@a.com", shell=True, check=True)
        # 现在使用 certbot 独立的方式获取证书。获取证书后，直接手动配置nginx配置文件启动。
        run(f"certbot certonly --non-interactive --agree-tos --standalone -d {domain} -m a@a.com", shell=True, check=True)
        # 确实证书文件存在
        if os.path.exists(cert_dir):            
            return cert_dir

    logger.info(f"证书文件视乎不存在，请注意查找原因")
    return None


def setup_nginx(domain_name=None, www_root="/var/www/html"):
    """根据环境变量和相关参数生产nginx配置文件"""

    nginx_conf_tpl = """user  www-data;
worker_processes auto;
error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;
events {
    worker_connections  1024;
}
http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;
    sendfile        on;
    #tcp_nopush     on;
    keepalive_timeout  65;

    gzip  on;
    gzip_comp_level 5;

    # gzip.conf
    gzip_min_length 256;
    gzip_proxied any;
    gzip_vary on;    

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;


    # Default Webdock Nginx configuration


    upstream nestjs {
        server 127.0.0.1:3600 weight=100 max_fails=12 fail_timeout=60s;
    }

    upstream mtxcms {
        server 127.0.0.1:8000 weight=450 max_fails=12 fail_timeout=60s;
    }
    
    server {
        root @@www_root@@; 
        client_max_body_size 256M;
        index index.html index.htm index.php;
        server_name @@DOMAIN_NAME@@;
        # location / {
        #     # First attempt to serve request as file, then
        #     # as directory, then fall back to displaying a 404.
        #     try_files $uri $uri/ /index.php?$query_string;
        # }
        location / {
            autoindex on;
            index index.html index.htm index.php;
            try_files $uri $uri/ /index.php?$args @mtx default_backend;
        }

        


        location = /favicon.ico { access_log off; log_not_found off; }
        location = /robots.txt  { access_log off; log_not_found off; }
        access_log /var/www/logs/access.log;
        error_log  /var/www/logs/error.log error;
        # error_page 404 /index.php;

        location ~ \.php$ {
            # add_header X-Powered-By "Webdock2.io";
            fastcgi_split_path_info ^(.+\.php)(/.+)$;
            # fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_index index.php;
            include fastcgi_params;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_intercept_errors off;
            fastcgi_buffer_size 16k;
            fastcgi_buffers 4 16k;
            fastcgi_connect_timeout 600;
            fastcgi_send_timeout 600;
            fastcgi_read_timeout 600;
        }

        location ^~ /mtxadmin/ {
            add_header X-Powered-By 'PHP';
            # try_files @nextfront $uri $uri/;
            proxy_pass http://mtxcms;
            # autoindex on;
            # index index.html index.htm;
        }
        location ^~ /static/ {
            # 开发板的静态文件
            add_header X-Powered-By 'PHP';
            proxy_pass http://mtxcms;
        }
        location ^~ /api/ {
            add_header X-Powered-By 'PHP';
            proxy_pass http://mtxcms;
        }

        # Necessary for Let's Encrypt Domain Name ownership validation. Place any other deny rules after this
        location ~ /.well-known {
        allow all;
    }

    # Deny access to .htaccess or .htpasswd files
    location ~ /\.ht {
        deny all;
    }

    # Deny access to any git repository
    location ~ /\.git {
        deny all;
    }

    # Deny access to xmlrpc.php - a common brute force target against Wordpress
    location = /xmlrpc.php {
        deny all;
        access_log off;
        log_not_found off;
        return 444;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/@@DOMAIN_NAME@@/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/@@DOMAIN_NAME@@/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}
   
    server {
    if ($host = @@DOMAIN_NAME@@) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    server_name @@DOMAIN_NAME@@;
    listen 80;
    return 404; # managed by Certbot

    }
}
"""


    

    DOMAIN_NAME=domain_name or os.environ.get("DOMAIN_NAME", "localhost")

    cert_dir =  renew_cert(DOMAIN_NAME)
    if not cert_dir:
        logger.info(f"证书没有成功获取")
        return 

    nginx_conf = nginx_conf_tpl.replace("@@DOMAIN_NAME@@", DOMAIN_NAME).replace("@@www_root@@", www_root)

    with open("/etc/nginx/nginx.conf", 'w') as fd:
        fd.write(nginx_conf)

    logger.info(f"初始化相关目录")
    os.makedirs("/var/www/logs", exist_ok=True)
    os.path.exists("/etc/nginx/conf.d") and shutil.rmtree("/etc/nginx/conf.d")
    # print(f"nginx.confg配置=============================================")
    # print(nginx_conf)
    # print("========================================================")

    # 设置目前权限
    # sudo chown nginx -R ./html
    if not os.path.exists(www_root):
        Path(www_root).mkdir(mode=0o700, exist_ok=True, )
        # os.mkdir(www_root,)
    run(f"sudo chown nginx -R {www_root}", shell=True, check=True)
    logger.info(f"重启nginx服务")

    
    run("sudo service nginx restart", shell=True)

    