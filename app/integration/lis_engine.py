"""
LIS Engine

Integration layer that coordinates
Trust, Reasoning and Agent components.
"""


from app.agents.task_agent import TaskAgent
from app.trust.identity import Identity
from app.trust.permission import Permission
from app.reasoning.reasoning_engine import ReasoningEngine


class LISEngine:
    """
    Main orchestration engine of LIS.
    """


    def __init__(
        self,
        agent: TaskAgent,
        identity: Identity,
        permission: Permission
    ):

        self.agent = agent
        self.identity = identity
        self.permission = permission

        self.reasoning = ReasoningEngine()


    def execute(
        self,
        task: str
    ) -> str:
        """
        Execute LIS workflow.

        Flow:

        Identity
            ↓
        Permission
            ↓
        Reasoning
            ↓
        Agent
        """


        if not self.permission.permissions:
            return "Permission denied"


        reasoning_result = self.reasoning.analyze(
            task
        )


        agent_result = self.agent.execute(
            task
        )


        return (
            f"{reasoning_result}\n"
            f"{agent_result}"
        )