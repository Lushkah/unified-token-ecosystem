# Unified Token Ecosystem - Local Development Guide

## 🚀 Quick Start for Local Development

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker & Docker Compose
- Git
- A code editor (VSCode, PyCharm, etc.)

---

## 📋 Step 1: Setup Local Environment

### Clone the Repository
```bash
git clone https://github.com/Lushkah/unified-token-ecosystem.git
cd unified-token-ecosystem
```

### Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Install Dependencies
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies
npm install
```

---

## 🔧 Step 2: Configure Local Environment

### Create .env File
```bash
# Copy example environment
cp .env.example .env

# Edit .env with your local settings
cat > .env << 'EOF'
# Platform Configuration
PLATFORM_ENV=development
PLATFORM_HOST=0.0.0.0
PLATFORM_PORT=8000
PLATFORM_DEBUG=true
LOG_LEVEL=DEBUG

# CORS Configuration
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]

# Database Configuration (Local PostgreSQL)
DATABASE_URL=postgresql://tokenuser:tokenpass@localhost:5432/token_ecosystem
DATABASE_ECHO=true

# Redis Configuration
REDIS_URL=redis://localhost:6379/0
REDIS_CACHE_TTL=3600

# JWT Configuration
JWT_SECRET_KEY=your-dev-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# OpenAI Configuration (optional for local dev)
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-4

# Blockchain Configuration (Local Hardhat)
ETH_RPC_URL=http://localhost:8545
ETH_MAINNET_RPC_URL=https://eth-mainnet.g.alchemy.com/v2/your-api-key
ETH_SEPOLIA_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/your-api-key

# Smart Contract Deployment (Local)
PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb476cadccee33ecb9f27f5eaa67
PAYER_ADDRESS=0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266

# Token Contract Configuration
TOKEN_NAME=Unified Token
TOKEN_SYMBOL=UTE
TOKEN_DECIMALS=18
TOKEN_INITIAL_SUPPLY=1000000000

# Contract Addresses (Will be set after deployment)
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
EOF
```

---

## 🐳 Step 3: Start Docker Services

### Start Infrastructure
```bash
# Start all services (PostgreSQL, Redis, App)
docker-compose up -d

# Verify services are running
docker-compose ps
```

### Check Service Status
```bash
# PostgreSQL
docker exec token-ecosystem-db psql -U tokenuser -d token_ecosystem -c "SELECT 1"

# Redis
docker exec token-ecosystem-cache redis-cli ping
```

---

## 💾 Step 4: Initialize Database

### Create Database Schema
```bash
# Initialize database
python scripts/init-db.py

# Run migrations
alembic upgrade head
```

### Verify Database
```bash
# Connect to database
docker exec -it token-ecosystem-db psql -U tokenuser -d token_ecosystem

# List tables
\dt

# Exit
\q
```

---

## 🤖 Step 5: Initialize Agents (Optional)

### Create Default Agent Pool
```bash
# Initialize agents
python scripts/init-agents.py
```

### View Available Agents
```bash
curl http://localhost:8000/api/v1/agents
```

---

## 🏃 Step 6: Run the Application

### Development Mode (with auto-reload)
```bash
# Start with hot-reload
python main.py

# Or with additional debug output
PLATFORM_DEBUG=true python main.py
```

### API Server Should Start
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started server process [12345]
```

### Access the Application
```
🌐 API:         http://localhost:8000
📖 API Docs:    http://localhost:8000/docs
🏥 Health:      http://localhost:8000/health
```

---

## 🧪 Step 7: Test the Application

### Check API Health
```bash
curl http://localhost:8000/health
```

### View API Documentation
```
Open browser: http://localhost:8000/docs
```

### Test Endpoints
```bash
# Get all agents
curl http://localhost:8000/api/v1/agents

# Get system info
curl http://localhost:8000/

# Create a task
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Task", "description": "Testing the API"}'
```

---

## 🔍 Step 8: Development Workflow

### File Structure for Development
```
unified-token-ecosystem/
├── src/                    # Source code
│   ├── agents/            # Agent implementations
│   ├── blockchain/        # Blockchain integration
│   ├── security/          # Security modules
│   ├── economics/         # Token economics
│   ├── tasks/             # Task management
│   ├── routes/            # API routes
│   └── config.py          # Configuration
├── scripts/               # Deployment scripts
├── tests/                 # Unit & integration tests
├── docs/                  # Documentation
├── main.py                # Entry point
└── requirements.txt       # Dependencies
```

