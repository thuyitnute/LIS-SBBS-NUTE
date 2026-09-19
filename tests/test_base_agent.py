"""
Test LIS Base Agent
"""

from app.agents.base_agent import BaseAgent


class SimpleAgent(BaseAgent):
    """
    Simple implementation for testing.
    """

    def execute(self, task: str):
        return f"Executing: {task}"


def test_base_agent():

    agent = SimpleAgent(
        "LIS Test Agent"
    )

    assert agent.name == "LIS Test Agent"

    assert agent.describe() == (
        "LIS Agent: LIS Test Agent"
    )

    result = agent.execute(
        "Understand LIS Knowledge"
    )

    assert result == (
        "Executing: Understand LIS Knowledge"
    )

    print(result)


if __name__ == "__main__":
    test_base_agent()