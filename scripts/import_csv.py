import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV = ROOT / "catalog" / "incoming_cases.csv"
OUTPUT_DIR = ROOT / "data" / "real_world_cases"


def parse_list(value: str):
    if not value:
        return []
    return [x.strip() for x in value.split(";") if x.strip()]


def to_bool(value: str):
    return str(value).strip().lower() in {"true", "1", "yes"}


def to_float_or_null(value: str):
    value = str(value).strip()
    if not value:
        return None
    return float(value)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with INPUT_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            case_id = row["case_id"].strip()
            record = {
                "case_id": case_id,
                "created_at": row["created_at"].strip(),
                "domain": row["domain"].strip(),
                "input_context": row["input_context"].strip(),
                "ai_output": row["ai_output"].strip(),
                "ai_confidence": to_float_or_null(row.get("ai_confidence", "")),
                "ai_reasoning_summary": row.get("ai_reasoning_summary", "").strip() or None,
                "human_override": row["human_override"].strip(),
                "human_rationale": row["human_rationale"].strip(),
                "failure_type": parse_list(row.get("failure_type", "")),
                "severity": row["severity"].strip(),
                "final_outcome": row["final_outcome"].strip(),
                "reviewer_role": row["reviewer_role"].strip(),
                "tags": parse_list(row.get("tags", "")),
                "source_name": row["source_name"].strip(),
                "source_url": row["source_url"].strip(),
                "source_type": row["source_type"].strip(),
                "is_public_seed": to_bool(row.get("is_public_seed", "false")),
                "evidence_status": row["evidence_status"].strip(),
                "example_granularity": row["example_granularity"].strip(),
                "license_note": row.get("license_note", "").strip() or None,
                "notes": row.get("notes", "").strip() or None,
            }

            out_path = OUTPUT_DIR / f"{case_id}.json"
            with out_path.open("w", encoding="utf-8") as out:
                json.dump(record, out, indent=2, ensure_ascii=False)
                out.write("\n")

            count += 1

    print(f"Imported {count} cases into {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
