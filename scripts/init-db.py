#!/usr/bin/env python3
"""
Database Initialization Script
Initializes all database schemas and tables
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.database import init_db, create_tables
from src.config import settings


async def main():
    print("="*80)
    print("Database Initialization")
    print("="*80)
    print()
    
    try:
        print(f"Database URL: {settings.DATABASE_URL}")
        print("Initializing database...")
        
        await init_db()
        print("✓ Database connection established")
        
        print("\nCreating tables...")
        await create_tables()
        print("✓ All tables created successfully")
        
        print("\n" + "="*80)
        print("✓ Database initialization complete!")
        print("="*80)
        print()
        
    except Exception as e:
        print(f"\n✗ Error during initialization: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
