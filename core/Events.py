"""
fastapi事件监听
"""

from typing import Callable
from fastapi import FastAPI



def startup(app):
    """
    Fastapi启动完成事件
    :param app:Fastapi
    :return: start_app
    """
    async def app_start():
        # app启动完成后触发
        print('启动完毕')
        pass
    return app_start

def stopping(app):
    """
    Fastapi启动完成事件
    :param app:Fastapi
    :return: start_app
    """
    async def stop_app():
        # app停止时触发
        print('停止')
        pass
    return stop_app
