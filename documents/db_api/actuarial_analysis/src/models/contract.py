"""Contract ORM model."""

from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Contract(Base):
    """
    ORM model for contracts.

    Attributes:
        contract_id: primary key
        client_id: FK to clients
        product: product name
        start_date, end_date: contract period
        sum_assured: insured sum
    """
    __tablename__ = "contracts"

    contract_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"))
    product = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    sum_assured = Column(Float)

    client = relationship("Client", back_populates="contracts")
    primes = relationship("Prime", back_populates="contract")
    claims = relationship("Claim", back_populates="contract")

    def __repr__(self) -> str:
        return f"<Contract(id={self.contract_id}, product={self.product}, client_id={self.client_id})>"