from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class RemoteMode(BaseModel):
    mode: Literal["fully_remote", "hybrid", "occasional"]
    remote_percentage: int = Field(..., ge=0, le=100)
    allow_byod: bool

class OrgProfile(BaseModel):
    org_name: str
    industry: str
    employees_count: int
    has_pdn: bool
    has_critical_infrastructure: bool
    remote_mode: RemoteMode
    # Optional fields for more detailed analysis
    it_systems: List[str] = Field(default_factory=list)

class RiskItem(BaseModel):
    risk_description: str
    probability: Literal["low", "medium", "high"]
    impact: Literal["low", "medium", "high"]
    recommendation: str
    priority: Literal["low", "medium", "high", "critical"]

class PolicyDraft(BaseModel):
    title: str
    sections: List[str]
    risks: List[RiskItem]
