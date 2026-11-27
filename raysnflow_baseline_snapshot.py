"""
Raysnflow / Citadel — Baseline Snapshot
Generated: 27 November 2026
Covers last ~2 days of technical discussion.
Cars game omitted.
"""

from datetime import date
from typing import List, Dict, Any

FREEZE_DATE = date(2026, 11, 27)

# ---------------------------------------------------------------------------
# Ranking Freeze Frame
# ---------------------------------------------------------------------------
RANKING_FREEZE = {
    "locked_date": FREEZE_DATE.isoformat(),
    "corridor": "Panama City harbor → Calhoun County via Hwy 20/231 + old-rail alignment",
    "rules": {
        "spacing_miles": (8, 10),
        "node_filter": "6-out-of-10",
        "design_class": "low-maintenance / traffic-signal reliability",
        "surface_disturbance": "existing ROW only",
        "landowner_package": "optional power/data access only",
    },
    "ranking_factors_ordered": [
        "existing_rail_bed_or_elevated_dot_pad",
        "oxidation_salinity_exposure",
        "solar_access_above_flood_line",
        "distance_compliance_8_to_10_mile",
        "minimal_new_clearing",
    ],
    "prototype_node_count_range": (6, 9),
    "candidate_segments": [
        {"rank": 1, "segment": "Harbor / port edge to first inland rail", "reason": "Highest solar + existing industrial pad"},
        {"rank": 2, "segment": "8–10 mi inland on old rail", "reason": "Rail-bed elevation, lower flood"},
        {"rank": 3, "segment": "Next 8–10 mi interval", "reason": "Continues rail alignment"},
        {"rank": 4, "segment": "Hwy 20 / 231 junction zone", "reason": "Existing DOT infrastructure"},
        {"rank": 5, "segment": "Mid-corridor rail segment", "reason": "Stable elevation"},
        {"rank": 6, "segment": "Approaching Calhoun County line", "reason": "Lower salinity expected"},
    ],
}

# ---------------------------------------------------------------------------
# Delta-Relevant Variable Log — Baseline
# ---------------------------------------------------------------------------
VARIABLE_BASELINE: List[Dict[str, Any]] = [
    {"variable": "node_spacing_rule", "baseline": (8, 10), "unit": "miles", "delta_trigger": "Any proposed change"},
    {"variable": "node_filter", "baseline": "6-out-of-10", "unit": "ratio", "delta_trigger": "Any relaxation or tightening"},
    {"variable": "prototype_node_count", "baseline": (6, 9), "unit": "count", "delta_trigger": "Addition or removal"},
    {"variable": "ranking_weight_1", "baseline": "rail-bed / elevated pad", "unit": "category", "delta_trigger": "Re-weight"},
    {"variable": "ranking_weight_2", "baseline": "oxidation / salinity exposure", "unit": "category", "delta_trigger": "Re-weight"},
    {"variable": "ox_state_Ag", "baseline": 0, "unit": "integer", "delta_trigger": "Shift to +1"},
    {"variable": "ox_state_Cu", "baseline": 2, "unit": "integer", "delta_trigger": "Any change"},
    {"variable": "ox_state_Fe", "baseline": "2/3", "unit": "integer", "delta_trigger": "Measured shift"},
    {"variable": "redox_potential", "baseline": None, "unit": "mV", "delta_trigger": "First reading"},
    {"variable": "lithology_classes", "baseline": "pending_first_well", "unit": "categorical", "delta_trigger": "Lab package arrival"},
    {"variable": "flood_marsh_risk", "baseline": "qualitative_high_near_coast", "unit": "ordinal", "delta_trigger": "Quantitative update"},
    {"variable": "solar_access", "baseline": "above_flood_line", "unit": "binary", "delta_trigger": "Site-specific exception"},
    {"variable": "surface_disturbance", "baseline": "existing_ROW_only", "unit": "constraint", "delta_trigger": "Any new clearing"},
    {"variable": "data_status", "baseline": "pre-first-well", "unit": "flag", "delta_trigger": "Package received"},
]

# ---------------------------------------------------------------------------
# Machine-Learning Setup Skeleton (from exploration)
# ---------------------------------------------------------------------------
ML_TARGETS = {
    "lithology_prediction": {
        "inputs": ["gamma", "resistivity", "density", "neutron"],
        "target": "lithology_class_from_core_cuttings",
        "status": "waiting_on_first_well_package",
    },
    "oxidation_forecast": {
        "inputs": ["time_series_resistance", "color_change", "humidity", "salinity"],
        "target": "days_to_measurable_ox_shift",
        "status": "bench_coupons_ready",
    },
    "node_ranking": {
        "inputs": ["flood_risk", "rail_elevation", "expected_oxidation", "solar_access"],
        "target": "ranked_score_against_freeze_frame",
        "status": "baseline_locked",
    },
    "anomaly_detection": {
        "inputs": ["redox", "temperature", "conductivity"],
        "target": "out_of_envelope_flag",
        "status": "post_instrumentation",
    },
}

def log_delta(variable: str, new_value: Any, reason: str, source: str = "") -> Dict:
    """Record a delta against the baseline. Returns the log entry."""
    baseline_entry = next((v for v in VARIABLE_BASELINE if v["variable"] == variable), None)
    if not baseline_entry:
        raise ValueError(f"Unknown variable: {variable}")
    return {
        "date": date.today().isoformat(),
        "variable": variable,
        "baseline": baseline_entry["baseline"],
        "new_value": new_value,
        "delta": "see_comparison",
        "reason": reason,
        "source": source,
    }

if __name__ == "__main__":
    print("=== RANKING FREEZE FRAME ===")
    print(RANKING_FREEZE)
    print("\n=== VARIABLE BASELINE COUNT ===")
    print(len(VARIABLE_BASELINE), "variables locked")
    print("\n=== ML TARGETS ===")
    for name, spec in ML_TARGETS.items():
        print(f"{name}: {spec['status']}")
