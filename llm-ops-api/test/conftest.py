"""
@Time    :2024/8/25 13:01
@Author  :jaguarliu
@File    :conftest.py
@Desc    :
"""
import pytest

from app.http.app import app


@pytest.fixture
def client():
    """获取 Flask 应用的测试客户端"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
