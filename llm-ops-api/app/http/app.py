"""
@Time    :2024/8/24 00:21
@Author  :jaguarliu
@File    :app.py
@Desc    : http服务主入口
"""
import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server import Http
from pkg.sqlalchemy import SQLAlchemy
from .module import ExtensionModule

# 将.env加载到环境变量里
dotenv.load_dotenv()

conf = Config()

injector = Injector([ExtensionModule])

app = Http(__name__, conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == '__main__':
    app.run()
