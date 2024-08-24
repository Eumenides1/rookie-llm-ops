"""
@Time    :2024/8/24 23:09
@Author  :jaguarliu
@File    :http_code.py
@Desc    : 统一返回结果类型枚举
"""
from enum import Enum


class HttpCode(str, Enum):
    """Http基础业务状态码"""
    SUCCESS = "success"  # 请求成功
    FAIL = "fail"  # 请求失败
    NOT_FOUND = "not_found"  # 资源不存在
    UNAUTHORIZED = "unauthorized"  # 未授权
    FORBIDDEN = "forbidden"  # 无权限
    VALIDATE_ERROR = "validate_error"  # 数据验证错误
