from src.schemas import SentimentInsight

def sentiment_agent(customer_id, sentiment_df):
    records = sentiment_df[sentiment_df["customer_id"] == customer_id]

    if records.empty:
        return SentimentInsight(
            sentiment="neutral",
            friction_type=None,
            confidence=0.3
        )

    row = records.iloc[-1]

    return SentimentInsight(
        sentiment=row["sentiment_label"],
        friction_type=row["friction_type"],
        confidence=0.8
    )
