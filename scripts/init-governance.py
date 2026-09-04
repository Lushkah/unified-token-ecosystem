#!/usr/bin/env python3
"""
Governance System Initialization Script
Sets up DAO and voting mechanisms
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.governance.manager import GovernanceManager
from src.config import settings


def main():
    print("="*80)
    print("Governance System Initialization")
    print("="*80)
    print()
    
    try:
        manager = GovernanceManager()
        
        print("Governance Configuration:")
        print(f"  Voting Period: {settings.VOTING_PERIOD_BLOCKS} blocks")
        print(f"  Quorum: {settings.VOTING_QUORUM_PERCENTAGE}%")
        print(f"  Proposal Threshold: {settings.PROPOSAL_THRESHOLD:,} tokens")
        print()
        
        print("Initializing governance system...")
        result = manager.initialize_governance()
        print("✓ Governance system initialized")
        print()
        
        print("Governance Features:")
        print("  ✓ Proposal creation")
        print("  ✓ Token-based voting")
        print("  ✓ Treasury management")
        print("  ✓ Policy enforcement")
        print()
        
        print("="*80)
        print("✓ Governance initialization complete!")
        print("="*80)
        print()
        print("Governance contract: ", settings.GOVERNANCE_CONTRACT_ADDRESS)
        print()
        
    except Exception as e:
        print(f"\n✗ Error during governance initialization: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
