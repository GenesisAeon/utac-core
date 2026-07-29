"""utac-core — UTAC logistic core: σ(β(R−Θ)), β-Fitting, Frame-Principle, v_RIG."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version

try:
    __version__ = _version("utac-core")
except PackageNotFoundError:
    # Not installed, e.g. running from source.
    __version__ = "0.0.0+unknown"

__author__ = "GenesisAeon Team"

from .core import beta_fit, frame_principle, v_rig

__all__ = ["beta_fit", "frame_principle", "v_rig", "__version__"]
