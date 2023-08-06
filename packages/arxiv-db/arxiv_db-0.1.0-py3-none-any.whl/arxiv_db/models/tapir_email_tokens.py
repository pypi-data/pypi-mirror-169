from sqlalchemy import Column, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata


class TapirEmailTokens(Base):
    __tablename__ = 'tapir_email_tokens'

    user_id = Column(ForeignKey('tapir_users.user_id'), primary_key=True, nullable=False, server_default=text("'0'"))
    secret = Column(String(32), primary_key=True, nullable=False, index=True, server_default=text("''"))
    tapir_dest = Column(String(255), nullable=False, server_default=text("''"))
    issued_when = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    issued_to = Column(String(16), nullable=False, server_default=text("''"))
    remote_host = Column(String(255), nullable=False, server_default=text("''"))
    tracking_cookie = Column(String(255), nullable=False, server_default=text("''"))
    wants_perm_token = Column(INTEGER(1), nullable=False, server_default=text("'0'"))

    user = relationship('TapirUsers')
