#!/usr/bin/env python3
"""Inventory ABC-XYZ and reorder-point analysis for a CSV file.

Expected columns:
sku, product, unit_cost, on_hand, lead_time_days, safety_stock,
m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11, m12

Usage:
    python scripts/analytics.py inventory.csv --output inventory_analysis.csv

This is an analytical aid, not a substitute for approved replenishment policy.
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import pandas as pd

MONTHS = [f"m{i:02d}" for i in range(1, 13)]
REQUIRED = ["sku", "product", "unit_cost", "on_hand", "lead_time_days", "safety_stock", *MONTHS]


def analyse(source: Path) -> pd.DataFrame:
    df = pd.read_csv(source)
    missing = [column for column in REQUIRED if column not in df.columns]
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))

    numeric = ["unit_cost", "on_hand", "lead_time_days", "safety_stock", *MONTHS]
    for column in numeric:
        df[column] = pd.to_numeric(df[column], errors="raise")
    if (df[["unit_cost", *MONTHS]] < 0).any().any():
        raise ValueError("Unit cost and monthly demand must be non-negative.")
    if (df[["lead_time_days", "safety_stock"]] < 0).any().any():
        raise ValueError("Lead time and safety stock must be non-negative.")

    df["annual_demand"] = df[MONTHS].sum(axis=1)
    df["annual_usage_value"] = df["annual_demand"] * df["unit_cost"]
    total_value = df["annual_usage_value"].sum()
    df = df.sort_values("annual_usage_value", ascending=False).reset_index(drop=True)
    df["value_share"] = (df["annual_usage_value"] / total_value) if total_value else 0.0
    df["cumulative_value_share"] = df["value_share"].cumsum()

    prior_cumulative = df["cumulative_value_share"] - df["value_share"]
    df["abc_class"] = "C"
    df.loc[prior_cumulative < 0.95, "abc_class"] = "B"
    df.loc[prior_cumulative < 0.80, "abc_class"] = "A"

    means = df[MONTHS].mean(axis=1)
    stds = df[MONTHS].std(axis=1, ddof=0)
    df["demand_cv"] = (stds / means.where(means != 0)).fillna(0.0)
    df["xyz_class"] = "Z"
    df.loc[df["demand_cv"] <= 1.0, "xyz_class"] = "Y"
    df.loc[df["demand_cv"] <= 0.5, "xyz_class"] = "X"
    df["abc_xyz_segment"] = df["abc_class"] + df["xyz_class"]

    df["avg_daily_demand"] = df["annual_demand"] / 365.0
    df["reorder_point"] = (df["avg_daily_demand"] * df["lead_time_days"] + df["safety_stock"]).apply(math.ceil)
    df["replenishment_review"] = df["on_hand"] <= df["reorder_point"]
    df["review_action"] = df.apply(
        lambda row: "Review replenishment" if row["replenishment_review"]
        else ("Review variable demand" if row["xyz_class"] == "Z"
              else ("Monitor high-value item" if row["abc_class"] == "A" else "Routine review")),
        axis=1,
    )
    return df


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path, help="CSV containing monthly item demand")
    parser.add_argument("--output", type=Path, default=Path("inventory_analysis.csv"), help="Output CSV path")
    args = parser.parse_args()
    try:
        result = analyse(args.input_csv)
        result.to_csv(args.output, index=False)
        cols = ["sku", "product", "abc_xyz_segment", "demand_cv", "on_hand", "reorder_point", "review_action"]
        print(result[cols].to_string(index=False))
        print(f"\nSaved {len(result)} analysed rows to {args.output}")
        return 0
    except (OSError, ValueError, pd.errors.ParserError) as exc:
        print(f"Analysis failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
