from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER

from .. import Base

metadata = Base.metadata


class AwsFiles(Base):
    __tablename__ = 'arXiv_aws_files'


    type = Column(String(10), nullable=False, index=True, server_default=text("''"))
    filename = Column(String(100), primary_key=True, server_default=text("''"))
    md5sum = Column(String(50))
    content_md5sum = Column(String(50))
    size = Column(INTEGER(11))
    timestamp = Column(DateTime)
    yymm = Column(String(4))
    seq_num = Column(INTEGER(11))
    first_item = Column(String(20))
    last_item = Column(String(20))
    num_items = Column(INTEGER(11))
