#!/usr/bin/env python3
"""
Token System Initialization Script
Sets up token parameters and initial distribution
"""

import sys
from pathlib import Path
from decimal import Decimal

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.economics.token_manager import TokenManager
from src.config import settings


def main():
    print("="*80)
    print("Token System Initialization")
    print("="*80)
    print()
    
    try:
        manager = TokenManager()
        
        print("Token Configuration:")
        print(f"  Name: {settings.TOKEN_NAME}")
        print(f"  Symbol: {settings.TOKEN_SYMBOL}")
        print(f"  Decimals: {settings.TOKEN_DECIMALS}")
        print(f"  Total Supply: {settings.TOKEN_INITIAL_SUPPLY:,}")
        print()
        
        print("Initializing token system...")
        result = manager.initialize_token_system()
        print("✓ Token system initialized")
        print()
        
        print("Initial Distribution:")
        distribution = {
            "Platform Treasury": Decimal(40),
            "Agent Rewards": Decimal(30),
            "Community": Decimal(20),
            "Core Team": Decimal(10),
        }
        
        total_supply = Decimal(settings.TOKEN_INITIAL_SUPPLY)
        for allocation, percentage in distribution.items():
            amount = total_supply * (percentage / 100)
            print(f"  {allocation}: {amount:,.0f} ({percentage}%)")
        print()
        
        print("="*80)
        print("✓ Token system initialization complete!")
        print("="*80)
        print()
        print("Token details:")
        print(f"  Contract Address: {settings.TOKEN_CONTRACT_ADDRESS}")
        print(f"  Network: {settings.PLATFORM_ENV}")
        print()
        
    except Exception as e:
        print(f"\n✗ Error during token initialization: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
