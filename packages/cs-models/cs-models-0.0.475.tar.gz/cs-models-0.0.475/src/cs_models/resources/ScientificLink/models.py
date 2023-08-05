from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean,
    Text,
)
from datetime import datetime

from ...database import Base


class ScientificLinkModel(Base):
    __tablename__ = 'scientific_links'

    id = Column(Integer, primary_key=True)
    doi = Column(String(191), nullable=False)
    pubmed_id = Column(
        Integer,
        ForeignKey('pubmed.id'),
        nullable=True,
    )
    date = Column(DateTime, nullable=True)
    title = Column(String(255), nullable=True)
    type = Column(String(50), nullable=True)
    abstract = Column(Text, nullable=True)
    journal_title = Column(String(255), nullable=True)
    inbound_ref_count = Column(Integer, nullable=True)
    outbound_ref_count = Column(Integer, nullable=True)
    orig_file_url = Column(String(255), nullable=True)
    best_oa_location = Column(String(255), nullable=True)
    method = Column(String(128), nullable=True)
    verification = Column(String(128), nullable=True)
    is_deleted = Column(Boolean, nullable=True)
    updated_at = Column(
        DateTime,
        nullable=False,
        # https://stackoverflow.com/questions/58776476/why-doesnt-freezegun-work-with-sqlalchemy-default-values
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
    )
