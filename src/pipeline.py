from src.agents.behavior_agent import behavior_agent
from src.agents.sentiment_agent import sentiment_agent
from src.agents.root_cause_agent import root_cause_agent
from src.agents.recommendation_agent import recommendation_agent


def run_pipeline(customer_id, use_case, events, sentiment, baseline, is_high_value):
    behavior = behavior_agent(customer_id, events, baseline)
    sentiment_out = sentiment_agent(customer_id, sentiment)
    root = root_cause_agent(behavior, sentiment_out, use_case)

    recommendation = recommendation_agent(
        use_case=use_case,
        behavior=behavior,
        sentiment=sentiment_out,
        is_high_value=is_high_value
    )

    return {
        "behavior": behavior,
        "sentiment": sentiment_out,
        "root_cause": root,
        "recommendation": recommendation
    }
