# Unified Token Ecosystem - Deployment Guide

## Pre-Deployment Checklist

- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Environment variables configured (`.env` file)
- [ ] Database initialized (`python scripts/init-db.py`)
- [ ] Smart contracts compiled and ready
- [ ] Wallet with sufficient ETH for gas fees
- [ ] API keys configured (OpenAI, Alchemy, etc.)

---

## Deployment Steps

### 1. Local Development

```bash
# Install dependencies
pip install -r requirements.txt
npm install

# Start services
docker-compose up -d

# Initialize database
python scripts/init-db.py

# Run the application
python main.py
```

Access at: http://localhost:8000

### 2. Testnet Deployment (Sepolia)

```bash
# Set environment
export PLATFORM_ENV=testnet
export ETH_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY

# Deploy smart contracts
python scripts/deploy-contracts.py --network=sepolia

# Start application
python main.py
```

### 3. Mainnet Deployment (Production)

```bash
# Set environment
export PLATFORM_ENV=production
export ETH_RPC_URL=https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY

# Deploy smart contracts
python scripts/deploy-contracts.py --network=mainnet

# Start with production server
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

---

## Docker Deployment

### Build Image

```bash
docker build -t token-ecosystem:latest .
```

### Run Container

```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:pass@db:5432/token_ecosystem \
  -e REDIS_URL=redis://cache:6379/0 \
  token-ecosystem:latest
```

### Docker Compose (All Services)

```bash
docker-compose up -d
```

---

## Kubernetes Deployment

See `k8s/` directory for Kubernetes manifests.

```bash
kubectl apply -f k8s/
```

---

## Smart Contract Deployment

### Compile Contracts

```bash
hardhat compile
```

### Deploy to Testnet

```bash
hardhat run scripts/deploy.js --network sepolia
```

### Deploy to Mainnet

```bash
hardhat run scripts/deploy.js --network mainnet
```

---

## Post-Deployment

### Verify Deployment

```bash
# Health check
curl http://localhost:8000/health

# API docs
http://localhost:8000/docs
```

### Initialize Agent Pool

```bash
python scripts/init-agents.py
```

### Fund Treasury

```bash
python scripts/fund-treasury.py --amount 1000000
```

---

## Monitoring

- **Prometheus**: http://localhost:9090
- **Logs**: `docker logs token-ecosystem-app`
- **Database**: Connect with `psql` to monitor queries

---

## Backup & Recovery

### Database Backup

```bash
docker exec token-ecosystem-db pg_dump -U tokenuser token_ecosystem > backup.sql
```

### Restore

```bash
docker exec -i token-ecosystem-db psql -U tokenuser token_ecosystem < backup.sql
```

---

## Troubleshooting

### Database Connection Issues

```bash
# Test connection
docker exec token-ecosystem-db psql -U tokenuser -d token_ecosystem -c "SELECT 1"
```

### Smart Contract Deployment Failed

```bash
# Check wallet balance
hardhat run scripts/check-balance.js --network sepolia

# Check gas prices
hardhat run scripts/check-gas.js --network sepolia
```

### Agent Startup Issues

```bash
# Check logs
docker logs token-ecosystem-app | tail -f

# Restart agents
python scripts/restart-agents.py
```

---

## Security

1. **Keep `.env` files secure** - Never commit to git
2. **Rotate API keys** regularly
3. **Use hardware wallet** for mainnet deployments
4. **Enable 2FA** on sensitive accounts
5. **Monitor contract interactions** via Etherscan

---

## Performance Tuning

### Database Optimization

```sql
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_agents_state ON agents(state);
```

### Redis Configuration

```bash
redis-cli CONFIG SET maxmemory-policy allkeys-lru
redis-cli CONFIG SAVE
```

---

## Ready to Deploy?

For detailed instructions, see [Getting Started](./docs/getting-started/README.md)
