from app.knowledge.atom import KnowledgeAtom
from app.knowledge.graph import KnowledgeGraph


def test_knowledge_graph():
	atom1 = KnowledgeAtom(
		atom_id="LIS-K001",
		title="Learning Intelligence Infrastructure",
		content="AI-Native learning infrastructure",
		source="LIS Architecture",
		tags=["AI", "Education"],
	)

	atom2 = KnowledgeAtom(
		atom_id="LIS-K002",
		title="Knowledge Graph",
		content="Network of knowledge relationships",
		source="LIS Knowledge Box",
		tags=["Knowledge", "Graph"],
	)

	graph = KnowledgeGraph()
	graph.add_atom(atom1)
	graph.add_atom(atom2)
	graph.connect("LIS-K001", "LIS-K002")

	related = graph.get_related("LIS-K001")

	assert "LIS-K002" in related

	print("Knowledge Relationship:", related)
	


if __name__ == "__main__":
	test_knowledge_graph()
