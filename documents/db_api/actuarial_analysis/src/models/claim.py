"""Claim (sinistre) ORM model."""

from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Claim(Base):
    """
    ORM model for claims (sinistres).
    
    Attributes:
        claim_id: primary key
        contract_id: FK to contracts
        report_date: date when claim was reported
        cost: claim cost
        cause: cause of the claim
    """
    __tablename__ = "claims"

    claim_id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey("contracts.contract_id"))
    report_date = Column(Date)
    cost = Column(Float)
    cause = Column(String(100))

    contract = relationship("Contract", back_populates="claims")

    def __repr__(self) -> str:
        return f"<Claim(id={self.claim_id}, cost={self.cost}, contract_id={self.contract_id})>"