from src.schemas import Recommendation


def recommendation_agent(use_case, behavior, sentiment, is_high_value):
    """
    Decide the best loyalty action based on behavior + sentiment
    """

    # Default recommendation
    campaign_type = "recognition"
    reward = "bonus loyalty points"
    message_angle = "appreciation"
    escalation_required = False

    # Logic based on behavior
    if behavior.redemption_change_pct < -20:
        campaign_type = "reactivation"
        reward = "limited-time redemption boost"
        message_angle = "urgency"

    if behavior.frequency_change_pct < -10:
        campaign_type = "engagement"
        reward = "visit-based incentive"
        message_angle = "habit-building"

    # Sentiment override
    if sentiment.sentiment == "negative":
        escalation_required = True
        message_angle = "reassurance"

    # High value customer override
    if is_high_value:
        reward = "premium bonus + concierge offer"

    return Recommendation(
        campaign_type=campaign_type,
        reward=reward,
        message_angle=message_angle,
        escalation_required=escalation_required
    )
