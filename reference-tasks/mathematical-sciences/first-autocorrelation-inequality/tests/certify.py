"""Exact outcome verifier for finite decimal AC1 step constructions."""

from __future__ import annotations

import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

from flint import fmpz_poly

HERE = Path(__file__).resolve().parent
BASELINE = json.loads((HERE / "baseline.json").read_text())
SOTA = Fraction(
    int(BASELINE["sota_exact_numerator"]),
    int(BASELINE["sota_exact_denominator"]),
)
MIN_IMPROVEMENT = Fraction(
    int(BASELINE["minimum_meaningful_improvement_numerator"]),
    int(BASELINE["minimum_meaningful_improvement_denominator"]),
)
PASS_BOUNDARY = SOTA - MIN_IMPROVEMENT
MAX_BYTES = 20_000_000
MIN_LENGTH = 2
MAX_LENGTH = 131_072
MAX_DECIMAL_PLACES = 18


def _reject_constant(token: str):
    raise ValueError(f"non-finite JSON number {token!r}")


def _decimal_string(value: Fraction, digits: int = 60) -> str:
    with localcontext() as context:
        context.prec = digits
        return format(Decimal(value.numerator) / Decimal(value.denominator), "f")


def _fraction_string(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def load_coefficients(path: Path) -> list[Decimal]:
    if not path.is_file():
        raise ValueError("missing /root/results/candidate.json")
    if path.stat().st_size > MAX_BYTES:
        raise ValueError(f"candidate.json exceeds {MAX_BYTES} bytes")
    payload = json.loads(
        path.read_text(),
        parse_float=Decimal,
        parse_int=Decimal,
        parse_constant=_reject_constant,
    )
    if not isinstance(payload, dict) or set(payload) != {"sequence"}:
        raise ValueError("candidate must be an object containing only `sequence`")
    sequence = payload["sequence"]
    if not isinstance(sequence, list) or not MIN_LENGTH <= len(sequence) <= MAX_LENGTH:
        raise ValueError(f"sequence length must be in [{MIN_LENGTH}, {MAX_LENGTH}]")
    values: list[Decimal] = []
    for index, value in enumerate(sequence):
        if isinstance(value, bool) or not isinstance(value, Decimal) or not value.is_finite():
            raise ValueError(f"coefficient {index} is not a finite JSON number")
        if value < 0 or value > 1000:
            raise ValueError(f"coefficient {index} is outside [0, 1000]")
        decimal_places = max(0, -value.as_tuple().exponent)
        if decimal_places > MAX_DECIMAL_PLACES:
            raise ValueError(
                f"coefficient {index} uses {decimal_places} decimal places; maximum is {MAX_DECIMAL_PLACES}"
            )
        values.append(value)
    if sum(values) < Decimal("0.01"):
        raise ValueError("coefficient sum must be at least 0.01")
    return values


def exact_score(values: list[Decimal]) -> Fraction:
    decimal_places = max(max(0, -value.as_tuple().exponent) for value in values)
    scale = 10**decimal_places
    integers = [int(value * scale) for value in values]
    convolution = fmpz_poly(integers) ** 2
    maximum = max(int(value) for value in convolution)
    total = sum(integers)
    return Fraction(2 * len(integers) * maximum, total * total)


def reward_for_score(score: Fraction) -> int:
    return 1 if score <= PASS_BOUNDARY else 0


def evaluate(path: Path) -> dict:
    base = {
        "valid": False,
        "match_sota": False,
        "certified": False,
        "scientific_score": None,
        "scientific_score_exact": None,
        "sota_score": float(SOTA),
        "sota_score_exact": _fraction_string(SOTA),
        "minimum_meaningful_improvement": float(MIN_IMPROVEMENT),
        "improvement_over_sota": None,
        "improvement_over_sota_exact": None,
        "reward": 0,
    }
    try:
        values = load_coefficients(path)
        score = exact_score(values)
    except Exception as exc:
        return {**base, "error": str(exc)}

    improvement = SOTA - score
    reward = reward_for_score(score)
    return {
        **base,
        "valid": True,
        "match_sota": score == SOTA,
        "certified": True,
        "sequence_length": len(values),
        "scientific_score": float(score),
        "scientific_score_decimal": _decimal_string(score),
        "scientific_score_exact": _fraction_string(score),
        "pass_boundary_decimal": _decimal_string(PASS_BOUNDARY),
        "improvement_over_sota": float(improvement),
        "improvement_over_sota_exact": _fraction_string(improvement),
        "reward": reward,
    }
