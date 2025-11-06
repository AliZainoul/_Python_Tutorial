"""Database setup utilities."""

from src.models.base import Base
from .connection import DatabaseManager


class DatabaseSetup:
    """Handle database schema creation and initialization."""
    
    def __init__(self, db_manager: DatabaseManager):
        """
        Initialize setup handler.
        
        Args:
            db_manager: DatabaseManager instance
        """
        self.db_manager = db_manager
    
    def create_tables(self, drop_first: bool = True) -> None:
        """
        Create database tables.
        
        Args:
            drop_first: if True, drop all tables before creating
        """
        engine = self.db_manager.get_engine()
        
        if drop_first:
            Base.metadata.drop_all(engine)
        
        Base.metadata.create_all(engine)
    
    def drop_tables(self) -> None:
        """Drop all database tables."""
        engine = self.db_manager.get_engine()
        Base.metadata.drop_all(engine)