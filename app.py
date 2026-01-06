from data_loader import load_use_case_data
from baseline import compute_baseline
from pipeline import run_pipeline

USE_CASE = "supermarket"   # or "fuel"
CUSTOMER_ID = "C001"

customers, events, campaigns, sentiment = load_use_case_data(USE_CASE)
baseline = compute_baseline(events)

is_high_value = customers.loc[
    customers["customer_id"] == CUSTOMER_ID, "is_high_value"
].iloc[0]

result = run_pipeline(
    CUSTOMER_ID,
    USE_CASE,
    events,
    sentiment,
    baseline,
    is_high_value
)

print("\n=== AGENTIC LOYALTY OUTPUT ===")
for k, v in result.items():
    print(f"\n{k.upper()}:\n{v}")
