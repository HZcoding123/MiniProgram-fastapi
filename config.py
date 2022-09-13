import os.path
from pydantic import BaseSettings
from typing import List


class Config(BaseSettings):
    # 调试模式
    APP_DEBUG = True
    # 项目信息
    VERSION = "0.0.1"
    PROJECT_NAME = "xianshangke"
    DESCRIPTION = 'xianshangke后台'
    # 静态资源
    STATIC_DIR = os.path.join(os.getcwd(), 'static')
    # 跨域请求
    CORS_ORIGINS = ['*']
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ['*']
    CORS_ALLOW_HEADERS = ['*']


settings = Config()
