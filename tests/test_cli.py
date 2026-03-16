"""Tests for the utac CLI commands."""

from typer.testing import CliRunner

from utac_core.cli import app

runner = CliRunner()


def test_fit_default():
    result = runner.invoke(app, ["fit"])
    assert result.exit_code == 0
    assert "β" in result.output or "Fitted" in result.output


def test_fit_custom_values():
    result = runner.invoke(
        app,
        ["fit", "--r", "2.0", "--r", "3.0", "--theta", "1.0", "--theta", "1.5"],
    )
    assert result.exit_code == 0
    assert "0.050000" in result.output


def test_rig_default():
    result = runner.invoke(app, ["rig"])
    assert result.exit_code == 0
    assert "v_RIG" in result.output or "RIG" in result.output


def test_rig_custom_t():
    result = runner.invoke(app, ["rig", "1.0"])
    assert result.exit_code == 0


def test_rig_custom_beta():
    result = runner.invoke(app, ["rig", "10.0", "--beta", "0.1"])
    assert result.exit_code == 0


def test_frame_principle():
    result = runner.invoke(app, ["frame-principle"])
    assert result.exit_code == 0
    assert "0.0625" in result.output


def test_logistic_basic():
    result = runner.invoke(app, ["logistic", "1.618"])
    assert result.exit_code == 0
    assert "σ" in result.output or "0." in result.output


def test_logistic_midpoint():
    result = runner.invoke(app, ["logistic", "1.0", "--theta", "1.0"])
    assert result.exit_code == 0
    assert "0.5" in result.output


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "utac" in result.output.lower() or "UTAC" in result.output
