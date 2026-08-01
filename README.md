# utac-core

**The mathematical UTAC logistic core** — σ(β(R−Θ)), β-Fitting, Frame-Principle (σ_Φ ≈ 0.0625) and v_RIG for unified field emergence.

[![CI](https://github.com/GenesisAeon/utac-core/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/utac-core/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: GPL-3.0-or-later](https://img.shields.io/badge/Code-GPLv3--or--later-blue.svg)](LICENSE)
[![Docs License: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS.md)
[![PyPI](https://img.shields.io/pypi/v/utac-core)](https://pypi.org/project/utac-core/)

---

## Installation

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
utac logistic 1.618 --beta 0.0625 --theta 1.0
```

## Python API

```python
from utac_core import beta_fit, v_rig, frame_principle
from utac_core.core import utac_logistic, SIGMA_PHI

# Fit β from field data
beta = beta_fit([1.0, 1.618, 2.718], [0.618, 1.0, 1.618])

# Evaluate UTAC logistic σ(β(x − Θ)) using the fitted β
sigma = utac_logistic(1.618, beta=beta, theta=1.0)

# Recursive implosive growth, also using the fitted β
growth = v_rig(t=10.0, beta=beta)

# Symbolic Frame-Principle equation
print(frame_principle())   # sigma(beta*(R - Theta)) = 0.0625
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

## Structure

```
utac-core/
├── src/utac_core/
│   ├── __init__.py
│   ├── core.py                  # σ(β(R−Θ)), β-Fit, Frame-Principle, v_RIG
│   ├── cli.py                   # utac CLI (Typer + Rich)
│   └── entropy_table_bridge.py  # optional [stack] bridge
├── tests/
│   ├── test_core.py
│   └── test_cli.py
├── domains.yaml
└── pyproject.toml
```

## Citation

If you use utac-core in research, please cite it via its Zenodo DOI:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20996681.svg)](https://doi.org/10.5281/zenodo.20996681)

**DOI**: [10.5281/zenodo.20996681](https://doi.org/10.5281/zenodo.20996681)
**PyPI**: `pip install utac-core` (or `pip install "utac-core[stack]"` for the full GenesisAeon stack)

## Role in the GenesisAeon Ecosystem

utac-core (P-CORE) is the UTAC base engine of the GenesisAeon ecosystem,
providing the logistic ODE / CREP tensor core that downstream packages
(`sigillin`, `mandala-visualize`, `sonification`, `aeon-ai`, and others)
build on.

## License

Source code is licensed under [GPL-3.0-or-later](LICENSE). Documentation
is licensed under [CC BY 4.0](LICENSE-DOCS.md).

---

Built with [SymPy](https://www.sympy.org/) · [NumPy](https://numpy.org/) · [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/)
