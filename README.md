# Intuition Delta

Intuition Delta is an open-source ledger of high-fidelity human override data.

It captures cases where AI systems produced outputs with strong logical confidence — sometimes with near-certainty — but expert human judgment determined those outputs were incorrect. These moments of disagreement are especially valuable because they reveal the limits of probabilistic reasoning and expose where human intuition, context, or expertise outperforms model confidence.

The goal of this repository is to preserve those expert decisions as structured learning data, so AI systems can improve from real-world corrections rather than confidence alone.

Intuition Delta maps the divergence between AI probabilistic outputs and expert human intuition — creating a shared ledger of the decisions that matter most.

## Data Layout

Intuition Delta stores two kinds of records:

- `data/public_seed_cases/` — benchmark- or publication-derived seed records used to initialize the ledger.
- `data/real_world_cases/` — real human override cases captured from practice.

Public seed cases are not claimed to be original field incidents unless explicitly marked as such.

## Data Model

Each case is stored as a standalone JSON file and validated against `schema/case.schema.json`.

Key provenance fields:
- `source_name`
- `source_url`
- `source_type`
- `is_public_seed`
- `evidence_status`
- `example_granularity`

These fields help distinguish source-backed benchmark seeds from incident-level real-world overrides.

## Validation

Run:

```bash
pip install jsonschema
python scripts/validate_cases.py
