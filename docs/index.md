# utac-core

**The mathematical UTAC logistic core** — σ(β(R−Θ)), β-Fitting, Frame-Principle (σ_Φ ≈ 0.0625) and v_RIG for unified field emergence.

## Install

```bash
pip install utac-core
# with full GenesisAeon stack integration:
pip install "utac-core[stack]"
```

## Quick start

```bash
utac fit
utac frame-principle
utac rig 10.0
utac logistic 1.618 --theta 1.0
```

## Python API

```python
from utac_core import beta_fit, v_rig, frame_principle
from utac_core.core import utac_logistic, SIGMA_PHI

# Fit β from field data
beta = beta_fit([1.0, 1.618, 2.718], [0.618, 1.0, 1.618])

# Evaluate UTAC logistic σ(β(x − Θ))
sigma = utac_logistic(1.618, beta=SIGMA_PHI, theta=1.0)

# Recursive implosive growth
growth = v_rig(t=10.0)

# Symbolic Frame-Principle equation
print(frame_principle())
```

## Mathematics

| Symbol | Meaning |
|--------|---------|
| σ(β(R−Θ)) | UTAC logistic function |
| σ_Φ ≈ 0.0625 | Frame-Principle constant (1/16) |
| β | Logistic steepness / fitting parameter |
| R | Field resonance value |
| Θ | Logistic threshold |
| v_RIG | Recursive implosive growth: β·ln(t+1)·σ_Φ |
