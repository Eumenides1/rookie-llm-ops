"""
@Time    :2024/8/24 21:25
@Author  :jaguarliu
@File    :app_schema.py
@Desc    :
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求实体"""
    # 必填、长度最大为 2000
    query = StringField("query", validators=[
        DataRequired(message="你没有什么问题吗？那你调接口干嘛？"),
        Length(max=2000, message="你话怎么这么多，2000字都不够你说的")
    ])
