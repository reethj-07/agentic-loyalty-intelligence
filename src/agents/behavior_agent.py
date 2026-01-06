from src.schemas import BehaviorInsight

def behavior_agent(customer_id, events, baseline):
    cust_events = events[events["customer_id"] == customer_id]

    current_spend = cust_events["spend_amount"].sum()
    baseline_row = baseline[baseline["customer_id"] == customer_id]

    if baseline_row.empty:
        return BehaviorInsight(
            spend_change_pct=0,
            frequency_change_pct=0,
            redemption_change_pct=0,
            loyalty_health="unknown"
        )

    avg_spend = baseline_row["avg_spend"].iloc[0]

    spend_change = ((current_spend - avg_spend) / avg_spend) * 100

    health = "declining" if spend_change < -20 else "stable"

    return BehaviorInsight(
        spend_change_pct=round(spend_change, 2),
        frequency_change_pct=-15.0,   # simplified for POC
        redemption_change_pct=-25.0,
        loyalty_health=health
    )
