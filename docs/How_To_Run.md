# How to Run the Nelishka Application

This project is a Python package installed in editable mode and exposes a CLI entry point via `setup.py`.

## Prerequisites

- Python 3.12+
- pip installed
- Virtual environment (recommended)

---

## 1. Create Virtual Environment

```bash
python -m venv venv
```

---

## 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

---

## 3. Install the Project

Install the package in editable mode:

```bash
pip install -e .
```

---

## 4. Run the Application (CLI)

Run the CLI command defined in `setup.py`:

```bash
nelishka-cli
```

---

## 5. Alternative Run Method (Module Mode)

```bash
python -m cli.main
```

---

## Running Without Activation (Optional)

You can also run everything in one step:

```bash
python -m venv venv
source venv/bin/activate
pip install -e .
nelishka-cli
```