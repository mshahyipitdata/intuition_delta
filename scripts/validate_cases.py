import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("Missing dependency: jsonschema")
    print("Install with: pip install jsonschema")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "case.schema.json"
DATA_DIRS = [
    ROOT / "data" / "public_seed_cases",
    ROOT / "data" / "real_world_cases",
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def iter_case_files():
    for data_dir in DATA_DIRS:
        if data_dir.exists():
            yield from sorted(data_dir.glob("*.json"))


def main():
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema)

    files = list(iter_case_files())
    if not files:
        print("No JSON case files found.")
        sys.exit(1)

    has_errors = False

    for file_path in files:
        try:
            data = load_json(file_path)
        except Exception as e:
            has_errors = True
            print(f"\n[INVALID JSON] {file_path}: {e}")
            continue

        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            has_errors = True
            print(f"\n[SCHEMA ERRORS] {file_path}")
            for err in errors:
                location = ".".join(str(x) for x in err.path) or "<root>"
                print(f"  - {location}: {err.message}")
        else:
            print(f"[OK] {file_path}")

    if has_errors:
        sys.exit(1)

    print("\nAll case files validated successfully.")


if __name__ == "__main__":
    main()
