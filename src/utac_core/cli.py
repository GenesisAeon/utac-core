"""UTAC-Core CLI — logistic threshold and frame-principle fitting."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel

from .core import SIGMA_PHI, beta_fit, frame_principle, utac_logistic, v_rig

app = typer.Typer(
    name="utac",
    help="UTAC-Core CLI — σ(β(R−Θ)) logistic, Frame-Principle, and v_RIG.",
    add_completion=False,
)
console = Console()


@app.command()
def fit(
    r: list[float] = typer.Option([1.0, 1.618, 2.718], "--r", help="R values"),
    theta: list[float] = typer.Option([0.618, 1.0, 1.618], "--theta", help="Θ values"),
) -> None:
    """Fit β to the UTAC logistic threshold from R and Θ sequences."""
    fitted = beta_fit(r, theta)
    mean_diff = SIGMA_PHI / fitted if fitted else 0.0
    console.print(
        Panel(
            f"[bold green]Fitted β:[/bold green] {fitted:.6f}\n"
            f"[dim]σ_Φ = {SIGMA_PHI}  ·  mean|R−Θ| = {mean_diff:.6f}[/dim]",
            title="β-Fit",
        )
    )


@app.command()
def rig(
    t: float = typer.Argument(10.0, help="Time value t"),
    beta: float = typer.Option(SIGMA_PHI, "--beta", "-b", help="β parameter"),
) -> None:
    """Calculate v_RIG at time t."""
    value = v_rig(t, beta=beta)
    console.print(
        Panel(
            f"[bold cyan]v_RIG(t={t}, β={beta}):[/bold cyan] {value:.6f}",
            title="v_RIG",
        )
    )


@app.command(name="frame-principle")
def frame_principle_cmd() -> None:
    """Show the symbolic Frame-Principle equation."""
    eq = frame_principle()
    console.print(
        Panel(
            f"[bold magenta]{eq}[/bold magenta]\n[dim]σ_Φ ≈ {SIGMA_PHI}[/dim]",
            title="Frame-Principle",
        )
    )


@app.command()
def logistic(
    x: float = typer.Argument(..., help="Input x"),
    beta: float = typer.Option(SIGMA_PHI, "--beta", "-b", help="β parameter"),
    theta: float = typer.Option(0.0, "--theta", "-t", help="Threshold Θ"),
) -> None:
    """Evaluate the UTAC logistic function σ(β(x − Θ))."""
    result = utac_logistic(x, beta=beta, theta=theta)
    console.print(
        Panel(
            f"[bold yellow]σ(β({x}−{theta})) = {result:.6f}[/bold yellow]",
            title="UTAC Logistic",
        )
    )


if __name__ == "__main__":
    app()
