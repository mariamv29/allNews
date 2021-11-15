from sqlalchemy.sql.functions import user
from sqlalchemy.sql.schema import ForeignKey
from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))