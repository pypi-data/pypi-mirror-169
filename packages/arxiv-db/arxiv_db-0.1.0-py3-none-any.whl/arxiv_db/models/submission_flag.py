from sqlalchemy import Column, ForeignKey, Index, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata


class SubmissionFlag(Base):
    __tablename__ = 'arXiv_submission_flag'
    __table_args__ = (
        Index('uniq_one_flag_per_mod', 'submission_id', 'user_id', unique=True),
    )

    flag_id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('tapir_users.user_id', ondelete='CASCADE'), nullable=False, index=True, server_default=text("'0'"))
    submission_id = Column(ForeignKey('arXiv_submissions.submission_id', ondelete='CASCADE'), nullable=False)
    flag = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    updated = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    submission = relationship('Submissions')
    user = relationship('TapirUsers')
