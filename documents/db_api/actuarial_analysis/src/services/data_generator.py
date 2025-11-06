"""Data generation service for populating the database."""

import random
from datetime import date
from typing import List

from sqlalchemy.orm import Session

from config.settings import (
    DataGenerationConfig,
    PRODUCTS,
    PRODUCT_WEIGHTS,
    CLAIM_BASE_PROBABILITIES,
    CLAIM_CAUSES,
    SEGMENT_INDIVIDUAL,
    SEGMENT_CORPORATE,
)
from src.models.client import Client
from src.models.contract import Contract
from src.models.prime import Prime
from src.models.claim import Claim
from src.utils.date_helpers import generate_random_birth_date, create_safe_date


class DataGenerator:
    """Service for generating realistic demo data."""
    
    def __init__(self, config: DataGenerationConfig):
        """
        Initialize data generator.
        
        Args:
            config: Data generation configuration
        """
        self.config = config
        random.seed(config.random_seed)
    
    def generate_all(self, session: Session) -> None:
        """
        Generate all demo data.
        
        Args:
            session: SQLAlchemy Session instance
        """
        clients = self._generate_clients()
        session.add_all(clients)
        session.flush()
        
        contracts = self._generate_contracts(session)
        session.add_all(contracts)
        session.flush()
        
        primes = self._generate_primes(session)
        session.add_all(primes)
        session.flush()
        
        claims = self._generate_claims(session)
        session.add_all(claims)
        session.flush()
    
    def _generate_clients(self) -> List[Client]:
        """Generate client records."""
        clients = []
        
        for i in range(1, self.config.n_clients + 1):
            is_corporate = random.random() < self.config.corporate_probability
            
            if is_corporate:
                name = f"Company_{i}"
                birth_date = None
                segment = SEGMENT_CORPORATE
            else:
                name = f"Client_{i}"
                birth_date = generate_random_birth_date(
                    self.config.min_age,
                    self.config.max_age
                )
                segment = SEGMENT_INDIVIDUAL
            
            clients.append(
                Client(name=name, birth_date=birth_date, segment=segment)
            )
        
        return clients
    
    def _generate_contracts(self, session: Session) -> List[Contract]:
        """Generate contract records."""
        contracts = []
        contract_id = 1
        
        for client in session.query(Client).all():
            n_contracts = random.randint(
                self.config.min_contracts_per_client,
                self.config.max_contracts_per_client
            )
            
            for _ in range(n_contracts):
                product = random.choices(PRODUCTS, weights=PRODUCT_WEIGHTS)[0]
                start_date = date(
                    2015 + random.randint(0, 7),
                    random.randint(1, 12),
                    random.randint(1, 28)
                )
                sum_assured = round(random.uniform(5000, 500000), 2)
                
                contracts.append(
                    Contract(
                        contract_id=contract_id,
                        client=client,
                        product=product,
                        start_date=start_date,
                        end_date=None,
                        sum_assured=sum_assured,
                    )
                )
                contract_id += 1
        
        return contracts
    
    def _generate_primes(self, session: Session) -> List[Prime]:
        """Generate prime (premium payment) records."""
        primes = []
        prime_id = 1
        
        for contract in session.query(Contract).all():
            n_primes = random.randint(
                self.config.min_primes_per_contract,
                self.config.max_primes_per_contract
            )
            
            for k in range(n_primes):
                year = contract.start_date.year + k
                paid_date = create_safe_date(
                    year,
                    contract.start_date.month,
                    contract.start_date.day
                )
                
                multiplier = 10.0 if contract.client.segment == SEGMENT_CORPORATE else 1.0
                amount = round(random.uniform(200, 5000) * multiplier, 2)
                
                primes.append(
                    Prime(
                        prime_id=prime_id,
                        contract=contract,
                        amount=amount,
                        paid_date=paid_date
                    )
                )
                prime_id += 1
        
        return primes
    
    def _generate_claims(self, session: Session) -> List[Claim]:
        """Generate claim records."""
        claims = []
        claim_id = 1
        
        for contract in session.query(Contract).all():
            prob = CLAIM_BASE_PROBABILITIES.get(contract.product, 0.02)
            
            for year in range(self.config.claim_start_year, self.config.claim_end_year + 1):
                if random.random() < prob:
                    report_date = date(
                        year,
                        random.randint(1, 12),
                        random.randint(1, 28)
                    )
                    cost = round(
                        random.expovariate(1 / 5000) + (contract.sum_assured * 0.01),
                        2
                    )
                    cause = random.choice(CLAIM_CAUSES)
                    
                    claims.append(
                        Claim(
                            claim_id=claim_id,
                            contract=contract,
                            report_date=report_date,
                            cost=cost,
                            cause=cause
                        )
                    )
                    claim_id += 1
        
        return claims