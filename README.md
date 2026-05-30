# Yin-Yang Convergence Window Protocol

A control-layer protocol for convergence window design, phase stability, amplitude threshold control, rebalance timing, and stability decisions in oscillating reasoning systems.

## Status

Draft specification.

Current version: `v0.1.0`

This repository defines an early structural protocol for describing how oscillating reasoning systems may stabilize, converge, rebalance, delay return, or stop after a settling period.

It extends the conceptual lineage of:

```text
Yin-Yang Five-Phase Reasoning Protocol
        ↓
Yin-Yang Oscillation Control Protocol
        ↓
Yin-Yang Convergence Window Protocol
```

This repository does not claim benchmark-proven performance improvement, hardware-level energy reduction, production readiness, or replacement of existing model architectures.

It defines a control vocabulary for reasoning convergence.

## Purpose

The purpose of this protocol is to describe how a reasoning system can decide when an oscillating reasoning process has become sufficiently stable.

It focuses on:

* convergence windows
* phase stability
* amplitude thresholds
* rebalance timing
* overcorrection prevention
* settling period control
* delayed return readiness
* stop readiness after oscillation
* controlled return from instability to balance

In simple terms:

```text
Oscillation Control asks:
How does reasoning move?

Convergence Window asks:
When has reasoning become stable enough to stop, return, delay, or continue minimally?
```

## Core Idea

Reasoning does not always become clear immediately.

A system may pass through several states:

```text
expand -> critique -> compress -> return -> rebalance -> stabilize
```

The question is not only:

```text
Should reasoning continue?
```

but also:

```text
Has reasoning entered a stable convergence window?
```

This protocol defines that window.

## Minimal Definition

Yin-Yang Convergence Window Protocol is a draft structural protocol for detecting, describing, and controlling convergence windows in phase-based reasoning systems.

## Short Definition

Reasoning should breathe.

But breathing should also settle.

A reasoning system should know when its oscillation has become useful, stable, excessive, premature, or ready to stop.

## Relationship to Parent Protocols

### Yin-Yang Five-Phase Reasoning Protocol

The Yin-Yang Five-Phase Reasoning Protocol defines the core reasoning roles:

```text
Wood  = direction
Fire  = expansion
Earth = integration
Metal = critique
Water = memory
```

It also defines dynamic control metrics and Yin-Yang Balancer.

This repository assumes that phase-based reasoning can move between activation, integration, critique, compression, memory, and return.

### Yin-Yang Oscillation Control Protocol

The Yin-Yang Oscillation Control Protocol describes how reasoning may move between activation and restraint.

It focuses on:

* oscillation amplitude
* dynamic rebalance
* control cycles
* expansion / compression movement
* controlled shifts between Yang and Yin tendencies

### Yin-Yang Convergence Window Protocol

This protocol focuses on the next question:

```text
When is the oscillation stable enough?
```

It adds a convergence-oriented vocabulary:

* `convergence_window`
* `phase_stability_score`
* `amplitude_threshold`
* `rebalance_interval`
* `overcorrection_limit`
* `settling_period`
* `stability_decision`

## Key Concepts

## Convergence Window

A convergence window is a temporary range in which reasoning is considered stable enough to stop, compress, return, delay, or produce a final answer.

It does not mean absolute certainty.

It means the current reasoning flow has reached a usable level of stability.

A convergence window may be:

```text
closed
opening
open
unstable
expired
```

## Phase Stability Score

`phase_stability_score` describes how stable the current phase sequence appears.

A high score may indicate:

* low phase conflict
* reduced oscillation amplitude
* stable context integration
* sufficient stop readiness
* low redundancy pressure
* low overcorrection risk

A low score may indicate:

* phase conflict
* excessive oscillation
* context drift
* redundancy pressure
* low stop readiness
* instability after rebalance

`phase_stability_score` is not a truth score.

It is a control-layer indicator for convergence decisions.

## Amplitude Threshold

`amplitude_threshold` defines the maximum acceptable swing between expansion and restraint before rebalancing is required.

Example:

```text
Yang expansion is high.
Yin suppression rises.
The system checks whether the swing remains within the allowed threshold.
```

If the amplitude remains within threshold, the reasoning flow may enter a convergence window.

If the amplitude exceeds threshold, the system may need compression, delay, or rebalance.

## Rebalance Interval

`rebalance_interval` defines how frequently the system should re-evaluate its state.

Possible values include:

```text
immediate
short
moderate
delayed
none
```