### Make Code Changes
```bash
# Edit files in src/ directory
# Changes will auto-reload due to PLATFORM_DEBUG=true
```

### Run Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_agents.py

# Run with verbose output
pytest -v
```

### Check Code Quality
```bash
# Format code
black .

# Check linting
flake8 .

# Type checking
mypy .

# All checks
make lint
```

---

## 📊 Step 9: Local Blockchain (Optional)

### Setup Local Hardhat Network
```bash
# Install Hardhat (if not already installed)
npm install --save-dev hardhat

# Start local blockchain
npx hardhat node

# In .env, set:
ETH_RPC_URL=http://localhost:8545
```

### Deploy Contracts Locally
```bash
# Compile contracts
npx hardhat compile

# Deploy to local network
python scripts/deploy-contracts.py --network=local
```

---

## 🔐 Step 10: Local Testing with MetaMask

### Add Local Network to MetaMask
1. Open MetaMask extension
2. Click network dropdown → "Add Network"
3. Configure:
   - Network Name: "Local Hardhat"
   - RPC URL: `http://localhost:8545`
   - Chain ID: `31337`
   - Currency Symbol: `ETH`
4. Click Save

### Import Test Account
1. In MetaMask, click account icon → "Import Account"
2. Paste private key: `0xac0974bec39a17e36ba4a6b4d238ff944bacb476cadccee33ecb9f27f5eaa67`
3. Account will have 10000 ETH for testing

---

## 🎯 Development Commands Reference

### Docker Management
```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f app

# Rebuild images
docker-compose up -d --build
```

### Database
```bash
# Initialize database
python scripts/init-db.py

# Run migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1

# Create new migration
alembic revision --autogenerate -m "Description"
```

### Testing
```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src

# Run async tests
pytest -m asyncio
```

### Code Quality
```bash
# Format code
black .

# Sort imports
isort .

# Lint check
flake8 .

# Type check
mypy .
```

### API
```bash
# Health check
curl http://localhost:8000/health

# View API docs
open http://localhost:8000/docs

# Test endpoint
curl http://localhost:8000/api/v1/agents
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in .env
PLATFORM_PORT=8001

# Or kill process using port 8000
sudo lsof -ti:8000 | xargs kill -9
```

### Database Connection Error
```bash
# Check if PostgreSQL is running
docker exec token-ecosystem-db pg_isready

# Restart PostgreSQL
docker-compose restart postgres
```

### Redis Connection Error
```bash
# Check if Redis is running
docker exec token-ecosystem-cache redis-cli ping

# Restart Redis
docker-compose restart redis
```

### Hot-Reload Not Working
```bash
# Ensure PLATFORM_DEBUG=true in .env
# Restart the application
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
```

---

## 📚 Additional Resources

### Documentation
- [API Documentation](http://localhost:8000/docs)
- [Agent Development Guide](./docs/agents/README.md)
- [System Architecture](./docs/architecture/README.md)
- [Token Economics](./docs/economics/tokenomics.md)

### Useful Tools
- **Postman**: API testing
- **DBeaver**: Database management
- **Redis Commander**: Redis browser
- **Hardhat**: Local blockchain

### IDE Setup (VSCode)

#### Install Extensions
- Python
- Pylance
- Black Formatter
- Flake8
- autoDocstring
- REST Client

#### Create `.vscode/settings.json`
```json
{
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": ["--max-line-length=100"],
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length=100"],
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter"
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

---

## 🎓 Next Steps

1. **Explore the API**: Visit http://localhost:8000/docs
2. **Run Tests**: Execute `pytest` to verify everything works
3. **Read Documentation**: Check `docs/` directory for detailed guides
4. **Create Agents**: Develop custom agents following `docs/agents/README.md`
5. **Deploy Contracts**: Deploy smart contracts for local testing

---

## 💡 Tips for Local Development

1. **Always use virtual environment** to avoid dependency conflicts
2. **Use `.env` file** for configuration (never commit to git)
3. **Enable debug mode** for better error messages
4. **Use VSCode REST Client** extension for API testing
5. **Check logs regularly** with `docker-compose logs -f app`
6. **Run tests before committing** with `pytest`
7. **Format code** with `black .` before pushing
8. **Keep dependencies updated** with `pip install -r requirements.txt --upgrade`

---

## 🚀 Ready to Start Developing!

Your local development environment is now ready. Start with Step 1 above and you'll be up and running in minutes! 🎉

For questions or issues, check the troubleshooting section or review the detailed documentation in the `docs/` directory.
