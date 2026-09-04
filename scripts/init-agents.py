#!/usr/bin/env python3
"""
Agent Initialization Script
Initializes AI agent pool with default agents
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agents.manager import AgentManager
from src.database import get_async_session


DEFAULT_AGENTS = [
    {
        "name": "Developer Agent",
        "agent_type": "developer",
        "description": "Autonomous code generation and optimization",
        "capabilities": ["code_generation", "refactoring", "bug_fixing"],
        "initial_stake": 1000,
    },
    {
        "name": "Architect Agent",
        "agent_type": "architect",
        "description": "System design and architecture optimization",
        "capabilities": ["design", "planning", "optimization"],
        "initial_stake": 1000,
    },
    {
        "name": "Tester Agent",
        "agent_type": "tester",
        "description": "Quality assurance and testing",
        "capabilities": ["testing", "validation", "bug_detection"],
        "initial_stake": 1000,
    },
    {
        "name": "Optimizer Agent",
        "agent_type": "optimizer",
        "description": "Performance and efficiency improvements",
        "capabilities": ["optimization", "performance", "efficiency"],
        "initial_stake": 1000,
    },
]


async def main():
    print("="*80)
    print("Agent Initialization")
    print("="*80)
    print()
    
    try:
        manager = AgentManager()
        
        print(f"Initializing {len(DEFAULT_AGENTS)} default agents...")
        print()
        
        for agent_config in DEFAULT_AGENTS:
            print(f"Creating {agent_config['name']}...")
            agent = await manager.create_agent(
                name=agent_config["name"],
                agent_type=agent_config["agent_type"],
                description=agent_config["description"],
                capabilities=agent_config["capabilities"],
            )
            print(f"  ✓ Created: {agent.id}")
            print(f"    Status: {agent.state}")
            print(f"    Capabilities: {', '.join(agent_config['capabilities'])}")
            print()
        
        print("="*80)
        print(f"✓ Successfully initialized {len(DEFAULT_AGENTS)} agents!")
        print("="*80)
        print()
        
    except Exception as e:
        print(f"\n✗ Error during agent initialization: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
