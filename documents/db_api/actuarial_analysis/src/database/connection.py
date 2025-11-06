"""Database connection and session management."""

from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config.settings import DatabaseConfig


class DatabaseManager:
    """Manages database engine and session creation."""
    
    def __init__(self, config: DatabaseConfig):
        """
        Initialize database manager.
        
        Args:
            config: Database configuration object
        """
        self.config = config
        self.engine = create_engine(
            config.url,
            echo=config.echo,
            future=config.future
        )
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            class_=Session,
            expire_on_commit=False
        )
    
    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """
        Provide a transactional scope around a series of operations.
        
        Yields:
            SQLAlchemy Session instance
        """
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    
    def get_engine(self):
        """Return the database engine."""
        return self.engine