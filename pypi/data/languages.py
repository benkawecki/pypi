import sqlalchemy as sa
import datetime
from pypi.data.modelbase import SqlAlchemyBase


class ProgrammingLanguage(SqlAlchemyBase):
    __tablename__ = "languages"

    id = sa.Column(sa.String, primary_key=True)
    create_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    description = sa.Column(sa.String)
