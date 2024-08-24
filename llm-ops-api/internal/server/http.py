"""
@Time    :2024/8/24 00:19
@Author  :jaguarliu
@File    :http.py
@Desc    :
"""
from flask import Flask

from config import Config
from internal.router import Router


class Http(Flask):
    """Http 服务引擎"""

    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_routes(self)
        # 将本地配置导入 flask
        self.config.from_object(conf)
