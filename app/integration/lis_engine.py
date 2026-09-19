"""
LIS Engine

Integration layer that coordinates
Knowledge, Agent and Trust components.
"""


from app.agents.task_agent import TaskAgent
from app.trust.identity import Identity
from app.trust.permission import Permission


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


    def execute(
        self,
        task: str
    ) -> str:
        """
        Execute a task through LIS workflow.

        Workflow:

        Identity
            ↓
        Permission Check
            ↓
        Agent Execution
        """


        if not self.permission.permissions:
            return "Permission denied"


        return self.agent.execute(task)