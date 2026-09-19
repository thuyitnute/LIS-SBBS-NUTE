"""
Test LIS Reasoning Engine

Version:
LIS v0.8.0 - Knowledge Reasoning Integration
"""


from app.knowledge.atom import KnowledgeAtom
from app.knowledge.graph import KnowledgeGraph

from app.reasoning.reasoning_engine import ReasoningEngine



def test_reasoning_engine():

    # Create Knowledge Atom

    atom_1 = KnowledgeAtom(
        atom_id="LIS-K001",
        title="Learning Intelligence Infrastructure",
        content="AI-Native University Platform",
        tags=[
            "AI",
            "Education"
        ]
    )


    atom_2 = KnowledgeAtom(
        atom_id="LIS-K002",
        title="Smart Black Box System",
        content="SBBS Architecture",
        tags=[
            "Architecture"
        ]
    )


    # Create Knowledge Graph

    graph = KnowledgeGraph()


    graph.add_atom(atom_1)
    graph.add_atom(atom_2)


    graph.connect(
        "LIS-K001",
        "LIS-K002"
    )


    # Create Reasoning Engine

    engine = ReasoningEngine(
        graph
    )


    # Analyze task

    result = engine.analyze(
        "Analyze LIS Architecture",
        atom_id="LIS-K001"
    )


    # Verify reasoning result

    assert (
        "Reasoning completed for task: Analyze LIS Architecture"
        in result
    )


    assert (
        "LIS-K002"
        in result
    )


    print(result)



if __name__ == "__main__":
    test_reasoning_engine()