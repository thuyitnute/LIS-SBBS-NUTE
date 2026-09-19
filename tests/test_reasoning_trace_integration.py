"""
Test Reasoning Trace Integration

Version:
LIS v1.0.0 - Cognitive Foundation
"""


from app.knowledge.atom import KnowledgeAtom
from app.knowledge.graph import KnowledgeGraph

from app.reasoning.reasoning_engine import ReasoningEngine



def test_reasoning_trace_integration():

    atom = KnowledgeAtom(
        atom_id="LIS-K001",
        title="Learning Intelligence Infrastructure",
        content="AI-Native University Platform"
    )


    graph = KnowledgeGraph()

    graph.add_atom(atom)


    engine = ReasoningEngine(
        graph
    )


    result = engine.analyze(
        "Analyze LIS Architecture",
        atom_id="LIS-K001"
    )


    traces = engine.get_traces()


    assert len(traces) == 1


    trace = traces[0]


    assert (
        trace.task
        ==
        "Analyze LIS Architecture"
    )


    assert (
        "LIS-K001"
        in trace.knowledge_used
    )


    assert (
        "Retrieve knowledge context"
        in trace.reasoning_steps
    )


    assert (
        "Analyze knowledge atom"
        in trace.reasoning_steps
    )


    print(trace.summary())



if __name__ == "__main__":
    test_reasoning_trace_integration()