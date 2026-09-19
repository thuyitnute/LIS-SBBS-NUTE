"""
LIS Task Agent

A basic agent implementation
for executing tasks in LIS.
"""

from app.agents.base_agent import BaseAgent


class TaskAgent(BaseAgent):
    """
    Basic task execution agent.
    """

    def __init__(self, name: str):
        super().__init__(name)


    def execute(self, task: str) -> str:
        """
        Execute a task and return result.
        """

        return (
            f"{self.name} executed task: {task}"
        )