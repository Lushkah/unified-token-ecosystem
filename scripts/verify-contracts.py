#!/usr/bin/env python3
"""
Smart Contract Verification Script
Verifies deployed contracts on blockchain
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.blockchain.verification import verify_all_contracts
from src.config import settings


def main():
    parser = argparse.ArgumentParser(description="Verify smart contracts")
    parser.add_argument(
        "--network",
        choices=["local", "sepolia", "mainnet", "polygon"],
        default="sepolia",
        help="Network where contracts are deployed"
    )
    
    args = parser.parse_args()
    
    print("="*80)
    print(f"Smart Contract Verification - {args.network.upper()}")
    print("="*80)
    print()
    
    try:
        print(f"Verifying contracts on {args.network}...")
        print()
        
        results = verify_all_contracts(network=args.network)
        
        print("Verification Results:")
        print()
        
        for contract_name, verification_status in results.items():
            status = "✓" if verification_status else "✗"
            print(f"  {status} {contract_name}: {verification_status}")
        
        print()
        print("="*80)
        print("✓ Contract verification complete!")
        print("="*80)
        print()
        
    except Exception as e:
        print(f"\n✗ Verification failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
