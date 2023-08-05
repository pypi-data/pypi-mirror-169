#!/usr/bin/env python3

##
## 运行gitpod环境下的主要任务，如docker镜像构建
##
import os
import sys
import subprocess
import shlex
from dotenv import load_dotenv, find_dotenv
import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

load_dotenv(".env")



DOCKER_HUB_USER=os.environ.get("DOCKER_HUB_USER")
IS_GITPOD = os.environ.get("USER") == "gitpod"


def login_dockerhub():
    logger.info(f"登录dockerhub")

def main():
    run( shlex.split(f"pip3 install -U mtlibs"), check=True)
    run(shlex.split(f"docker pull {DOCKER_HUB_USER}/dev"), check=True)



if __name__ == "__main__":
    main()
