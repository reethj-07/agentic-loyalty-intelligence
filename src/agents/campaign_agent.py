from src.schemas import CampaignRecommendation

def campaign_agent(root_cause, is_high_value):
    if "price" in root_cause.primary_cause.lower():
        return CampaignRecommendation(
            campaign_type="cashback",
            reward="5% immediate cashback",
            message_angle="value",
            escalation_required=is_high_value
        )

    return CampaignRecommendation(
        campaign_type="recognition",
        reward="bonus loyalty points",
        message_angle="appreciation",
        escalation_required=False
    )
