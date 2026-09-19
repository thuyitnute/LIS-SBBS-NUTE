"""
Test LIS Permission Model
"""

from app.trust.permission import Permission


def test_permission():

    permission = Permission(
        identity_id="AGENT-001"
    )


    permission.add_permission(
        "READ_KNOWLEDGE"
    )

    permission.add_permission(
        "CREATE_REPORT"
    )


    assert permission.has_permission(
        "READ_KNOWLEDGE"
    )


    assert not permission.has_permission(
        "DELETE_SYSTEM"
    )


    print(
        permission.permissions
    )


if __name__ == "__main__":
    test_permission()