"""Configuration settings for the actuarial analysis application."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class DatabaseConfig:
    """Database configuration."""
    url: str = "sqlite:///actuarial_analysis.db"
    echo: bool = False
    future: bool = True


@dataclass
class DataGenerationConfig:
    """Configuration for data generation."""
    random_seed: int = 42
    n_clients: int = 200
    corporate_probability: float = 0.1
    min_age: int = 20
    max_age: int = 80
    min_contracts_per_client: int = 1
    max_contracts_per_client: int = 3
    min_primes_per_contract: int = 1
    max_primes_per_contract: int = 6
    claim_start_year: int = 2016
    claim_end_year: int = 2022


@dataclass
class AnalysisConfig:
    """Configuration for analysis functions."""
    default_ref_date: str = "2022-12-31"
    frequency_start_year: int = 2016
    frequency_end_year: int = 2022


# Product configuration
PRODUCTS = ["TermLife", "WholeLife", "Auto", "Fire", "Health"]
PRODUCT_WEIGHTS = [0.25, 0.15, 0.25, 0.2, 0.15]

# Claim base probabilities by product
CLAIM_BASE_PROBABILITIES: Dict[str, float] = {
    "TermLife": 0.02,
    "WholeLife": 0.015,
    "Auto": 0.08,
    "Fire": 0.03,
    "Health": 0.05,
}

# Claim causes
CLAIM_CAUSES = ["Accident", "Theft", "Natural", "Health"]

# Age buckets
AGE_BUCKETS = {
    "0-25": (0, 25),
    "26-45": (26, 45),
    "46-65": (46, 65),
    "66+": (66, 200),
}

# Segments
SEGMENT_INDIVIDUAL = "individual"
SEGMENT_CORPORATE = "corporate"