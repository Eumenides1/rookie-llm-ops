"""
@Time    :2024/8/24 00:19
@Author  :jaguarliu
@File    :http.py
@Desc    :
"""
from flask import Flask

from internal.router import Router


class Http(Flask):
    """Http 服务引擎"""

    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_routes(self)
