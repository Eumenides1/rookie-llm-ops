"""
@Time    :2024/8/25 21:59
@Author  :jaguarliu
@File    :app.py
@Desc    :
"""
import uuid
from datetime import datetime

from sqlalchemy import Column, UUID, String, Text, DateTime, PrimaryKeyConstraint, Index

from internal.extension.database_extension import db


class App(db.Model):
    """ai应用基础模型类"""
    __tablename__ = 'app'
    __table_args__ = (
        PrimaryKeyConstraint('id', name="pk_app_id"),
        Index("idx_app_account_id", "account_id"),
    )

    id = Column(UUID, default=uuid.uuid4, nullable=False)
    account_id = Column(UUID, nullable=False)
    name = Column(String(255), default="", nullable=False)
    icon = Column(String(255), default="", nullable=False)
    description = Column(Text, default="", nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
