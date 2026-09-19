"""
Test LIS Engine Integration Flow
"""


from app.agents.task_agent import TaskAgent
from app.trust.identity import Identity
from app.trust.permission import Permission
from app.integration.lis_engine import LISEngine



def test_lis_engine():

    identity = Identity(
        identity_id="AGENT-001",
        name="LIS Research Agent",
        entity_type="AI_AGENT"
    )


    permission = Permission(
        identity_id="AGENT-001"
    )


    permission.add_permission(
        "READ_KNOWLEDGE"
    )


    agent = TaskAgent(
        "LIS Task Agent"
    )


    engine = LISEngine(
        agent=agent,
        identity=identity,
        permission=permission
    )


    result = engine.execute(
        "Analyze Knowledge Graph"
    )


    assert result == (
        "LIS Task Agent executed task: "
        "Analyze Knowledge Graph"
    )


    print(result)



if __name__ == "__main__":
    test_lis_engine()