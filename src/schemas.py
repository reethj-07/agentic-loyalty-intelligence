from pydantic import BaseModel
from typing import List, Optional

class BehaviorInsight(BaseModel):
    spend_change_pct: float
    frequency_change_pct: float
    redemption_change_pct: float
    loyalty_health: str

class SentimentInsight(BaseModel):
    sentiment: str
    friction_type: Optional[str]
    confidence: float

class RootCauseInsight(BaseModel):
    primary_cause: str
    contributing_factors: List[str]
    evidence: List[str]

class CampaignRecommendation(BaseModel):
    campaign_type: str
    reward: str
    message_angle: str
    escalation_required: bool

class Recommendation(BaseModel):
    campaign_type: str
    reward: str
    message_angle: str
    escalation_required: bool
