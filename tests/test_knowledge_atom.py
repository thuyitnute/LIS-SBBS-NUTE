from app.knowledge.atom import KnowledgeAtom


def test_create_knowledge_atom():

    atom = KnowledgeAtom(
        atom_id="LIS-K001",
        title="Learning Intelligence Infrastructure",
        content="AI-Native learning infrastructure",
        source="LIS Architecture",
        tags=[
            "AI",
            "Education",
            "Knowledge"
        ]
    )

    assert atom.atom_id == "LIS-K001"
    assert atom.title == "Learning Intelligence Infrastructure"

    print(atom.summary())


if __name__ == "__main__":
    test_create_knowledge_atom()