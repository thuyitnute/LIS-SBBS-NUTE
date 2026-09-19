"""
LIS Identity Model

Defines identity information
for users, agents and system entities.
"""

from dataclasses import dataclass


@dataclass
class Identity:
    """
    Represents an identity entity in LIS Trust Layer.
    """

    identity_id: str
    name: str
    entity_type: str


    def describe(self) -> str:
        """
        Return identity description.
        """

        return (
            f"{self.entity_type}: "
            f"{self.name} "
            f"({self.identity_id})"
        )