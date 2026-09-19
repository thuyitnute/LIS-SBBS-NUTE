"""
Test LIS Reasoning Trace

Version:
LIS v1.0.0 - Cognitive Foundation
"""


from app.reasoning.trace import ReasoningTrace



def test_reasoning_trace():

    trace = ReasoningTrace(
        task="Analyze LIS Architecture",
        knowledge_used=[
            "LIS-K001"
        ]
    )


    trace.add_step(
        "Retrieve knowledge context"
    )


    trace.add_step(
        "Analyze architecture relationship"
    )


    trace.result = (
        "Architecture analysis completed"
    )


    summary = trace.summary()


    assert (
        "Analyze LIS Architecture"
        in summary
    )


    assert (
        "LIS-K001"
        in summary
    )


    assert (
        "Retrieve knowledge context"
        in summary
    )


    assert (
        "Architecture analysis completed"
        in summary
    )


    print(summary)



if __name__ == "__main__":
    test_reasoning_trace()