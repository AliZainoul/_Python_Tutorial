"""Client ORM model."""

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from .base import Base


class Client(Base):
    """
    ORM model for clients.

    Attributes:
        client_id: primary key
        name: client/company name
        birth_date: date of birth for individuals (None for corporates)
        segment: 'individual' or 'corporate'
    """
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_date = Column(Date)
    segment = Column(String(50))

    contracts = relationship("Contract", back_populates="client")

    def __repr__(self) -> str:
        return f"<Client(id={self.client_id}, name={self.name}, segment={self.segment})>"