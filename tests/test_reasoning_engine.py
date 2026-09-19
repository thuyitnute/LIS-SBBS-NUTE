"""
Test LIS Reasoning Engine
"""


from app.reasoning.reasoning_engine import ReasoningEngine



def test_reasoning_engine():

    engine = ReasoningEngine()


    result = engine.analyze(
        "Analyze Knowledge Graph"
    )


    assert result == (
        "Reasoning completed for task: "
        "Analyze Knowledge Graph"
    )


    history = engine.get_history()


    assert (
        "Analyze Knowledge Graph"
        in history
    )


    print(result)



if __name__ == "__main__":
    test_reasoning_engine()