"""
Test LIS Reasoning Engine

Version:
LIS v0.9.0 - Knowledge Retrieval Enhancement
"""


from app.knowledge.atom import KnowledgeAtom
from app.knowledge.graph import KnowledgeGraph

from app.reasoning.reasoning_engine import ReasoningEngine



def test_reasoning_engine():

    atom_1 = KnowledgeAtom(
        atom_id="LIS-K001",
        title="Learning Intelligence Infrastructure",
        content="AI-Native University Platform",
        tags=[
            "AI",
            "Education"
        ]
    )


    graph = KnowledgeGraph()


    graph.add_atom(
        atom_1
    )


    engine = ReasoningEngine(
        graph
    )


    result = engine.analyze(
        "Analyze LIS Architecture",
        atom_id="LIS-K001"
    )


    assert (
        "Reasoning completed for task: Analyze LIS Architecture"
        in result
    )


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


    print(result)



if __name__ == "__main__":
    test_reasoning_engine()