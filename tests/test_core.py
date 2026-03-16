"""Tests for utac_core.core — β-Fit, v_RIG, Frame-Principle, UTAC logistic."""

import pytest

from utac_core.core import SIGMA_PHI, beta_fit, frame_principle, utac_logistic, v_rig


class TestSigmaPhi:
    def test_value(self):
        assert pytest.approx(0.0625) == SIGMA_PHI


class TestBetaFit:
    def test_basic(self):
        R = [2.0, 3.0]
        Theta = [1.0, 1.5]
        result = beta_fit(R, Theta)
        # mean|R-Theta| = mean([1.0, 1.5]) = 1.25; beta = 0.0625 / 1.25 = 0.05
        assert result == pytest.approx(0.05, rel=1e-6)

    def test_golden_ratio_values(self):
        R = [1.0, 1.618, 2.718]
        Theta = [0.618, 1.0, 1.618]
        result = beta_fit(R, Theta)
        assert result > 0

    def test_equal_values_large_diff(self):
        R = [10.0]
        Theta = [0.0]
        result = beta_fit(R, Theta)
        assert result == pytest.approx(SIGMA_PHI / 10.0, rel=1e-6)

    def test_returns_float(self):
        assert isinstance(beta_fit([1.0], [0.5]), float)


class TestVRig:
    def test_at_t1(self):
        # v_rig(1) = 0.0625 * ln(2) * 0.0625 ≈ 0.002708
        result = v_rig(1.0)
        import numpy as np

        expected = 0.0625 * np.log(2) * 0.0625
        assert result == pytest.approx(expected, rel=1e-6)

    def test_at_t10_default_beta(self):
        import numpy as np

        result = v_rig(10.0)
        expected = SIGMA_PHI * np.log(11.0) * SIGMA_PHI
        assert result == pytest.approx(expected, rel=1e-6)

    def test_custom_beta(self):
        import numpy as np

        result = v_rig(10.0, beta=0.1)
        expected = 0.1 * np.log(11.0) * SIGMA_PHI
        assert result == pytest.approx(expected, rel=1e-6)

    def test_at_t0(self):
        assert v_rig(0.0) == pytest.approx(0.0, abs=1e-12)

    def test_returns_float(self):
        assert isinstance(v_rig(1.0), float)


class TestFramePrinciple:
    def test_returns_string(self):
        assert isinstance(frame_principle(), str)

    def test_contains_sigma_phi(self):
        result = frame_principle()
        assert "0.0625" in result

    def test_is_equation(self):
        result = frame_principle()
        # SymPy renders as Eq(...) or with = sign depending on version
        assert "Eq(" in result or "=" in result


class TestUtacLogistic:
    def test_midpoint(self):
        # At x=theta, sigmoid = 0.5
        result = utac_logistic(1.0, beta=1.0, theta=1.0)
        assert result == pytest.approx(0.5, rel=1e-6)

    def test_above_threshold(self):
        result = utac_logistic(10.0, beta=1.0, theta=0.0)
        assert result > 0.9

    def test_below_threshold(self):
        result = utac_logistic(-10.0, beta=1.0, theta=0.0)
        assert result < 0.1

    def test_default_beta_sigma_phi(self):
        result = utac_logistic(0.0)
        assert result == pytest.approx(0.5, rel=1e-6)

    def test_returns_float(self):
        assert isinstance(utac_logistic(1.0), float)

    def test_output_range(self):
        for x in [-100.0, -1.0, 0.0, 1.0, 100.0]:
            r = utac_logistic(x)
            assert 0.0 < r < 1.0
