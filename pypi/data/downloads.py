import sqlalchemy as sa
from pypi.data.modelbase import SqlAlchemyBase
import datetime


class Download(SqlAlchemyBase):
    __tablename__ = "downloads"

    id = sa.Column(sa.BIGINT, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DATETIME, default=datetime.datetime.now, index=True)

    package_id = sa.Column(sa.String, index=True)
    release_id = sa.Column(sa.BigInteger, index=True)

    ip_address = sa.Column(sa.String)
    user_agent = sa.Column(sa.String)
