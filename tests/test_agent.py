import pytest
from src.agent.graph import build_graph
from src.audit.schemas import EvidenceBundle, ActionLog

def test_graph_execution():
    # Setup
    ticket = "TEST-101"
    initial_bundle = EvidenceBundle(ticket_id=ticket, agent_version="test-v1")
    initial_state = {
        "ticket_id": ticket,
        "goal": "Test Goal",
        "evidence": initial_bundle,
        "plan": None,
        "code": None,
        "execution_result": None
    }

    # Execution
    graph = build_graph()
    final_state = graph.invoke(initial_state)

    # Assertions
    assert final_state["execution_result"] is not None
    assert len(final_state["evidence"].replay_log) == 1
    
    log_entry = final_state["evidence"].replay_log[0]
    # Check if it is an instance of ActionLog or a dict
    # Pydantic V2 inside a list might coerce, but let's see what we actually get.
    # If it's a dict, we should fix the code to be strict.
    assert isinstance(log_entry, ActionLog), f"Expected ActionLog, got {type(log_entry)}"
    assert log_entry.step_id == 1
    assert log_entry.tool_name == "mock_exec"
