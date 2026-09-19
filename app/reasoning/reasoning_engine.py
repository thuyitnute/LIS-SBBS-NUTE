"""
LIS Reasoning Engine

Provides reasoning capability
based on LIS Knowledge Graph.
"""


from typing import List

from app.knowledge.graph import KnowledgeGraph



class ReasoningEngine:
    """
    Reasoning engine using Knowledge Graph.
    """


    def __init__(
        self,
        knowledge_graph: KnowledgeGraph
    ):
        self.knowledge_graph = knowledge_graph
        self.history: List[str] = []


    def analyze(
        self,
        task: str,
        atom_id: str = ""
    ) -> str:
        """
        Analyze task with knowledge context.
        """


        self.history.append(task)


        knowledge_context = ""


        if atom_id:

            atom = (
                self.knowledge_graph
                .get_atom(atom_id)
            )


            if atom:

                knowledge_context = (
                    f"ID: {atom.atom_id}\n"
                    f"Title: {atom.title}\n"
                    f"Content: {atom.content}\n"
                    f"Tags: {atom.tags}"
                )


        if knowledge_context:

            return (
                f"Reasoning completed for task: {task}\n"
                f"Knowledge context:\n{knowledge_context}"
            )


        return (
            f"Reasoning completed for task: {task}\n"
            "Knowledge context: None"
        )


    def get_history(self) -> List[str]:
        """
        Return reasoning history.
        """

        return self.history