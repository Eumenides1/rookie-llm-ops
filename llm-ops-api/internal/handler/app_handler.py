"""
@Time    :2024/8/24 00:07
@Author  :jaguarliu
@File    :app_handler.py
@Desc    :
"""
import os

from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json


class AppHandler:
    """
    应用控制器
    """

    def completion(self):
        """聊天接口"""
        # 1. 获取接口中的输入
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2. 构建 OpenAi 客户端，并发起请求
        client = OpenAI(
            base_url=os.getenv('OPENAI_API_BASE')
        )
        # 3. 得到请求响应，然后将 OpenAI 的响应传递给前端
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一个有趣的聊天助手，请根据用户的输入回复对应消息"},
                {"role": "user", "content": req.query.data}
            ]
        )
        content = completion.choices[0].message.content
        return success_json({"content": content})

    def ping(self):
        raise FailException("服务请求失败")
