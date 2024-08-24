"""
@Time    :2024/8/24 22:53
@Author  :jaguarliu
@File    :config.py
@Desc    :
"""


class Config:
    def __init__(self):
        # 关闭 wtf 的 CSRF
        self.WTF_CSRF_ENABLED = False
