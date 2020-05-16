from loguru import logger
from sqla_wrapper import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from boil import conf
from boil.model.magic.utils import db_session_scope

db = SQLAlchemy(conf.db_uri, scopefunc=db_session_scope)


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def get_by_id(cls, model_id):
        try:
            return db.query(cls).get(model_id)
        except SQLAlchemyError:
            logger.exception()
            raise



