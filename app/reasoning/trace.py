"""
LIS Reasoning Trace

Stores the reasoning process
for transparency and analysis.
"""


from dataclasses import dataclass, field
from typing import List



@dataclass
class ReasoningTrace:
    """
    Represents a reasoning execution trace.
    """


    task: str

    knowledge_used: List[str] = field(
        default_factory=list
    )

    reasoning_steps: List[str] = field(
        default_factory=list
    )

    result: str = ""


    def add_step(
        self,
        step: str
    ):
        """
        Add a reasoning step.
        """

        self.reasoning_steps.append(
            step
        )


    def summary(self) -> str:
        """
        Return trace summary.
        """

        return (
            f"Task: {self.task}\n"
            f"Knowledge: {self.knowledge_used}\n"
            f"Steps: {self.reasoning_steps}\n"
            f"Result: {self.result}"
        )