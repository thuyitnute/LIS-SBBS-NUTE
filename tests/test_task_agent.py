"""
Test LIS Task Agent
"""

from app.agents.task_agent import TaskAgent


def test_task_agent():

    agent = TaskAgent(
        "LIS Task Agent"
    )

    result = agent.execute(
        "Analyze Knowledge Graph"
    )

    assert result == (
        "LIS Task Agent executed task: "
        "Analyze Knowledge Graph"
    )

    print(result)


if __name__ == "__main__":
    test_task_agent()