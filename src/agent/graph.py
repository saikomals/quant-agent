from langgraph.graph import StateGraph, END
from src.agent.state import AgentState
from src.audit.schemas import ActionLog

# --- NODE 1: PLAN ---
def plan_node(state: AgentState):
    print("🧠 [Brain] Thinking about the goal...")
    # (Later, this is where GPT-4o writes the plan)
    return {"plan": "1. Fetch Data\n2. Calculate Mean\n3. Plot"}

# --- NODE 2: EXECUTE ---
def execute_node(state: AgentState):
    print("🛠️ [Hands] Executing code...")
    # (Later, this is where Docker runs the code)
    return {"execution_result": "Success: BTC Price is $98k", "code": "print('BTC')"}

# --- NODE 3: AUDIT ---
def audit_node(state: AgentState):
    print("⚖️ [Lawyer] Logging action to Evidence Bundle...")
    # We pretend to log the action here
    log_entry = ActionLog(
        step_id=1,
        tool_name="mock_exec",
        input_hash="abc",
        output_hash="xyz"
    )
    state["evidence"].replay_log.append(log_entry)
    return {"evidence": state["evidence"]}

# --- GRAPH WIRING ---
def build_graph():
    workflow = StateGraph(AgentState)

    # 1. Add Nodes
    workflow.add_node("planner", plan_node)
    workflow.add_node("executor", execute_node)
    workflow.add_node("auditor", audit_node)

    # 2. Add Edges (The Logic Flow)
    # Start -> Plan -> Execute -> Audit -> End
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "executor")
    workflow.add_edge("executor", "auditor")
    workflow.add_edge("auditor", END)

    # 3. Compile
    return workflow.compile()
