"""
example_usage.py -- Demonstrates CustomerChurnCohortClient
"""
from client import CustomerChurnCohortClient

def main():
    client = CustomerChurnCohortClient()
    result = client.calculate_cohort(
        cohort_registrations=1000,
        active_users_month1=800,
        active_users_month3=450
    )
    print("[Cohort Decay Result]")
    print(f"Month 1: {result['month1_retention_pct']}%")
    print(f"Month 3: {result['month3_retention_pct']}%")
    print(f"Stability: {result['decay_tier']}")

if __name__ == "__main__":
    main()
