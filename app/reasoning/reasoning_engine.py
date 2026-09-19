"""
LIS Reasoning Engine

Provides reasoning capability
with reasoning trace support.
"""


from typing import List

from app.knowledge.graph import KnowledgeGraph

from app.reasoning.trace import ReasoningTrace



class ReasoningEngine:
    """
    Reasoning engine using Knowledge Graph
    with trace recording.
    """


    def __init__(
        self,
        knowledge_graph: KnowledgeGraph
    ):

        self.knowledge_graph = knowledge_graph

        self.history: List[str] = []

        self.traces: List[ReasoningTrace] = []



    def analyze(
        self,
        task: str,
        atom_id: str = ""
    ) -> str:
        """
        Analyze task and create reasoning trace.
        """


        self.history.append(
            task
        )


        trace = ReasoningTrace(
            task=task
        )


        knowledge_context = ""


        if atom_id:

            atom = (
                self.knowledge_graph
                .get_atom(atom_id)
            )


            if atom:

                trace.knowledge_used.append(
                    atom.atom_id
                )


                trace.add_step(
                    "Retrieve knowledge context"
                )


                trace.add_step(
                    "Analyze knowledge atom"
                )


                knowledge_context = (
                    f"ID: {atom.atom_id}\n"
                    f"Title: {atom.title}\n"
                    f"Content: {atom.content}\n"
                    f"Tags: {atom.tags}"
                )


        trace.result = (
            f"Reasoning completed for task: {task}"
        )


        self.traces.append(
            trace
        )


        if knowledge_context:

            return (
                f"{trace.result}\n"
                f"Knowledge context:\n"
                f"{knowledge_context}"
            )


        return trace.result



    def get_history(self) -> List[str]:
        """
        Return reasoning history.
        """

        return self.history



    def get_traces(self) -> List[ReasoningTrace]:
        """
        Return reasoning traces.
        """

        return self.traces