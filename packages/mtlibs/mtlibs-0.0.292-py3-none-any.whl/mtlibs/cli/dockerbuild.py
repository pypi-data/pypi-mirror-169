#!/usr/bin/env python3

##
## 运行gitpod环境下的主要任务，如docker镜像构建
##
import os
import sys
import subprocess
from subprocess import run ,Popen
import shlex
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import argparse  
import time
import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

load_dotenv(".env")

DOCKER_HUB_USER=os.environ.get("DOCKER_HUB_USER")
DOCKER_HUB_PASSWORD=os.environ.get("DOCKER_HUB_PASSWORD")
DOCKER_HUB_REGISTER=os.environ.get("DOCKER_HUB_REGISTER","")
IS_GITPOD = os.environ.get("USER") == "gitpod"

def login_dockerhub():
    logger.info(f"登录dockerhub, 用户名: {DOCKER_HUB_USER}")
    cmd = f"echo {DOCKER_HUB_PASSWORD} | docker login {DOCKER_HUB_REGISTER} -u {DOCKER_HUB_USER} --password-stdin"
    logger.info(f"执行命令：{cmd}")
    run(cmd, check=True, shell=True)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("urls", default=None, nargs="*") 
    args = parser.parse_args()
    logger.info(f"urls: {args.urls}")

    urls = args.urls
    if not urls:
        # logger.info(f"没有输入urls参数，转为从环境变量中获取")
        # 从输入参数，或者环境变量中获取gitup网址。
        urls_from_env = os.environ.get("DOCKERBUILD_URL")
        if urls_from_env:
            urls = urls_from_env.split("|")

    
    if not urls:
        logger.info(f"need urls")
        time.sleep(3)
        exit()
        
    #克隆到临时目录


    login_dockerhub()
    run( shlex.split(f"pip3 install -U mtlibs"), check=True)
    # run(shlex.split(f"docker pull {DOCKER_HUB_USER}/dev"), check=True)

    if Path("./bin/docker_build").exists():
        logger.info(f"docker build 使用脚本 ./bin/docker_build")
        run(f"bin/docker_build", check=True)

    elif Path("./compose.yml"):
        logger.info(f"docker build 使用脚本: docker-compose build prebuild")
        run(shlex.split(f"docker-compose build prebuild"), check=True)
        run(shlex.split(f"docker-compose push prebuild"), check=True)
    else:
        logger.error(f"找不到 docker build 的相关脚本")


if __name__ == "__main__":
    main()
