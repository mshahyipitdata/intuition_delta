import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIRS = [
    ROOT / "data" / "public_seed_cases",
    ROOT / "data" / "real_world_cases",
]
OUTPUT = ROOT / "catalog" / "cases.csv"

FIELDS = [
    "case_id",
    "created_at",
    "domain",
    "source_name",
    "source_type",
    "is_public_seed",
    "evidence_status",
    "example_granularity",
    "severity",
    "reviewer_role",
    "failure_type",
    "tags",
    "source_url",
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def iter_case_files():
    for data_dir in DATA_DIRS:
        if data_dir.exists():
            yield from sorted(data_dir.glob("*.json"))


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for file_path in iter_case_files():
        record = load_json(file_path)
        row = {
            "case_id": record.get("case_id", ""),
            "created_at": record.get("created_at", ""),
            "domain": record.get("domain", ""),
            "source_name": record.get("source_name", ""),
            "source_type": record.get("source_type", ""),
            "is_public_seed": record.get("is_public_seed", ""),
            "evidence_status": record.get("evidence_status", ""),
            "example_granularity": record.get("example_granularity", ""),
            "severity": record.get("severity", ""),
            "reviewer_role": record.get("reviewer_role", ""),
            "failure_type": ";".join(record.get("failure_type", [])),
            "tags": ";".join(record.get("tags", [])),
            "source_url": record.get("source_url", ""),
        }
        rows.append(row)

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
