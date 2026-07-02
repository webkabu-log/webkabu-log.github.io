"""Paper-lab CSV validator and return calculator (standard library only)."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def as_float(row: dict[str, str], key: str) -> float:
    value = row.get(key, "").strip()
    if not value:
        raise ValueError(f"week {row.get('week')}, {row.get('method')}/{row.get('symbol')}: {key} is empty")
    return float(value)


def main() -> int:
    protocol = json.loads((ROOT / "protocol.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((ROOT / "predictions.csv").open(encoding="utf-8-sig", newline="")))
    settled = [row for row in rows if row.get("status", "").strip() == "settled"]
    if not settled:
        print("No settled rows yet. Add predictions first; do not invent prices.")
        return 0

    allowed_methods = set(protocol["methods"])
    seen: set[tuple[str, str, str]] = set()
    weekly: dict[tuple[str, str], list[tuple[float, float]]] = defaultdict(list)
    evidence = defaultdict(lambda: {"pass": 0, "fail": 0, "pending": 0})

    for row in settled:
        method = row.get("method", "").strip()
        direction = row.get("direction", "").strip()
        key = (row.get("week", "").strip(), method, row.get("symbol", "").strip())
        if method not in allowed_methods:
            raise ValueError(f"unknown method: {method}")
        if direction not in {"up", "cash"}:
            raise ValueError(f"unknown direction: {direction}")
        if key in seen:
            raise ValueError(f"duplicate settled row: {key}")
        seen.add(key)
        weight = as_float(row, "weight")
        if direction == "cash":
            gross = 0.0
            cost = 0.0
        else:
            entry = as_float(row, "entry_price")
            exit_price = as_float(row, "exit_price")
            gross = exit_price / entry - 1
            cost = float(protocol["round_trip_cost_rate"])
        weekly[(key[0], method)].append((weight, gross - cost))
        check = row.get("evidence_check", "pending").strip() or "pending"
        if check not in evidence[method]:
            raise ValueError(f"unknown evidence_check: {check}")
        evidence[method][check] += 1

    cumulative = defaultdict(lambda: 1.0)
    print("week,method,net_return")
    for (week, method), values in sorted(weekly.items()):
        total_weight = sum(weight for weight, _ in values)
        if abs(total_weight - 1.0) > 0.001:
            raise ValueError(f"week {week}, {method}: weights total {total_weight:.4f}, expected 1.0")
        net_return = sum(weight * result for weight, result in values)
        cumulative[method] *= 1 + net_return
        print(f"{week},{method},{net_return:.4%}")

    print("\nmethod,cumulative_return,evidence_failures")
    for method in sorted(cumulative):
        print(f"{method},{cumulative[method] - 1:.4%},{evidence[method]['fail']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
