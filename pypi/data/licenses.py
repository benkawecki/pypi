import datetime
import sqlalchemy as sa
from pypi.data.modelbase import SqlAlchemyBase


class License(SqlAlchemyBase):
    __tablename__ = "licenses"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    create_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    description = sa.Column(sa.String)
