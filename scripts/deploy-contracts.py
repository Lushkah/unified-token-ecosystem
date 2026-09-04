#!/usr/bin/env python3
"""
Smart Contract Deployment Script
Deploys all smart contracts to the specified network
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.blockchain.deployment import deploy_all_contracts
from src.config import settings


def main():
    parser = argparse.ArgumentParser(description="Deploy smart contracts")
    parser.add_argument(
        "--network",
        choices=["local", "sepolia", "mainnet", "polygon"],
        default="sepolia",
        help="Target network for deployment"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify contracts on blockchain explorer"
    )
    
    args = parser.parse_args()
    
    print("="*80)
    print(f"Smart Contract Deployment - {args.network.upper()}")
    print("="*80)
    print()
    
    try:
        print(f"Target Network: {args.network}")
        print(f"Environment: {settings.PLATFORM_ENV}")
        print()
        
        print("Deploying contracts...")
        deployment_result = deploy_all_contracts(
            network=args.network,
            verify=args.verify
        )
        
        print("\n✓ Contract Deployment Results:")
        print(f"  Token Contract: {deployment_result.get('token_contract')}")
        print(f"  Rewards Contract: {deployment_result.get('rewards_contract')}")
        print(f"  Governance Contract: {deployment_result.get('governance_contract')}")
        print()
        
        print("\n" + "="*80)
        print("✓ All contracts deployed successfully!")
        print("="*80)
        print()
        print("Next steps:")
        print("  1. Update .env with contract addresses")
        print("  2. Run initialization scripts")
        print(f"  3. Verify on Etherscan: https://{args.network}.etherscan.io")
        print()
        
    except Exception as e:
        print(f"\n✗ Deployment failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
