# genpark-customer-churn-cohort-skill

> **GenPark AI Agent Skill** -- Cohort customer churn and retention compiler.

## Quick Start

```python
from client import CustomerChurnCohortClient
client = CustomerChurnCohortClient()
res = client.calculate_cohort(100, 90, 70)
print(res["decay_tier"])
```
