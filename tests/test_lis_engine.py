"""
Test LIS Engine

Version:
LIS v0.8.0 - Knowledge Reasoning Integration
"""


from app.agents.task_agent import TaskAgent

from app.trust.identity import Identity
from app.trust.permission import Permission

from app.knowledge.atom import KnowledgeAtom
from app.knowledge.graph import KnowledgeGraph

from app.integration.lis_engine import LISEngine



def test_lis_engine():
    """
    Test complete LIS pipeline.

    Flow:

    Identity
        ↓
    Permission
        ↓
    KnowledgeGraph
        ↓
    ReasoningEngine
        ↓
    TaskAgent
        ↓
    Result
    """


    # Create Knowledge Atoms

    atom_1 = KnowledgeAtom(
        atom_id="LIS-K001",
        title="Learning Intelligence Infrastructure",
        content="AI-Native University Platform"
    )


    atom_2 = KnowledgeAtom(
        atom_id="LIS-K002",
        title="Smart Black Box System",
        content="SBBS Architecture"
    )


    # Create Knowledge Graph

    graph = KnowledgeGraph()

    graph.add_atom(atom_1)

    graph.add_atom(atom_2)


    graph.connect(
        "LIS-K001",
        "LIS-K002"
    )


    # Create Trust Identity

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
        permission=permission,
        knowledge_graph=graph
    )


    # Execute

    result = engine.execute(
        "Analyze LIS Architecture",
        atom_id="LIS-K001"
    )


    # Verify Knowledge Reasoning

    assert (
        "Reasoning completed for task: Analyze LIS Architecture"
        in result
    )


    assert (
        "LIS-K002"
        in result
    )


    # Verify Agent Execution

    assert (
        "LIS Task Agent executed task: Analyze LIS Architecture"
        in result
    )


    print(result)



if __name__ == "__main__":
    test_lis_engine()