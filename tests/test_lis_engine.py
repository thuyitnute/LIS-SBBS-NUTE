"""
Test LIS Engine

Version:
LIS v0.9.0 - Knowledge Retrieval Enhancement
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
    Knowledge Retrieval
        ↓
    ReasoningEngine
        ↓
    TaskAgent
        ↓
    Result
    """


    # -----------------------------
    # Create Knowledge Layer
    # -----------------------------

    atom = KnowledgeAtom(
        atom_id="LIS-K001",
        title="Learning Intelligence Infrastructure",
        content="AI-Native University Platform",
        source="LIS Research",
        tags=[
            "AI",
            "Education"
        ]
    )


    graph = KnowledgeGraph()


    graph.add_atom(
        atom
    )


    # -----------------------------
    # Create Trust Layer
    # -----------------------------

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


    # -----------------------------
    # Create Agent Layer
    # -----------------------------

    agent = TaskAgent(
        "LIS Task Agent"
    )


    # -----------------------------
    # Create LIS Engine
    # -----------------------------

    engine = LISEngine(
        agent=agent,
        identity=identity,
        permission=permission,
        knowledge_graph=graph
    )


    # -----------------------------
    # Execute LIS Workflow
    # -----------------------------

    result = engine.execute(
        "Analyze LIS Architecture",
        atom_id="LIS-K001"
    )


    # -----------------------------
    # Verify Reasoning Layer
    # -----------------------------

    assert (
        "Reasoning completed for task: Analyze LIS Architecture"
        in result
    )


    # -----------------------------
    # Verify Knowledge Retrieval
    # -----------------------------

    assert (
        "ID: LIS-K001"
        in result
    )


    assert (
        "Title: Learning Intelligence Infrastructure"
        in result
    )


    assert (
        "Content: AI-Native University Platform"
        in result
    )


    # -----------------------------
    # Verify Agent Execution
    # -----------------------------

    assert (
        "LIS Task Agent executed task: Analyze LIS Architecture"
        in result
    )


    print(result)



if __name__ == "__main__":
    test_lis_engine()