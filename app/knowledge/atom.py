"""
LIS Knowledge Atom

A Knowledge Atom represents a basic unit of knowledge
inside the Learning Intelligence Infrastructure.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class KnowledgeAtom:
    """
    Basic knowledge unit in LIS.

    Attributes:
        atom_id: Unique identifier
        title: Knowledge title
        content: Knowledge content
        source: Origin of knowledge
        tags: Semantic labels
    """

    atom_id: str
    title: str
    content: str
    source: str = ""
    tags: List[str] = field(default_factory=list)


    def summary(self) -> str:
        """
        Return a short description of the knowledge atom.
        """

        return f"{self.atom_id}: {self.title}"