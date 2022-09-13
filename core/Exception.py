#  异常处理
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError


async def http_error_handler(request, httpexception):
    """
    http异常处理
    :param request:
    :param httpexception:
    :return:
    """
    return JSONResponse({
        "code": httpexception.status_code,
        "message": httpexception.detail,
        "data": httpexception.detail,
    }, status_code=httpexception.status_code)


class UnicornException(Exception):

    def __init__(self, code, errmsg, data=None):
        """
        Unicorn服务异常类
        :param code:
        :param errmsg:
        :param data:
        """
        if data is None:
            data = {}
        self.code = code
        self.errmsg = errmsg
        self.data = data


async def unicorn_exception_handler(request, unicornexception):
    """
    unicorn 异常处理
    :param request:
    :param unicornexception:
    :return:
    """
    return JSONResponse({
        'code': unicornexception.code,
        'message': unicornexception.errmsg,
        'data': unicornexception.data,
    })


async def http422_error_handler(request, union):
    """
    参数校验错误处理
    :param request:
    :param union:
    :return:
    """
    return JSONResponse({
        'code': status.HTTP_422_UNPROCESSABLE_ENTITY,
        'message': f'参数校验错误{union.errors()}',
        'data': union.errors(),
    },
        status_code=422,
    )

