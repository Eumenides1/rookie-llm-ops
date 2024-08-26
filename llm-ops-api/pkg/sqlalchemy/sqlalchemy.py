"""
@Time    :2024/8/26 21:25
@Author  :jaguarliu
@File    :sqlalchemy.py
@Desc    :
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    """重写 Flask_SQLAlchemy核心类，实现自动提交"""

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
