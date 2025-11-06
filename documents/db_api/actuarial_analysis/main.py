#!/usr/bin/env python3
"""
Main entry point for the actuarial analysis application.

This script demonstrates a clean architecture with:
- Separation of concerns (models, services, database, config)
- DRY principles (reusable components)
- Clear structure and maintainability
"""

from config.settings import (
    DatabaseConfig,
    DataGenerationConfig,
    AnalysisConfig,
)
from src.database.connection import DatabaseManager
from src.database.setup import DatabaseSetup
from src.services.data_generator import DataGenerator
from src.services.analytics import AnalyticsService


def print_average_premiums(analytics: AnalyticsService) -> None:
    """Print average premium analysis by age bucket."""
    print("=" * 80)
    print("1. AVERAGE PREMIUM BY AGE BUCKET AND PRODUCT")
    print("=" * 80)
    
    config = AnalysisConfig()
    results = analytics.compute_average_premium_by_age_bucket()
    
    for bucket, product_map in sorted(results.items()):
        print(f"\nAge Bucket: {bucket}")
        for product, avg in sorted(product_map.items()):
            print(f"  {product:15s}: {avg:>10.2f} €")


def print_claim_frequency(analytics: AnalyticsService) -> None:
    """Print claim frequency analysis by product and year."""
    print("\n" + "=" * 80)
    print("2. CLAIM FREQUENCY BY PRODUCT AND YEAR")
    print("=" * 80)
    
    config = AnalysisConfig()
    results = analytics.compute_frequency_by_product_year(
        start_year=config.frequency_start_year,
        end_year=config.frequency_end_year
    )
    
    print(f"\n{'Product':<15} {'Year':<8} {'Claims':<10} {'Active':<10} {'Frequency %':>12}")
    print("-" * 80)
    
    for product, year, n_claims, n_active in results:
        freq_pct = (n_claims / n_active * 100) if n_active > 0 else 0.0
        print(f"{product:<15} {year:<8} {n_claims:<10} {n_active:<10} {freq_pct:>11.2f}%")


def print_avg_cost_by_segment(analytics: AnalyticsService) -> None:
    """Print average claim cost by segment."""
    print("\n" + "=" * 80)
    print("3. AVERAGE CLAIM COST BY SEGMENT")
    print("=" * 80)
    
    results = analytics.compute_avg_cost_by_segment()
    
    print(f"\n{'Segment':<15} {'Avg Cost':>15} {'N Claims':>12}")
    print("-" * 45)
    
    for segment, avg_cost, n_claims in results:
        print(f"{segment:<15} {avg_cost:>14.2f} € {n_claims:>12}")


def print_claim_to_premium_ratio(analytics: AnalyticsService) -> None:
    """Print claim-to-premium ratio by product."""
    print("\n" + "=" * 80)
    print("4. CLAIM-TO-PREMIUM RATIO BY PRODUCT")
    print("=" * 80)
    
    results = analytics.compute_claim_to_premium_ratio()
    
    print(f"\n{'Product':<15} {'Total Claims':>18} {'Total Premiums':>18} {'Ratio':>10}")
    print("-" * 80)
    
    for product, total_claims, total_primes, ratio in results:
        ratio_str = f"{ratio:.4f}" if ratio is not None else "N/A"
        print(f"{product:<15} {total_claims:>17.2f} € {total_primes:>17.2f} € {ratio_str:>10}")


def main() -> None:
    """
    Main execution routine.
    
    Steps:
    1. Setup database
    2. Generate demo data
    3. Compute and display actuarial indicators
    """
    # Initialize configuration
    db_config = DatabaseConfig()
    data_config = DataGenerationConfig()
    
    # Setup database
    db_manager = DatabaseManager(db_config)
    db_setup = DatabaseSetup(db_manager)
    
    print("Setting up database...")
    db_setup.create_tables(drop_first=True)
    
    # Generate data
    print("Generating demo data...")
    data_generator = DataGenerator(data_config)
    
    with db_manager.get_session() as session:
        data_generator.generate_all(session)
    
    # Run analytics
    print("Computing actuarial indicators...\n")
    
    with db_manager.get_session() as session:
        analytics = AnalyticsService(session)
        
        print_average_premiums(analytics)
        print_claim_frequency(analytics)
        print_avg_cost_by_segment(analytics)
        print_claim_to_premium_ratio(analytics)
    
    print("\n" + "=" * 80)
    print("Analysis complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()