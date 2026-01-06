import pandas as pd

def load_use_case_data(use_case: str):
    base = f"data/{use_case}"

    customers = pd.read_csv(f"{base}/customers.csv")
    events = pd.read_csv(f"{base}/loyalty_events.csv")
    campaigns = pd.read_csv(f"{base}/campaign_interactions.csv")
    sentiment = pd.read_csv(f"{base}/sentiment_feedback.csv")

    return customers, events, campaigns, sentiment
