#!/usr/bin/env python3
"""
Local Development Setup Helper
Automated setup for local development environment
"""

import os
import sys
import subprocess
import platform
from pathlib import Path


class LocalDevSetup:
    def __init__(self):
        self.platform = platform.system()
        self.project_root = Path(__file__).parent
        self.venv_path = self.project_root / "venv"
        self.env_file = self.project_root / ".env"
        
    def print_header(self, text):
        print(f"\n{'='*80}")
        print(f"  {text}")
        print(f"{'='*80}\n")
    
    def print_step(self, step, text):
        print(f"\n[{step}] {text}")
        print("-" * 80)
    
    def run_command(self, command, description):
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, cwd=self.project_root)
        if result.returncode != 0:
            print(f"\n❌ Failed: {description}")
            return False
        print(f"✓ {description}")
        return True
    
    def step_1_check_prerequisites(self):
        self.print_step("1/8", "Checking Prerequisites")
        
        checks = [
            ("python3 --version", "Python 3.10+"),
            ("node --version", "Node.js 18+"),
            ("docker --version", "Docker"),
            ("docker-compose --version", "Docker Compose"),
            ("git --version", "Git"),
        ]
        
        all_ok = True
        for command, name in checks:
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"✓ {name}: {result.stdout.strip()}")
                else:
                    print(f"❌ {name}: NOT INSTALLED")
                    all_ok = False
            except Exception as e:
                print(f"❌ {name}: Error checking - {e}")
                all_ok = False
        
        if not all_ok:
            print("\n⚠️  Please install missing prerequisites")
            return False
        
        print("\n✓ All prerequisites installed")
        return True
    
    def step_2_create_venv(self):
        self.print_step("2/8", "Creating Virtual Environment")
        
        if self.venv_path.exists():
            print(f"✓ Virtual environment already exists: {self.venv_path}")
            return True
        
        if self.run_command(f"python3 -m venv {self.venv_path}", "Virtual environment created"):
            if self.platform == "Windows":
                activate_cmd = f"{self.venv_path}\\Scripts\\activate"
                print(f"\nTo activate, run: {activate_cmd}")
            else:
                activate_cmd = f"source {self.venv_path}/bin/activate"
                print(f"\nTo activate, run: {activate_cmd}")
            return True
        return False
    
    def step_3_install_dependencies(self):
        self.print_step("3/8", "Installing Python Dependencies")
        
        if self.platform == "Windows":
            activate_script = self.venv_path / "Scripts" / "activate"
            pip_cmd = f"{self.venv_path}\\Scripts\\pip"
        else:
            activate_script = self.venv_path / "bin" / "activate"
            pip_cmd = f"{self.venv_path}/bin/pip"
        
        return self.run_command(
            f"{pip_cmd} install -r requirements.txt",
            "Python dependencies installed"
        )
    
    def step_4_install_npm_deps(self):
        self.print_step("4/8", "Installing Node.js Dependencies")
        return self.run_command("npm install", "Node.js dependencies installed")
    
    def step_5_create_env_file(self):
        self.print_step("5/8", "Creating .env Configuration File")
        
        if self.env_file.exists():
            print(f"✓ .env file already exists")
            return True
        
        env_content = """# Platform Configuration
PLATFORM_ENV=development
PLATFORM_HOST=0.0.0.0
PLATFORM_PORT=8000
PLATFORM_DEBUG=true
LOG_LEVEL=DEBUG

# CORS Configuration
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]

# Database Configuration
DATABASE_URL=postgresql://tokenuser:tokenpass@localhost:5432/token_ecosystem
DATABASE_ECHO=true

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
REDIS_CACHE_TTL=3600

# JWT Configuration
JWT_SECRET_KEY=your-dev-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# OpenAI Configuration
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-4

# Blockchain Configuration
ETH_RPC_URL=http://localhost:8545
ETH_MAINNET_RPC_URL=https://eth-mainnet.g.alchemy.com/v2/your-api-key
ETH_SEPOLIA_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/your-api-key

# Smart Contract Deployment
PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb476cadccee33ecb9f27f5eaa67
PAYER_ADDRESS=0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266

# Token Configuration
TOKEN_NAME=Unified Token
TOKEN_SYMBOL=UTE
TOKEN_DECIMALS=18
TOKEN_INITIAL_SUPPLY=1000000000

# Contract Addresses
TOKEN_CONTRACT_ADDRESS=0x0000000000000000000000000000000000000000
REWARDS_CONTRACT_ADDRESS=0x0000000000000000000000000000000000000000
GOVERNANCE_CONTRACT_ADDRESS=0x0000000000000000000000000000000000000000

# Security Configuration
ENCRYPTION_KEY=your-32-char-encryption-key-12345
AI_SECURITY_ENABLED=true
ANOMALY_DETECTION_THRESHOLD=0.8

# Agent Configuration
AGENT_MAX_RETRIES=3
AGENT_TIMEOUT_SECONDS=300
AGENT_PARALLEL_TASKS=5

# Task Configuration
TASK_QUEUE_SIZE=1000
TASK_TIMEOUT_SECONDS=600
TASK_RETRY_DELAY_SECONDS=30

# Reward Configuration
BASE_REWARD_PER_TASK=10
QUALITY_BONUS_MULTIPLIER=1.5
INNOVATION_BONUS=50
EFFICIENCY_BONUS_MULTIPLIER=1.2

# Development Tools
DEBUG_MODE=true
PROFILE_ENABLED=true
"""
        
        try:
            with open(self.env_file, "w") as f:
                f.write(env_content)
            print(f"✓ .env file created: {self.env_file}")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    
    def step_6_start_docker(self):
        self.print_step("6/8", "Starting Docker Services")
        return self.run_command(
            "docker-compose up -d",
            "Docker services started (PostgreSQL, Redis, App)"
        )
    
    def step_7_init_database(self):
        self.print_step("7/8", "Initializing Database")
        
        if self.platform == "Windows":
            python_cmd = f"{self.venv_path}\\Scripts\\python"
        else:
            python_cmd = f"{self.venv_path}/bin/python"
        
        return self.run_command(
            f"{python_cmd} scripts/init-db.py",
            "Database schema initialized"
        )
    
    def step_8_final_info(self):
        self.print_step("8/8", "Setup Complete!")
        
        self.print_header("🎉 Local Development Environment Ready!")
        
        print("\n📝 Next Steps:")
        print("\n1. Activate Virtual Environment:")
        if self.platform == "Windows":
            print(f"   .\\venv\\Scripts\\activate")
        else:
            print(f"   source venv/bin/activate")
        
        print("\n2. Start the Application:")
        print("   python main.py")
        
        print("\n3. Access the Application:")
        print("   API:         http://localhost:8000")
        print("   API Docs:    http://localhost:8000/docs")
        print("   Health:      http://localhost:8000/health")
        
        print("\n4. View Docker Services:")
        print("   docker-compose ps")
        
        print("\n5. View Logs:")
        print("   docker-compose logs -f app")
        
        print("\n6. Run Tests:")
        print("   pytest")
        
        print("\n📚 Documentation:")
        print("   - Local Dev Guide: LOCAL_DEV.md")
        print("   - Full Docs: ./docs/")
        print("   - API Docs: http://localhost:8000/docs")
        
        print("\n💡 Tips:")
        print("   - Code changes auto-reload (PLATFORM_DEBUG=true)")
        print("   - Database is in PostgreSQL running in Docker")
        print("   - Cache is Redis running in Docker")
        print("   - Blockchain runs on local Hardhat (optional)")
        
        print("\n🚀 You're all set! Happy coding!\n")
    
    def run_setup(self):
        self.print_header("Unified Token Ecosystem - Local Development Setup")
        
        steps = [
            ("Checking Prerequisites", self.step_1_check_prerequisites),
            ("Creating Virtual Environment", self.step_2_create_venv),
            ("Installing Python Dependencies", self.step_3_install_dependencies),
            ("Installing Node.js Dependencies", self.step_4_install_npm_deps),
            ("Creating .env File", self.step_5_create_env_file),
            ("Starting Docker Services", self.step_6_start_docker),
            ("Initializing Database", self.step_7_init_database),
        ]
        
        for step_name, step_func in steps:
            if not step_func():
                print(f"\n❌ Setup failed at: {step_name}")
                print("Please fix the issue and run again.")
                return False
        
        self.step_8_final_info()
        return True


if __name__ == "__main__":
    setup = LocalDevSetup()
    success = setup.run_setup()
    sys.exit(0 if success else 1)
