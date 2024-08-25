"""
@Time    :2024/8/25 12:53
@Author  :jaguarliu
@File    :test_app_handler.py
@Desc    :
"""
from pkg.response import HttpCode


class TestAppHandler:
    """app_handler单元测试类"""

    def test_completion(self, client):
        resp = client.post("/app/completion", json={"query": "你好呀"})
        assert resp.status_code == 200
        assert resp.json.get("code") == HttpCode.SUCCESS
        print("响应内容：", resp.json)
