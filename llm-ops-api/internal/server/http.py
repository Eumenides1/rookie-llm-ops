"""
@Time    :2024/8/24 00:19
@Author  :jaguarliu
@File    :http.py
@Desc    :
"""
import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.response import (Response, json, HttpCode)
from pkg.sqlalchemy import SQLAlchemy


class Http(Flask):
    """Http 服务引擎"""

    def __init__(
            self,
            *args,
            conf: Config,
            db: SQLAlchemy,
            migrate: Migrate,
            router: Router,
            **kwargs):
        super().__init__(*args, **kwargs)
        # 将本地配置导入 flask
        self.config.from_object(conf)
        # 注册绑定异常处理
        self.register_error_handler(Exception, self._register_error_handler)
        # 初始化 database
        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migration")
        # 解决前后端跨域问题
        CORS(self, resources={
            r"/*": {
                "origins": "*",
                "supports_credentials": True,
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
            }
        })
        # 注册应用路由
        router.register_routes(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {},
            ))
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
