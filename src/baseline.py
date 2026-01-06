import pandas as pd

def compute_baseline(events: pd.DataFrame, window_days=90):
    events["event_date"] = pd.to_datetime(events["event_date"])

    baseline = (
        events[events["event_type"] == "transaction"]
        .groupby("customer_id")
        .agg(
            avg_spend=("spend_amount", "mean"),
            txn_count=("event_id", "count")
        )
        .reset_index()
    )

    return baseline
