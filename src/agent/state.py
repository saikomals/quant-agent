from typing import TypedDict, List, Optional
from src.audit.schemas import EvidenceBundle

class AgentState(TypedDict):
    """
    The working memory of the agent.
    Passed between every node in the graph.
    """
    ticket_id: str
    goal: str
    plan: Optional[str]            # The agent's plan of attack
    code: Optional[str]            # The Python code it generated
    execution_result: Optional[str] # Output from the code run
    evidence: EvidenceBundle       # The official audit log