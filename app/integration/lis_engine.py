"""
LIS Engine

Integration layer that coordinates:

- Trust
- Knowledge
- Reasoning
- Agent
"""


from app.agents.task_agent import TaskAgent

from app.trust.identity import Identity
from app.trust.permission import Permission

from app.knowledge.graph import KnowledgeGraph

from app.reasoning.reasoning_engine import ReasoningEngine



class LISEngine:
    """
    Main orchestration engine of LIS.
    """


    def __init__(
        self,
        agent: TaskAgent,
        identity: Identity,
        permission: Permission,
        knowledge_graph: KnowledgeGraph
    ):

        self.agent = agent

        self.identity = identity

        self.permission = permission

        self.knowledge_graph = knowledge_graph


        self.reasoning = ReasoningEngine(
            knowledge_graph
        )


    def execute(
        self,
        task: str,
        atom_id: str = ""
    ) -> str:
        """
        Execute LIS workflow.

        Flow:

        Identity
            ↓
        Permission
            ↓
        Knowledge Reasoning
            ↓
        Agent Execution
        """


        if not self.permission.permissions:

            return "Permission denied"



        reasoning_result = self.reasoning.analyze(
            task,
            atom_id
        )


        agent_result = self.agent.execute(
            task
        )


        return (
            f"{reasoning_result}\n"
            f"{agent_result}"
        )