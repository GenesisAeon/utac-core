"""UTAC logistic core: σ(β(R−Θ)), β-Fitting, Frame-Principle, v_RIG."""

from __future__ import annotations

import numpy as np
import sympy as sp
from typing import List

# Symbolic variables
beta_sym, R_sym, Theta_sym = sp.symbols("beta R Theta", real=True)

# UTAC-Logistic: σ(β(R−Θ))
_sigma_utac = sp.Function("sigma")(beta_sym * (R_sym - Theta_sym))

# Frame-Principle constant σ_Φ ≈ 0.0625
SIGMA_PHI: float = 0.0625


def beta_fit(R_values: List[float], Theta_values: List[float]) -> float:
    """Fit β to the UTAC logistic threshold.

    β = σ_Φ / mean(|R − Θ|)
    """
    diff = np.array(R_values) - np.array(Theta_values)
    return float(SIGMA_PHI / np.mean(np.abs(diff)))


def v_rig(t: float, beta: float = SIGMA_PHI) -> float:
    """v_RIG — recursive implosive growth at time t.

    v_RIG(t) = β · ln(t + 1) · σ_Φ
    """
    return float(beta * np.log(t + 1) * SIGMA_PHI)


def frame_principle() -> str:
    """Return the symbolic Frame-Principle equation as a string.

    σ(β(R−Θ)) = σ_Φ
    """
    return str(sp.Eq(_sigma_utac, SIGMA_PHI))


def utac_logistic(x: float, beta: float = SIGMA_PHI, theta: float = 0.0) -> float:
    """Evaluate the UTAC logistic function σ(β(x − Θ)).

    Uses the standard sigmoid: 1 / (1 + exp(−β(x − Θ))).
    """
    return float(1.0 / (1.0 + np.exp(-beta * (x - theta))))
