"""Prime (premium) ORM model."""

from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Prime(Base):
    """
    ORM model for premiums (payments).
    
    Attributes:
        prime_id: primary key
        contract_id: FK to contracts
        amount: premium amount
        paid_date: date of payment
    """
    __tablename__ = "primes"

    prime_id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey("contracts.contract_id"))
    amount = Column(Float)
    paid_date = Column(Date)

    contract = relationship("Contract", back_populates="primes")

    def __repr__(self) -> str:
        return f"<Prime(id={self.prime_id}, amount={self.amount}, contract_id={self.contract_id})>"