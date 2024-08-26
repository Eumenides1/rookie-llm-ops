"""
@Time    :2024/8/24 00:07
@Author  :jaguarliu
@File    :app_handler.py
@Desc    :
"""
import os
import uuid
from dataclasses import dataclass

from injector import inject
from openai import OpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
    """
    应用控制器
    """
    app_service: AppService

    def create_app(self):
        """调用服务创建新的 APP 记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id 为{app.id}")

    def get_app(self, id: uuid.UUID):
        """根据 ID 查询 APP 记录"""
        app = self.app_service.get_app(id)
        return success_message(f"成功获取应用，名称是:{app.name}")

    def update_app(self, id: uuid.UUID):
        """根据 id 更新记录"""
        app = self.app_service.update_app(id)
        return success_message(f"应用已完成修改，修改后数据:{app.icon}")

    def delete_app(self, id: uuid.UUID):
        """根据 ID 删除APP 记录"""
        app = self.app_service.delete_app(id)
        return success_message(f"应用已删除，删除的应用 id：{app.id}")

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
