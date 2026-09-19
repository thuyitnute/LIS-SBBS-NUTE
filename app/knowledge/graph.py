"""
LIS Knowledge Graph

Manages relationships between Knowledge Atoms.
"""

from typing import Dict, List

from app.knowledge.atom import KnowledgeAtom


class KnowledgeGraph:
    """
    Basic graph structure for LIS knowledge relationships.
    """


    def __init__(self):
        self.atoms: Dict[str, KnowledgeAtom] = {}
        self.relationships: Dict[str, List[str]] = {}


    def add_atom(self, atom: KnowledgeAtom):
        """
        Add a knowledge atom into graph.
        """

        self.atoms[atom.atom_id] = atom
        self.relationships[atom.atom_id] = []


    def connect(self, source_id: str, target_id: str):
        """
        Create a relationship between two knowledge atoms.
        """

        if source_id in self.relationships:
            self.relationships[source_id].append(target_id)


    def get_related(self, atom_id: str) -> List[str]:
        """
        Return related knowledge atoms.
        """

        return self.relationships.get(atom_id, [])


    def get_atom(self, atom_id: str):
        """
        Return knowledge atom by id.
        """

        return self.atoms.get(atom_id)