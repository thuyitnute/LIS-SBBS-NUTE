"""
LIS Integration Layer

Provides orchestration components
that connect Smart Boxes:

- Knowledge Box
- Agent Box
- Trust Box
- Reasoning Layer
"""

from app.integration.lis_engine import LISEngine


__all__ = [
    "LISEngine",
]