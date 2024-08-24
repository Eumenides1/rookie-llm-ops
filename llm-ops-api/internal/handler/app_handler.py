"""
@Time    :2024/8/24 00:07
@Author  :jaguarliu
@File    :app_handler.py
@Desc    :
"""
import os

from flask import request
from openai import OpenAI


class AppHandler:
    """
    应用控制器
    """

    def completion(self):
        """聊天接口"""
        # 1. 获取接口中的输入
        query = request.json.get('query')
        # 2. 构建 OpenAi 客户端，并发起请求
        client = OpenAI(
            api_key=os.environ['MY_API_KEY'],
            base_url=os.environ['OPENAI_API_BASE']
        )
        # 3. 得到请求响应，然后将 OpenAI 的响应传递给前端
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一个有趣的聊天助手，请根据用户的输入回复对应消息"},
                {"role": "user", "content": query}
            ]
        )
        content = completion.choices[0].message.content
        return content

    def ping(self):
        return {"ping": "pong"}