from sqlalchemy import BigInteger, Column

from boil.model import BaseModel


class Chat(BaseModel):
    chat_id = Column(BigInteger, unique=True, primary_key=True)
