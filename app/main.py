"""
LIS Application Entry Point

Run:
python -m app.main
"""


from app.agents.task_agent import TaskAgent

from app.trust.identity import Identity
from app.trust.permission import Permission

from app.knowledge.atom import KnowledgeAtom
from app.knowledge.graph import KnowledgeGraph

from app.integration.lis_engine import LISEngine



def create_lis_engine():
    """
    Create LIS runtime engine.
    """


    # -------------------------
    # Knowledge
    # -------------------------

    graph = KnowledgeGraph()


    atom = KnowledgeAtom(
        atom_id="LIS-K001",
        title="Learning Intelligence Infrastructure",
        content="AI-Native University Platform",
        source="LIS Core",
        tags=[
            "AI",
            "Education"
        ]
    )


    graph.add_atom(
        atom
    )


    # -------------------------
    # Trust
    # -------------------------

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


    # -------------------------
    # Agent
    # -------------------------

    agent = TaskAgent(
        "LIS Task Agent"
    )


    # -------------------------
    # Engine
    # -------------------------

    engine = LISEngine(
        agent=agent,
        identity=identity,
        permission=permission,
        knowledge_graph=graph
    )


    return engine



def main():

    print("=" * 50)
    print("LIS - Learning Intelligence Infrastructure")
    print("Cognitive Foundation v1.0.0")
    print("=" * 50)


    engine = create_lis_engine()


    while True:

        task = input(
            "\nEnter task (exit to quit): "
        )


        if task.lower() == "exit":
            print("LIS shutdown.")
            break


        result = engine.execute(
            task,
            atom_id="LIS-K001"
        )


        print("\n--- LIS Response ---")
        print(result)



if __name__ == "__main__":
    main()