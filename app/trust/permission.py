"""
LIS Permission Model

Defines permission management
for LIS entities.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Permission:
    """
    Represents permissions assigned
    to an LIS identity.
    """

    identity_id: str
    permissions: List[str] = field(
        default_factory=list
    )


    def add_permission(
        self,
        permission: str
    ):
        """
        Add a permission.
        """

        if permission not in self.permissions:
            self.permissions.append(permission)


    def has_permission(
        self,
        permission: str
    ) -> bool:
        """
        Check whether permission exists.
        """

        return permission in self.permissions