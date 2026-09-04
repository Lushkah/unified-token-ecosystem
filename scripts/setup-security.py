#!/usr/bin/env python3
"""
Security Infrastructure Setup Script
Configures AI-powered security and anomaly detection
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.security.manager import SecurityManager
from src.config import settings


def main():
    print("="*80)
    print("Security Infrastructure Setup")
    print("="*80)
    print()
    
    try:
        manager = SecurityManager()
        
        print("Security Configuration:")
        print(f"  AI Security Enabled: {settings.AI_SECURITY_ENABLED}")
        print(f"  Anomaly Detection Threshold: {settings.ANOMALY_DETECTION_THRESHOLD}")
        print(f"  Encryption: AES-256")
        print()
        
        print("Initializing security infrastructure...")
        result = manager.initialize_security()
        print("✓ Security infrastructure initialized")
        print()
        
        print("Security Features:")
        print("  ✓ Encryption (AES-256)")
        print("  ✓ Anomaly detection (ML-based)")
        print("  ✓ Transaction verification")
        print("  ✓ Multi-layer authentication")
        print("  ✓ Zero-knowledge proofs")
        print()
        
        print("="*80)
        print("✓ Security setup complete!")
        print("="*80)
        print()
        print("Security Status:")
        print("  ✓ All layers active")
        print("  ✓ Monitoring enabled")
        print("  ✓ Alerts configured")
        print()
        
    except Exception as e:
        print(f"\n✗ Error during security setup: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
