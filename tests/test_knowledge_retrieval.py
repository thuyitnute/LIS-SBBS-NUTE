"""
Test LIS Knowledge Retrieval

Version:
LIS v0.9.0 - Knowledge Retrieval Enhancement
"""


from app.knowledge.atom import KnowledgeAtom
from app.knowledge.graph import KnowledgeGraph



def test_knowledge_retrieval():

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


    retrieved = graph.get_atom(
        "LIS-K001"
    )


    assert retrieved is not None


    assert (
        retrieved.title
        ==
        "Learning Intelligence Infrastructure"
    )


    assert (
        retrieved.content
        ==
        "AI-Native University Platform"
    )


    print(
        retrieved.summary()
    )



if __name__ == "__main__":
    test_knowledge_retrieval()