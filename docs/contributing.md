Standards
=========

All contributions must satisfy the following criteria in order to be reviewed and merged:

1. Proposed changes must logically relate to `gspread` or worksheets in Google Sheets, Microsoft Excel, or other spreadsheet-like software.
2. Proposed changes must be tested _scrupulously_ with documented tests in `tests/`.
3. The `__all__` double-underscore object must be included at the head of `__init__` and all relevant modules.
4. Proposed changes to `README.md`, `contributions.md`, and `tool.poetry.group.dev.dependencies` must be defended with solid rationale.
5. Object names must be logical, mature, and respectful, i.e. no prejoratives, expletives, etc., as well as sensible and in accordance with PEP standards.
6. Documentation must be provided for functions and classes in accordance with [numpydoc](https://numpydoc.readthedocs.io/en/latest/index.html) standards.
7. Documentation must be written in standard written english.
8. New functions, classes, methods, etc. must be intuitive--that is, easy to comprehend and use.
9. Take pride in your work. Although this project is small, that is not an excuse to release sloppy code. Do not shy away from using new features in the standard library or from the open source community.
10. Please update the directory tree in `README.md` before opening a pull request!

Step by Step Instructions
=========================

Clone the repo to your local machine. Do not forget to create a new branch!

```bash
$ git clone https://github.com/<your-user-name>/gspread-helpers.git && cd gspread-helpers
```

Install poetry in your virtual environment and install all of the necessary dependencies using `poetry install`.

```bash
$ poetry install
```

Make your changes. Test those changes with `pytest`.

```bash
$ pytest tests/<file name>.py
```

Add any new dependencies using `poetry add`. Validate the subsequent changes to `pyproject.toml` using `poetry check`.

```bash
$ poetry add <your new dependency>
$ poetry check
```

Install all hooks and verify that your changes pass the tests according to `black`, `isort`, and `flake8`, as found in `.pre-commit-config.yaml`. TIP: You do not _need_ to use `run`. Instead, you can wait until running `git commit`. The Git hooks will be activated at that time, and the tests will fail or succeed accordingly. It's up to you, though!

```bash
$ git add .
$ pre-commit install
$ pre-commit run
```

If all of your changes have passed the tests and hooks then you should be good to finally commit and open a pull request!

```bash
$ git commit -m "<your message>"
```