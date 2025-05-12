import logging

from langconnect.database.connection import get_vectorstore
from langconnect.auth import AuthenticatedUser
from datetime import UTC, datetime

logger = logging.getLogger(__name__)


async def initialize_database(user: AuthenticatedUser):
    """Initialize the database by creating necessary extensions and tables."""
    logger.info("Starting database initialization...")

    # Pass user identity to the collection metadata when creating the default collection
    metadata = {}
    metadata["owner_id"] = user.identity
    # Write current time in ISO-8601 formatted style to created_at
    metadata["created_at"] = datetime.now(UTC).isoformat()

    get_vectorstore(collection_metadata=metadata)
    logger.info("Database initialization complete.")
