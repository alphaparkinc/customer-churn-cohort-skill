"""
customer-churn-cohort-skill: Client SDK
Calculates retention rate drops per monthly cohorts to detect early customer dropouts.
"""
from __future__ import annotations
from typing import Optional


class CustomerChurnCohortClient:
    """
    SDK for cohort analytics tracking.
    """

    def calculate_cohort(
        self,
        cohort_registrations: int,
        active_users_month1: int,
        active_users_month3: int,
    ) -> dict:
        total = max(1.0, float(cohort_registrations))
        
        m1_ret = round((active_users_month1 / total) * 100, 1)
        m3_ret = round((active_users_month3 / total) * 100, 1)

        # Evaluate cohort decay tier
        if m3_ret >= 60.0:
            tier = "stable"
        elif m3_ret >= 30.0:
            tier = "decaying"
        else:
            tier = "high-risk"

        return {
            "month1_retention_pct": m1_ret,
            "month3_retention_pct": m3_ret,
            "decay_tier": tier
        }
