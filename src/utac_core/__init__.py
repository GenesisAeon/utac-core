"""utac-core — mathematical UTAC logistic core: σ(β(R−Θ)), β-Fitting, Frame-Principle, v_RIG."""

__version__ = "0.1.0"
__author__ = "GenesisAeon Team"

from .core import beta_fit, frame_principle, v_rig

__all__ = ["beta_fit", "frame_principle", "v_rig", "__version__"]
