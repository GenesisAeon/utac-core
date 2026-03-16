"""Optional bridge to entropy-table (requires utac-core[stack])."""

from __future__ import annotations

from pathlib import Path


class UtacCoreBridge:
    """Bridge between utac-core computations and the entropy-table registry.

    Requires the [stack] extra: pip install utac-core[stack]
    """

    def __init__(self) -> None:
        try:
            from entropy_table import EntropyTable  # type: ignore[import]
        except ImportError as exc:
            raise ImportError(
                "entropy-table is not installed. "
                "Install it with: pip install utac-core[stack]"
            ) from exc
        self.table = EntropyTable(domain="utac-core")

    def add_utac(self, key: str, value: float) -> None:
        """Register a utac-core relation in the entropy table."""
        self.table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path | str:
        """Export the entropy table to a YAML file."""
        self.table.export(filepath)
        return filepath
