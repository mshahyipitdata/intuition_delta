
# Failure Types

This project uses a controlled taxonomy for classifying AI-human divergence.

## Core categories

- `hallucination` — the model states false information as if it were true.
- `missing_context` — the model lacked relevant situational or external context.
- `bad_assumption` — the model relied on an incorrect premise.
- `incorrect_inference` — the reasoning chain was plausible but invalid.
- `expertise_gap` — domain expertise was required beyond model competence.
- `stale_knowledge` — the answer depended on outdated knowledge.
- `anchoring_error` — the model fixated on an early but wrong interpretation.
- `ungrounded_claim` — the output was not supported by evidence or source context.
- `real_world_chat_failure` — failure observed in authentic interactive use.
- `diagnostic_error` — incorrect clinical or diagnostic reasoning.
- `reasoning_error` — broader logical mistake not captured above.
- `factual_error` — factually incorrect answer.
