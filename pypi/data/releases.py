import sqlalchemy as sa
import datetime
from sqlalchemy import orm
from pypi.data.modelbase import SqlAlchemyBase


class Release(SqlAlchemyBase):
    __tablename__ = "releases"

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)

    major_ver = sa.Column(sa.BigInteger, index=True)
    minor_ver = sa.Column(sa.BigInteger, index=True)
    build_ver = sa.Column(sa.BigInteger, index=True)

    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    comment = sa.Column(sa.String)
    url = sa.Column(sa.String)
    size = sa.Column(sa.BigInteger)

    package_id = sa.Column(sa.String, sa.ForeignKey("packages.id"))
    package = orm.relation("Package", back_populates="releases")

    @property
    def version_text(self):
        return f"{self.major_ver}.{self.minor_ver}.{self.build_ver}"
