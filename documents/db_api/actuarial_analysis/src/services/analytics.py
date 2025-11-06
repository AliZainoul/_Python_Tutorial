"""Analytics service for actuarial calculations."""

from datetime import date
from typing import Dict, List, Tuple, Optional
from collections import defaultdict

from sqlalchemy import func, extract, or_
from sqlalchemy.orm import Session

from src.models.client import Client
from src.models.contract import Contract
from src.models.prime import Prime
from src.models.claim import Claim
from src.utils.date_helpers import calculate_age, get_age_bucket


class AnalyticsService:
    """Service for computing actuarial indicators."""
    
    def __init__(self, session: Session):
        """
        Initialize analytics service.
        
        Args:
            session: SQLAlchemy Session instance
        """
        self.session = session
    
    def compute_average_premium_by_age_bucket(
        self, ref_date: date = date(2022, 12, 31)
    ) -> Dict[str, Dict[str, float]]:
        """
        Compute average premium amount by product and age bucket.

        Args:
            ref_date: reference date for age calculation

        Returns:
            dict mapping bucket -> {product -> average_amount}
        """
        query = self.session.query(
            Prime.amount,
            Contract.product,
            Client.birth_date
        ).join(
            Contract, Prime.contract_id == Contract.contract_id
        ).join(
            Client, Contract.client_id == Client.client_id
        )

        rows = query.all()
        
        # Group data by bucket and product
        buckets: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        
        for amount, product, birth_date in rows:
            age = calculate_age(birth_date, ref_date)
            bucket = get_age_bucket(age)
            buckets[bucket].append((product, amount))
        
        # Compute averages
        result: Dict[str, Dict[str, float]] = {}
        
        for bucket, entries in buckets.items():
            product_amounts: Dict[str, List[float]] = defaultdict(list)
            
            for product, amount in entries:
                product_amounts[product].append(amount)
            
            result[bucket] = {
                product: sum(amounts) / len(amounts) if amounts else 0.0
                for product, amounts in product_amounts.items()
            }
        
        return result
    
    def compute_frequency_by_product_year(
        self, start_year: int = 2016, end_year: int = 2022
    ) -> List[Tuple[str, int, int, int]]:
        """
        Compute claim frequency per product and year.

        Returns:
            list of tuples (product, year, n_claims, n_active_contracts)
        """
        products = [
            row[0] for row in self.session.query(Contract.product).distinct().all()
        ]
        
        results = []
        
        for product in products:
            for year in range(start_year, end_year + 1):
                n_claims = self._count_claims_for_product_year(product, year)
                n_active = self._count_active_contracts(product, year)
                results.append((product, year, n_claims, n_active))
        
        return results
    
    def _count_claims_for_product_year(self, product: str, year: int) -> int:
        """Count claims for a product in a specific year."""
        count = self.session.query(
            func.count(Claim.claim_id)
        ).join(
            Contract
        ).filter(
            Contract.product == product,
            extract("year", Claim.report_date) == year
        ).scalar()
        
        return int(count or 0)
    
    def _count_active_contracts(self, product: str, year: int) -> int:
        """Count active contracts for a product in a specific year."""
        year_start = date(year, 1, 1)
        year_end = date(year, 12, 31)
        
        count = self.session.query(
            func.count(Contract.contract_id)
        ).filter(
            Contract.product == product,
            Contract.start_date <= year_end,
            or_(Contract.end_date == None, Contract.end_date >= year_start)
        ).scalar()
        
        return int(count or 0)
    
    def compute_avg_cost_by_segment(self) -> List[Tuple[str, float, int]]:
        """
        Compute average claim cost by client segment.

        Returns:
            list of tuples (segment, avg_cost, n_claims)
        """
        query = self.session.query(
            Client.segment,
            func.avg(Claim.cost).label("avg_cost"),
            func.count(Claim.claim_id).label("n_claims"),
        ).join(
            Contract, Client.client_id == Contract.client_id
        ).join(
            Claim, Contract.contract_id == Claim.contract_id
        ).group_by(
            Client.segment
        )

        return [
            (row.segment, float(row.avg_cost), int(row.n_claims))
            for row in query.all()
        ]
    
    def compute_claim_to_premium_ratio(
        self
    ) -> List[Tuple[str, float, float, Optional[float]]]:
        """
        Compute total claims, total premiums and ratio per product.

        Returns:
            list of tuples (product, total_claims, total_primes, ratio_or_none)
        """
        query = self.session.query(
            Contract.product,
            func.sum(Claim.cost).label("total_claims"),
            func.sum(Prime.amount).label("total_primes"),
        ).join(
            Claim, Contract.contract_id == Claim.contract_id
        ).join(
            Prime, Contract.contract_id == Prime.contract_id
        ).group_by(
            Contract.product
        )

        results = []
        
        for row in query.all():
            total_claims = float(row.total_claims) if row.total_claims else 0.0
            total_primes = float(row.total_primes) if row.total_primes else 0.0
            ratio = (total_claims / total_primes) if total_primes > 0 else None
            
            results.append((row.product, total_claims, total_primes, ratio))
        
        return results