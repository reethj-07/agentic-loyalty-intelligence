from groq import Groq
from src.config import GROQ_API_KEY, GROQ_MODEL
from src.schemas import RootCauseInsight

client = Groq(api_key=GROQ_API_KEY)

def root_cause_agent(behavior, sentiment, use_case):
    prompt = f"""
You are a loyalty intelligence analyst.

Use case: {use_case}

Behavior insight:
{behavior}

Sentiment insight:
{sentiment}

Explain clearly:
1. Primary reason the customer disengaged
2. 2 contributing factors
3. Evidence from the data

Be business-friendly. No technical jargon.
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    text = response.choices[0].message.content.strip()
    lines = [l for l in text.split("\n") if l.strip()]

    return RootCauseInsight(
        primary_cause=lines[0],
        contributing_factors=lines[1:3],
        evidence=lines[3:6]
    )
