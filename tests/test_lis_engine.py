"""
Test LIS Engine Integration Flow

Version:
LIS v0.7.0 - Reasoning Layer Integration
"""


from app.agents.task_agent import TaskAgent

from app.trust.identity import Identity
from app.trust.permission import Permission

from app.integration.lis_engine import LISEngine



def test_lis_engine():
    """
    Test complete LIS execution flow.

    Flow:

    Identity
        ↓
    Permission
        ↓
    ReasoningEngine
        ↓
    TaskAgent
        ↓
    Result
    """


    # Create Identity

    identity = Identity(
        identity_id="AGENT-001",
        name="LIS Research Agent",
        entity_type="AI_AGENT"
    )


    # Create Permission

    permission = Permission(
        identity_id="AGENT-001"
    )


    permission.add_permission(
        "READ_KNOWLEDGE"
    )


    # Create Agent

    agent = TaskAgent(
        "LIS Task Agent"
    )


    # Create LIS Engine

    engine = LISEngine(
        agent=agent,
        identity=identity,
        permission=permission
    )


    # Execute task

    result = engine.execute(
        "Analyze Knowledge Graph"
    )


    # Verify Reasoning Layer

    assert (
        "Reasoning completed for task: Analyze Knowledge Graph"
        in result
    )


    # Verify Agent Layer

    assert (
        "LIS Task Agent executed task: Analyze Knowledge Graph"
        in result
    )


    print(result)



if __name__ == "__main__":
    test_lis_engine()