"""Validate and summarize the AI Investment Research weekly ledger."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def number(row: dict[str, str], key: str) -> float:
    value = row.get(key, "").strip()
    if not value:
        raise ValueError(f"{row.get('portfolio')}/{row.get('data_ticker')}: {key} is empty")
    return float(value)


def validate_selections(rows: list[dict[str, str]], protocol: dict) -> None:
    if not rows:
        return
    allowed = set(protocol["portfolios"])
    seen: set[tuple[str, str]] = set()
    weights = defaultdict(float)
    counts = defaultdict(int)
    for row in rows:
        portfolio = row.get("portfolio", "").strip()
        ticker = row.get("data_ticker", "").strip()
        if portfolio not in allowed:
            raise ValueError(f"unknown portfolio: {portfolio}")
        if not ticker:
            raise ValueError(f"{portfolio}: data_ticker is empty")
        key = (portfolio, ticker)
        if key in seen:
            raise ValueError(f"duplicate selection: {key}")
        seen.add(key)
        counts[portfolio] += 1
        weights[portfolio] += number(row, "weight")
        if row.get("eligibility_status", "").strip() not in {"pass", "pending"}:
            raise ValueError(f"invalid eligibility_status: {key}")
    for portfolio in allowed:
        expected = protocol["positions"][portfolio]
        if counts[portfolio] != expected:
            raise ValueError(f"{portfolio}: {counts[portfolio]} selections, expected {expected}")
        if abs(weights[portfolio] - 1.0) > 0.001:
            raise ValueError(f"{portfolio}: weights total {weights[portfolio]:.4f}, expected 1.0")


def summarize(rows: list[dict[str, str]], protocol: dict) -> None:
    if not rows:
        print("No valuation rows yet. The study is still preparing; do not invent results.")
        return
    weekly = defaultdict(float)
    coverage = defaultdict(int)
    for row in rows:
        if row.get("data_status", "").strip() != "ok":
            raise ValueError(f"unverified valuation: {row.get('portfolio')}/{row.get('data_ticker')}")
        key = (int(row["week"]), row["portfolio"])
        weekly[key] += number(row, "value_jpy")
        coverage[key] += 1
    capital = float(protocol["virtual_capital_jpy_per_portfolio"])
    print("week,portfolio,value_jpy,return_pct,coverage")
    for (week, portfolio), value in sorted(weekly.items()):
        print(f"{week},{portfolio},{value:.0f},{value / capital - 1:.4%},{coverage[(week, portfolio)]}")


def main() -> int:
    protocol = json.loads((ROOT / "protocol.json").read_text(encoding="utf-8"))
    selections = read_csv("predictions.csv")
    if selections:
        validate_selections(selections, protocol)
        print(f"Validated {len(selections)} selections.")
    else:
        print("No selections yet. Run each fixed prompt once after the information cutoff is set.")
    summarize(read_csv("valuations.csv"), protocol)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
