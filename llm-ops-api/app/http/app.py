"""
@Time    :2024/8/24 00:21
@Author  :jaguarliu
@File    :app.py
@Desc    : http服务主入口
"""
from injector import Injector

from internal.router import Router
from internal.server import Http

injector = Injector()

app = Http(__name__, router=injector.get(Router))

if __name__ == '__main__':
    app.run()
