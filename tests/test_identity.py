"""
Test LIS Identity Model
"""

from app.trust.identity import Identity


def test_identity():

    identity = Identity(
        identity_id="AGENT-001",
        name="LIS Research Agent",
        entity_type="AI_AGENT"
    )


    assert identity.identity_id == "AGENT-001"

    assert identity.describe() == (
        "AI_AGENT: LIS Research Agent "
        "(AGENT-001)"
    )


    print(identity.describe())


if __name__ == "__main__":
    test_identity()