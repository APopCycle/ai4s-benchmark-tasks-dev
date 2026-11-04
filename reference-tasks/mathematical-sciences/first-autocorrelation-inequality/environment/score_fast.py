#!/usr/bin/env python3
"""Fast, non-certifying AC1 scorer for agent iteration."""

import argparse
import json
import math
from pathlib import Path

import numpy as np


def load_sequence(path: Path) -> np.ndarray:
    payload = json.loads(path.read_text())
    raw = payload.get("sequence", payload.get("values"))
    if not isinstance(raw, list) or not 2 <= len(raw) <= 131072:
        raise ValueError("sequence must be a flat array of length 2..131072")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in raw):
        raise ValueError("every coefficient must be a JSON number")
    values = np.asarray(raw, dtype=np.float64)
    if not np.isfinite(values).all() or (values < 0).any() or (values > 1000).any():
        raise ValueError("coefficients must be finite and lie in [0, 1000]")
    if not math.isfinite(float(values.sum())) or float(values.sum()) < 0.01:
        raise ValueError("coefficient sum must be at least 0.01")
    return values


def score(values: np.ndarray) -> float:
    out_len = 2 * len(values) - 1
    fft_len = 1 << (out_len - 1).bit_length()
    convolution = np.fft.irfft(np.fft.rfft(values, fft_len) ** 2, fft_len)[:out_len]
    return 2.0 * len(values) * float(convolution.max()) / float(values.sum()) ** 2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path, nargs="?", default=Path("/root/results/candidate.json"))
    args = parser.parse_args()
    value = score(load_sequence(args.candidate))
    print(json.dumps({"valid": True, "scientific_score_approx": value}, indent=2))


if __name__ == "__main__":
    main()
