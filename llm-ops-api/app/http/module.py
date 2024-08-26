"""
@Time    :2024/8/25 21:45
@Author  :jaguarliu
@File    :module.py
@Desc    :
"""
from injector import Module, Binder

from internal.extension.database_extension import db
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
