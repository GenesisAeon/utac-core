# Contributing

Thanks for your interest in contributing to utac-core!

## Getting started

1. Fork and clone the repository.
2. Create a virtual environment: `python -m venv .venv && source .venv/bin/activate`
   (or `.venv\Scripts\activate` on Windows).
3. Install in editable mode with dev dependencies: `pip install -e ".[dev]"`.
4. Run the test suite: `pytest`.

## Code style

- Format and lint with `ruff check src tests`.
- Type-check with `mypy src`.
- Keep functions documented with docstrings.

## Licensing of contributions

By submitting a pull request, you agree that your code contributions are
licensed under **GPL-3.0-or-later** and any documentation contributions
under **CC BY 4.0**, consistent with this repo's dual-license scheme (see
`LICENSE` and `LICENSE-DOCS.md`).

## Pull requests

- One logical change per PR.
- Add or update tests for any behavioral change.
- Update `CHANGELOG.md` under an `## [Unreleased]` section.
- Fill out the PR template (`.github/PULL_REQUEST_TEMPLATE.md`).

## Reporting issues

Please use the issue templates in `.github/ISSUE_TEMPLATE/` — they help us
triage bug reports vs. feature requests quickly.