Too short an interval may cause overcorrection.

Too long an interval may allow runaway expansion or stagnation.

## Overcorrection Prevention

`overcorrection_prevention` prevents a system from switching too aggressively between expansion and suppression.

This helps avoid unstable loops such as:

```text
expand -> suppress -> expand -> suppress -> expand
```

The protocol may prevent overcorrection by requiring:

* a minimum settling period
* limited rebalance attempts
* context checking before reversal
* avoiding immediate opposite actions

## Settling Period

`settling_period` defines a stabilization period before final stopping, delayed return, or minimal continuation.

A settling period may be useful:

* after compression
* after critique
* after rebalance
* after memory return
* before final stop

This allows the system to avoid ending too early or reactivating too quickly.

## Stability Decision

`stability_decision` describes the result of convergence evaluation.

Possible decisions may include:

```text
continue_expansion
compress_then_continue
rebalance
enter_convergence_window
delay_return
stop_after_settling
reject_convergence
request_additional_integration
```

These are protocol-level control decisions.

They do not guarantee correctness, safety, or truth.

## Initial Protocol Layers

This repository may be understood through five layers.

### Layer 1: Oscillation Input Layer

Receives current oscillation signals.

Example:

```yaml
oscillation_input:
  yang_level: 0.78
  yin_level: 0.52
  balance_pressure: 0.64
```

Typical inputs:

* `yang_level`
* `yin_level`
* `balance_pressure`
* `current_phase`
* `active_phase_count`
* `expansion_depth`
* `compression_level`
* `critique_pressure`
* `memory_settling_required`

### Layer 2: Stability Measurement Layer

Calculates stability-related indicators.

Example:

```yaml
stability_measurement:
  phase_stability_score: 0.71
  amplitude_delta: 0.26
  context_drift: 0.18
  redundancy_pressure: 0.32
  stop_readiness: 0.69
```

This layer estimates whether the current reasoning flow is:

* unstable
* partially stable
* opening toward convergence
* stable enough for final review
* ready to stop after settling

### Layer 3: Convergence Window Layer

Determines whether the current reasoning state has entered a usable convergence window.

Example:

```yaml
convergence_window:
  status: open
  confidence: 0.74
  allowed_duration: short
```

The convergence window layer helps decide whether the system should stop, settle, return, delay, or continue minimally.

### Layer 4: Rebalance Timing Layer

Determines whether rebalancing should happen now, later, or not at all.

Example:

```yaml
rebalance_timing:
  rebalance_required: true
  rebalance_interval: moderate
  overcorrection_risk: low
```

This layer prevents unnecessary reactivation and avoids unstable correction loops.

### Layer 5: Stability Decision Layer

Produces the final convergence-related control decision.

Example:

```yaml
stability_decision:
  action: stop_after_settling
  reason: convergence_window_open
```

This layer selects the next control action.

## Example Conceptual Flow

```text
Fire expansion increases
        ↓
Water compression rises
        ↓
Earth checks integration stability
        ↓
Metal detects remaining excess
        ↓
Amplitude falls below threshold
        ↓
Convergence window opens
        ↓
System stops after settling
```

## Example Control Profile

```yaml
oscillation_input:
  yang_level: 0.68
  yin_level: 0.46
  balance_pressure: 0.62
  current_phase: earth
  active_phase_count: 3
  expansion_depth: 3
  compression_level: 0.57
  critique_pressure: 0.41
  memory_settling_required: false

stability_measurement:
  phase_stability_score: 0.74
  amplitude_delta: 0.22
  context_drift: 0.18
  redundancy_pressure: 0.34
  stop_readiness: 0.71

convergence_window:
  status: open
  confidence: 0.76
  allowed_duration: short

rebalance_timing:
  rebalance_required: false
  rebalance_interval: none
  overcorrection_risk: low
  next_check: final_review

stability_decision:
  action: stop_after_settling
  reason: convergence_window_open
```

## Repository Structure

```text
yin-yang-convergence-window-protocol-v0.1/
├── README.md
├── spec/
│   └── convergence-window-protocol-v0.1.yaml
├── schemas/
│   └── convergence-window.schema.json
├── examples/
│   ├── basic-convergence-window.example.yaml
│   ├── phase-stability-score.example.yaml
│   ├── amplitude-threshold.example.yaml
│   └── rebalance-interval.example.yaml
├── scripts/
│   └── validate_specs.py
├── .github/
│   └── workflows/
│       └── validate-specs.yml
├── CHANGELOG.md
├── CITATION.cff
└── LICENSE
```

