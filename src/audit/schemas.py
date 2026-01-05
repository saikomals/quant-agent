from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid

# --- 1. The Replay Log (Machine Readable) ---
class ActionLog(BaseModel):
    step_id: int
    tool_name: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    input_hash: str     # SHA256 of the input provided to the tool
    output_hash: str    # SHA256 of the output received from the tool
    data_snapshot_id: Optional[str] = None # If external data was fetched

# --- 2. The Decision Record (Human Readable) ---
class DecisionRecord(BaseModel):
    summary: str        # "I analyzed BTC momentum..."
    logic_chain: str    # "I chose 30-day window because..."
    citations: List[str]# ["Reference data_snapshot_88", "Reference code_commit_a1b2"]
    
# --- 3. The "Kill Shot" Evidence Bundle ---
class EvidenceBundle(BaseModel):
    run_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    ticket_id: str
    agent_version: str  # Git SHA of THIS repo
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    # The immutable history
    replay_log: List[ActionLog] = []
    
    # The compliance artifacts
    decision_record: Optional[DecisionRecord] = None
    
    # Validation Gates
    validation_results: Dict[str, bool] = {
        "lookahead_bias_passed": False,
        "data_leakage_passed": False
    }

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}