# Python Coding Practice

This workspace is set up for practicing Python coding problems.

## Structure

- `problems/` - place your solution files here.
- `tests/` - unit tests for your practice problems.
- `templates/` - starter templates for new problems.

## Getting started

1. Open `problems/two_sum.py` and solve the example problem.
2. Run tests from the project root with:

```bash
python -m pytest
```

> Do not run the test file directly with `python tests/test_<name>.py`; use `pytest` so the project root is added to Python path correctly.

### Using `uv`

If you prefer `uv` instead of `venv`, that works well here too. From the project root:

```bash
uv venv .venv
uv pip install pytest
uv run pytest
```

Or if you already have the environment created:

```bash
uv run python -m pytest
```

3. Add a new problem:
   - Copy `templates/problem_template.py` into `problems/<problem_name>.py`
   - Write the solution function(s)
   - Add tests in `tests/test_<problem_name>.py`

## Recommended workflow

- Keep functions small and testable.
- Use descriptive names for problem files and tests.
- Add docstrings for problem descriptions and constraints.
