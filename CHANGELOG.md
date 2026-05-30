# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight semantic versioning style for specification development.

## [0.1.0] - 2026-05-31

### Added

Initial draft release of the Yin-Yang Convergence Window Protocol.

Added the core protocol structure:

* convergence window detection
* phase stability scoring
* amplitude threshold control
* rebalance timing
* overcorrection prevention
* settling period control
* stability decision model
* delayed return readiness
* stop readiness after oscillation

### Core Specification

Added:

* `spec/convergence-window-protocol-v0.1.yaml`
* `schemas/convergence-window.schema.json`

### Examples

Added initial examples:

* `examples/basic-convergence-window.example.yaml`
* `examples/phase-stability-score.example.yaml`
* `examples/amplitude-threshold.example.yaml`
* `examples/rebalance-interval.example.yaml`

### Validation

Added validation infrastructure:

* `scripts/validate_specs.py`
* `.github/workflows/validate-specs.yml`

The validation checks:

* required repository files exist
* the core YAML specification validates against the JSON Schema
* example YAML files are structurally valid
* example versions are aligned with `0.1.0`
* normalized control values remain within `0.0` to `1.0`
* convergence-window examples include required structural groups

### Core Concepts

The initial protocol defines how oscillating reasoning systems may determine whether they are stable enough to stop, delay, return, rebalance, or continue minimally.

Core architecture:

```text
Oscillation Input = current reasoning movement
Stability Measurement = phase stability and amplitude signals
Convergence Window = usable stability range
Rebalance Timing = when to adjust
Overcorrection Prevention = avoiding unstable reversals
Settling Period = stabilization before final action
Stability Decision = stop, continue, delay, or rebalance
```

### Relationship to Parent Protocols

This protocol is positioned as a convergence-focused extension in the following lineage:

```text
Yin-Yang Five-Phase Reasoning Protocol
        ↓
Yin-Yang Oscillation Control Protocol
        ↓
Yin-Yang Convergence Window Protocol
```

The parent protocols define reasoning phases, oscillation, and balance control.

This repository focuses specifically on convergence windows, phase stability, amplitude thresholds, and rebalance timing.

### Non-Goals

This initial release does not attempt to:

* prove measured energy reduction
* replace model architecture
* guarantee better reasoning accuracy
* guarantee safer AI behavior
* define a complete inference engine
* provide a production-ready runtime
* claim universal novelty
* claim benchmark-proven improvement
* define a physical law of inference

This is a draft structural protocol, not a completed implementation.

### Notes

The central principle of the protocol is:

```text
Reasoning should breathe, but breathing should also settle.
```