## Key Documents

### Core Specification

* `spec/convergence-window-protocol-v0.1.yaml`

  Machine-readable draft specification for the Yin-Yang Convergence Window Protocol.

  It defines:

  * convergence window detection
  * phase stability scoring
  * amplitude threshold control
  * rebalance timing
  * overcorrection prevention
  * settling period control
  * stability decisions
  * delayed return readiness
  * stop readiness after oscillation

* `schemas/convergence-window.schema.json`

  JSON Schema for validating the core convergence window specification.

  The schema checks the main specification structure while remaining flexible enough for future protocol extensions.

### Examples

* `examples/basic-convergence-window.example.yaml`

  Demonstrates how an oscillating reasoning process may enter a convergence window and stop after a short settling period.

* `examples/phase-stability-score.example.yaml`

  Demonstrates how `phase_stability_score` may be interpreted across low, medium, and high stability states.

* `examples/amplitude-threshold.example.yaml`

  Demonstrates how `amplitude_delta` may be compared against acceptable, warning, high, and critical threshold bands.

* `examples/rebalance-interval.example.yaml`

  Demonstrates how `rebalance_interval` may determine whether reasoning should rebalance immediately, after a short interval, after settling, after memory return, or not at all.

### Validation

* `scripts/validate_specs.py`

  Local validation script for the protocol specification and examples.

  It validates:

  * required repository files
  * the core YAML specification against the JSON Schema
  * example YAML structure
  * example version consistency
  * normalized control values from `0.0` to `1.0`
  * required structural groups in each example

* `.github/workflows/validate-specs.yml`

  GitHub Actions workflow for automated validation.

  It runs the local validation script on push, pull request, tag push, and manual workflow dispatch.

### Release and Citation

* `CHANGELOG.md`

  Documents release history and notable changes.

* `CITATION.cff`

  Provides citation metadata for the protocol.

* `LICENSE`

  MIT License.

## Start Here

Recommended reading order:

1. `README.md`
2. `spec/convergence-window-protocol-v0.1.yaml`
3. `schemas/convergence-window.schema.json`
4. `examples/basic-convergence-window.example.yaml`
5. `examples/phase-stability-score.example.yaml`
6. `examples/amplitude-threshold.example.yaml`
7. `examples/rebalance-interval.example.yaml`
8. `scripts/validate_specs.py`
9. `CHANGELOG.md`
10. `CITATION.cff`

## Validation

This repository includes automated validation for the core specification and examples.

The validation checks:

* required repository files exist
* `spec/convergence-window-protocol-v0.1.yaml` validates against `schemas/convergence-window.schema.json`
* all example YAML files are structurally valid
* all example files use version `0.1.0`
* normalized control values remain within `0.0` to `1.0`
* `basic-convergence-window.example.yaml` includes convergence-window control structure
* `phase-stability-score.example.yaml` includes low, medium, and high stability cases
* `amplitude-threshold.example.yaml` includes acceptable, warning, high, and critical amplitude cases
* `rebalance-interval.example.yaml` includes immediate, short, moderate, delayed, and none rebalance cases

Run validation locally:

```bash
python scripts/validate_specs.py
```

GitHub Actions runs the same validation automatically through:

```text
.github/workflows/validate-specs.yml
```

The validation process is intentionally lightweight.

It is designed to confirm structural consistency, YAML validity, schema alignment, version alignment, and normalized value ranges.

It does not test empirical performance, benchmark improvement, hardware-level energy reduction, or production readiness.

## Suggested Use Cases

This protocol may support:

* adaptive stopping experiments
* convergence-aware reasoning control
* phase-stability evaluation
* multi-agent reasoning stabilization
* delayed return control
* overcorrection prevention
* lightweight assistant behavior tuning
* reasoning workflow documentation
* convergence-window test vectors
* balance-aware routing experiments

These are structural use cases.

They require implementation and evaluation before empirical claims can be made.

## Implementation Possibilities

This protocol may be implemented in several ways.

### Prompt-Level Implementation

A prompt-level implementation may use the convergence window model to decide when an answer is stable enough to stop.

Example:

```text
1. Estimate whether the reasoning has expanded enough.
2. Check whether compression has reduced redundancy.
3. Estimate phase stability.
4. Check whether amplitude remains within threshold.
5. Decide whether to stop after settling, continue minimally, or rebalance.
```

