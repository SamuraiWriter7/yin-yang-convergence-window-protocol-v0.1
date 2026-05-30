#!/usr/bin/env python3
"""
Validation script for Yin-Yang Convergence Window Protocol.

This script validates:

- spec/convergence-window-protocol-v0.1.yaml
- schemas/convergence-window.schema.json
- examples/*.example.yaml

It performs JSON Schema validation for the main spec and lightweight
structural validation for the examples.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft7Validator


ROOT = Path(__file__).resolve().parents[1]

SPEC_PATH = ROOT / "spec" / "convergence-window-protocol-v0.1.yaml"
SCHEMA_PATH = ROOT / "schemas" / "convergence-window.schema.json"

EXAMPLE_PATHS = [
    ROOT / "examples" / "basic-convergence-window.example.yaml",
    ROOT / "examples" / "phase-stability-score.example.yaml",
    ROOT / "examples" / "amplitude-threshold.example.yaml",
    ROOT / "examples" / "rebalance-interval.example.yaml",
]

EXPECTED_VERSION = "0.1.0"

NORMALIZED_KEYS = {
    "yang_level",
    "yin_level",
    "balance_pressure",
    "compression_level",
    "critique_pressure",
    "phase_stability_score",
    "amplitude_delta",
    "context_drift",
    "redundancy_pressure",
    "stop_readiness",
    "confidence",
}


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def require_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path.relative_to(ROOT)}")


def validate_spec_against_schema() -> None:
    print(f"Validating spec: {SPEC_PATH.relative_to(ROOT)}")
    print(f"Using schema: {SCHEMA_PATH.relative_to(ROOT)}")

    spec_data = load_yaml(SPEC_PATH)
    schema_data = load_json(SCHEMA_PATH)

    validator = Draft7Validator(schema_data)
    errors = sorted(
        validator.iter_errors(spec_data),
        key=lambda error: list(error.path),
    )

    if errors:
        print("Schema validation failed:")
        for error in errors:
            path = ".".join(str(part) for part in error.path)
            location = path if path else "<root>"
            print(f"- {location}: {error.message}")
        raise SystemExit(1)

    version = spec_data.get("protocol", {}).get("version")
    if version != EXPECTED_VERSION:
        raise ValueError(
            f"Expected protocol.version to be {EXPECTED_VERSION}, got {version!r}"
        )

    print("Spec validation passed.")


def require_keys(data: dict[str, Any], keys: list[str], path: Path) -> None:
    missing = [key for key in keys if key not in data]
    if missing:
        raise ValueError(
            f"{path.relative_to(ROOT)} is missing required keys:\n"
            + "\n".join(missing)
        )


def validate_normalized_values(data: Any, path: Path, location: str = "") -> None:
    if isinstance(data, dict):
        for key, value in data.items():
            next_location = f"{location}.{key}" if location else key

            if key in NORMALIZED_KEYS and isinstance(value, (int, float)):
                if not 0.0 <= float(value) <= 1.0:
                    raise ValueError(
                        f"{path.relative_to(ROOT)} has out-of-range normalized value "
                        f"at {next_location}: {value!r}"
                    )

            validate_normalized_values(value, path, next_location)

    elif isinstance(data, list):
        for index, item in enumerate(data):
            next_location = f"{location}[{index}]"
            validate_normalized_values(item, path, next_location)


def validate_example_version(data: dict[str, Any], path: Path) -> None:
    version = data.get("example", {}).get("version")
    if version != EXPECTED_VERSION:
        raise ValueError(
            f"Expected example.version in {path.relative_to(ROOT)} "
            f"to be {EXPECTED_VERSION}, got {version!r}"
        )


def validate_basic_convergence_example(data: dict[str, Any], path: Path) -> None:
    require_keys(
        data,
        [
            "example",
            "input",
            "initial_state",
            "oscillation_input",
            "stability_measurement",
            "convergence_window",
            "rebalance_timing",
            "settling_period",
            "stability_decision",
            "result",
            "validation_notes",
        ],
        path,
    )


def validate_phase_stability_example(data: dict[str, Any], path: Path) -> None:
    require_keys(
        data,
        [
            "example",
            "purpose",
            "input",
            "phase_stability_model",
            "stability_factors",
            "cases",
            "comparison_summary",
            "result",
            "validation_notes",
        ],
        path,
    )

    cases = data.get("cases", [])
    if not isinstance(cases, list) or len(cases) < 3:
        raise ValueError(
            f"{path.relative_to(ROOT)} should include low, medium, and high cases."
        )


def validate_amplitude_threshold_example(data: dict[str, Any], path: Path) -> None:
    require_keys(
        data,
        [
            "example",
            "purpose",
            "input",
            "amplitude_threshold_model",
            "calculation_method",
            "cases",
            "overcorrection_prevention",
            "comparison_summary",
            "result",
            "validation_notes",
        ],
        path,
    )

    cases = data.get("cases", [])
    if not isinstance(cases, list) or len(cases) < 4:
        raise ValueError(
            f"{path.relative_to(ROOT)} should include acceptable, warning, high, and critical cases."
        )


def validate_rebalance_interval_example(data: dict[str, Any], path: Path) -> None:
    require_keys(
        data,
        [
            "example",
            "purpose",
            "input",
            "rebalance_interval_model",
            "default_policy",
            "cases",
            "comparison_summary",
            "result",
            "validation_notes",
        ],
        path,
    )

    cases = data.get("cases", [])
    if not isinstance(cases, list) or len(cases) < 5:
        raise ValueError(
            f"{path.relative_to(ROOT)} should include immediate, short, moderate, delayed, and none cases."
        )


def validate_example(path: Path) -> None:
    print(f"Validating example: {path.relative_to(ROOT)}")

    data = load_yaml(path)

    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must be a YAML mapping.")

    validate_example_version(data, path)
    validate_normalized_values(data, path)

    filename = path.name

    if filename == "basic-convergence-window.example.yaml":
        validate_basic_convergence_example(data, path)
    elif filename == "phase-stability-score.example.yaml":
        validate_phase_stability_example(data, path)
    elif filename == "amplitude-threshold.example.yaml":
        validate_amplitude_threshold_example(data, path)
    elif filename == "rebalance-interval.example.yaml":
        validate_rebalance_interval_example(data, path)
    else:
        raise ValueError(f"Unexpected example file: {filename}")

    print(f"Example validation passed: {path.relative_to(ROOT)}")


def main() -> int:
    try:
        required_files = [SPEC_PATH, SCHEMA_PATH, *EXAMPLE_PATHS]

        for path in required_files:
            require_file(path)

        validate_spec_against_schema()

        for path in EXAMPLE_PATHS:
            validate_example(path)

        print("All validations passed.")
        return 0

    except Exception as error:
        print("Validation failed.")
        print(f"Error: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

