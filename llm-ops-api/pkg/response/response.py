"""
@Time    :2024/8/24 23:12
@Author  :jaguarliu
@File    :response.py
@Desc    : API统一返回结构
"""
from dataclasses import field, dataclass
from typing import Any

from flask import jsonify

from pkg.response.http_code import HttpCode


@dataclass
class Response:
    """基础 HTTP 接口响应格式"""
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    """基础的响应接口"""
    return jsonify(data), HttpCode.SUCCESS


def success_json(data: Any = None):
    """成功数据响应"""
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    """失败数据响应"""
    return json(Response(code=HttpCode.FAIL, message="", data=data))


def validate_error_json(errors: dict = None):
    """实体验证错误响应"""
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json(Response(code=HttpCode.VALIDATE_ERROR, message=msg, data=errors))


def message(code: HttpCode = None, msg: str = ""):
    """基础的消息响应，固定返回消息提示"""
    return json(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    """成功基础的消息响应，固定返回消息提示"""
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    """失败基础的消息响应，固定返回消息提示"""
    return message(code=HttpCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    """未找到的消息响应，固定返回消息提示"""
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def unauthorized_message(msg: str = ""):
    """未授权的消息响应，固定返回消息提示"""
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):
    """无权限的消息响应，固定返回消息提示"""
    return message(code=HttpCode.FORBIDDEN, msg=msg)
