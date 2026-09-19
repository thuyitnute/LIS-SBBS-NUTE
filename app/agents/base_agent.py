"""
LIS Base Agent

Defines the fundamental structure
for all AI Agents in LIS.
"""


from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Abstract base class for LIS Agents.
    """

    def __init__(self, name: str):
        self.name = name


    def describe(self) -> str:
        """
        Return agent description.
        """

        return f"LIS Agent: {self.name}"


    @abstractmethod
    def execute(self, task: str):
        """
        Execute an assigned task.
        """

        pass