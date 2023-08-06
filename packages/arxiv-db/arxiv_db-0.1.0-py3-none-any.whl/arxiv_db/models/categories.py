from sqlalchemy import Column, Enum, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import relationship

from .. import Base

metadata = Base.metadata


class Categories(Base):
    __tablename__ = 'arXiv_categories'


    archive = Column(ForeignKey('arXiv_archives.archive_id'), primary_key=True, nullable=False, server_default=text("''"))
    subject_class = Column(String(16), primary_key=True, nullable=False, server_default=text("''"))
    definitive = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    active = Column(INTEGER(1), nullable=False, server_default=text("'0'"))
    category_name = Column(String(255))
    endorse_all = Column(Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'"))
    endorse_email = Column(Enum('y', 'n', 'd'), nullable=False, server_default=text("'d'"))
    papers_to_endorse = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    endorsement_domain = Column(ForeignKey('arXiv_endorsement_domains.endorsement_domain'), index=True)

    arXiv_archives = relationship('Archives')
    arXiv_endorsement_domains = relationship('EndorsementDomains')