### Agent-Level Implementation

In a multi-agent system, this protocol may act as a convergence evaluator.

Example:

```text
Expansion Agent     -> produces reasoning branches
Critique Agent      -> detects weak or redundant branches
Integration Agent   -> checks context fit
Memory Agent        -> retains useful patterns
Convergence Monitor -> decides whether the system is stable enough
```

### Policy-Level Implementation

A policy-level implementation may use convergence signals as routing conditions.

Example:

```yaml
policies:
  convergence_policy:
    trigger:
      - phase_stability_score_high
      - amplitude_delta_within_threshold
      - stop_readiness_rising
    action: enter_convergence_window

  rebalance_policy:
    trigger:
      - amplitude_delta_exceeds_threshold
      - phase_conflict_detected
      - context_drift_high
    action: rebalance

  stop_policy:
    trigger:
      - convergence_window_open
      - stop_readiness_high
      - redundancy_pressure_low
    action: stop_after_settling
```

## Design Principles

## 1. Convergence Is Not Absolute Certainty

A convergence window does not mean the reasoning is perfectly correct.

It means the reasoning has reached a usable level of stability for a control decision.

## 2. Stability Requires Multiple Signals

`phase_stability_score` should not be used alone.

It should be interpreted together with:

* `amplitude_delta`
* `context_drift`
* `redundancy_pressure`
* `stop_readiness`
* `memory_settling_required`

## 3. Rebalance Should Not Be Automatic

Not every instability requires immediate rebalance.

Sometimes the correct action is:

* wait briefly
* compress first
* delay return
* allow memory to settle
* avoid unnecessary reversal

## 4. Overcorrection Is a Failure Mode

A system can become unstable by correcting itself too aggressively.

This protocol treats overcorrection as a control risk.

## 5. Stopping May Require Settling

Stopping immediately after compression or critique may be premature.

A settling period can help prevent abrupt or unstable conclusions.

## 6. Convergence Is a Control Decision

Convergence is not a claim of truth.

It is a decision about whether the current reasoning state is stable enough to stop, delay, return, rebalance, or continue minimally.

## Non-Goals

This protocol does not attempt to:

* prove measured energy reduction
* replace model architecture
* guarantee better reasoning accuracy
* guarantee safer AI behavior
* define a complete inference engine
* provide a production-ready runtime
* claim universal novelty
* claim benchmark-proven improvement
* define a physical law of inference
* claim that convergence equals truth
* claim that phase stability guarantees correctness

This is a draft structural protocol, not a completed implementation.

## Claim Boundaries

This repository makes structural claims.

It may claim that it:

* proposes a convergence-window control model
* defines a vocabulary for phase stability and rebalance timing
* provides schema-backed draft specification files
* includes example YAML profiles
* may support future convergence-aware reasoning experiments

It should not claim without evidence that it:

* improves benchmark performance
* reduces actual hardware energy usage
* guarantees safer AI behavior
* replaces existing architectures
* solves reasoning instability
* is production-ready
* is a complete runtime system

Recommended external description:

```text
A draft structural protocol for convergence-window design, phase stability,
amplitude threshold control, and rebalance timing in oscillating reasoning systems.
```

## Future Work

Possible future work includes:

* convergence test vectors
* oscillation decay profiles
* phase-stability thresholds
* convergence confidence scoring
* integration with Multi-Wing systems
* implementation profiles for prompt-level assistants
* agent-framework examples
* additional validation scripts
* comparison with adaptive reasoning and early stopping methods
* relationship documentation for parent protocols
* claim-boundary documentation
* reference implementation experiments

## Citation

If you use this specification, please cite:

```text
Yin-Yang Convergence Window Protocol
SamuraiWriter7
2026
```

See `CITATION.cff` for citation metadata.

## License

This project is licensed under the MIT License.

See `LICENSE` for details.

## Summary

The Yin-Yang Convergence Window Protocol defines how an oscillating reasoning process may become stable enough to stop, delay, return, rebalance, or continue minimally.

Its core architecture is:

```text
Oscillation Input = current reasoning movement
Stability Measurement = phase stability and amplitude signals
Convergence Window = usable stability range
Rebalance Timing = when to adjust
Overcorrection Prevention = avoiding unstable reversals
Settling Period = stabilization before final action
Stability Decision = stop, continue, delay, or rebalance
```

The central principle is:

```text
Reasoning should breathe, but breathing should also settle.
```
