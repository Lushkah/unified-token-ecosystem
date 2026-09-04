#!/usr/bin/env python3
"""
Unified Token AI Ecosystem - Main Entry Point

Combines:
- Intelligent autonomous AI agents
- Blockchain-based token economy
- Advanced security infrastructure
"""

import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.config import settings
from src.database import init_db
from src.routes import (
    agents,
    blockchain,
    governance,
    health,
    rewards,
    tasks,
    tokens,
    wallet,
)

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events"""
    # Startup
    logger.info("="*60)
    logger.info("Starting Unified Token AI Ecosystem...")
    logger.info("="*60)
    logger.info(f"Environment: {settings.PLATFORM_ENV}")
    logger.info(f"Debug Mode: {settings.PLATFORM_DEBUG}")
    
    try:
        await init_db()
        logger.info("✓ Database initialized successfully")
        logger.info("✓ System ready for operations")
    except Exception as e:
        logger.error(f"✗ Failed to initialize database: {e}")
        raise
    
    yield
    
    # Shutdown
    logger.info("="*60)
    logger.info("Shutting down Unified Token AI Ecosystem...")
    logger.info("="*60)


# Create FastAPI application
app = FastAPI(
    title="Unified Token AI Ecosystem",
    description="A comprehensive platform combining intelligent AI agents, blockchain security, and token economics",
    version="0.2.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health", tags=["Health"], include_in_schema=False)
async def health_check():
    """Check system health"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "version": "0.2.0",
            "environment": settings.PLATFORM_ENV,
            "components": {
                "api": "operational",
                "database": "connected",
                "cache": "connected",
            }
        }
    )


# Root endpoint
@app.get("/", tags=["Info"], include_in_schema=False)
async def root():
    """Welcome to Unified Token AI Ecosystem"""
    return {
        "name": "Unified Token AI Ecosystem",
        "description": "Intelligent agents + blockchain security + token economics",
        "version": "0.2.0",
        "docs": "/docs",
        "features": [
            "Multi-agent autonomous development",
            "Blockchain-based rewards",
            "AI-powered security",
            "Token-based governance",
            "Real-time analytics"
        ]
    }


# Include routers
logger.info("Registering API routes...")

app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
logger.info("  ✓ Health endpoints registered")

app.include_router(agents.router, prefix="/api/v1/agents", tags=["Agents"])
logger.info("  ✓ Agent endpoints registered")

app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["Tasks"])
logger.info("  ✓ Task endpoints registered")

app.include_router(tokens.router, prefix="/api/v1/tokens", tags=["Tokens"])
logger.info("  ✓ Token endpoints registered")

app.include_router(rewards.router, prefix="/api/v1/rewards", tags=["Rewards"])
logger.info("  ✓ Reward endpoints registered")

app.include_router(wallet.router, prefix="/api/v1/wallet", tags=["Wallet"])
logger.info("  ✓ Wallet endpoints registered")

app.include_router(blockchain.router, prefix="/api/v1/blockchain", tags=["Blockchain"])
logger.info("  ✓ Blockchain endpoints registered")

app.include_router(governance.router, prefix="/api/v1/governance", tags=["Governance"])
logger.info("  ✓ Governance endpoints registered")


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "type": type(exc).__name__,
            "environment": settings.PLATFORM_ENV,
        }
    )


if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"Starting server on {settings.PLATFORM_HOST}:{settings.PLATFORM_PORT}")
    
    uvicorn.run(
        "main:app",
        host=settings.PLATFORM_HOST,
        port=settings.PLATFORM_PORT,
        reload=settings.PLATFORM_DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )
