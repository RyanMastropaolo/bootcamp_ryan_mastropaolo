# Homework 05 — Data Storage

## Data Storage

### Folder Structure

```
homework05/
├── data/
│   ├── raw/         # CSV files (source-of-truth snapshots)
│   └── processed/   # Parquet files (validated/typed downstream copies)
├── .env             # DATA_DIR_RAW, DATA_DIR_PROCESSED (not committed with real secrets)
├── .env.example      # template for .env
└── stage05_data-storage_homework-starter.ipynb
```

`data/raw/` and `data/processed/` are created automatically at notebook run time via
`Path.mkdir(parents=True, exist_ok=True)` if they don't already exist, so the folders never need
to be created by hand.

### Formats Used and Why

- **CSV → `data/raw/`**: human-readable, universally compatible, and a good match for the raw/
  source-of-truth layer where inspectability matters more than performance. Downside: no native
  dtype preservation (e.g. dates round-trip as strings and must be re-parsed on load).
- **Parquet → `data/processed/`**: columnar, compressed, and preserves dtypes on read/write
  (dates, ints, floats survive the round trip without extra parsing). Better fit for the
  processed/ layer that downstream analysis code consumes, at the cost of not being human
  readable and depending on an engine (`pyarrow`/`fastparquet`).

Both formats are timestamped on write (`sample_YYYYMMDD-HHMMSS.{csv,parquet}`) so repeated runs
don't silently overwrite prior outputs.

### How the Code Reads/Writes Using Env Variables

Paths are never hardcoded. `python-dotenv` loads `.env`, and `DATA_DIR_RAW` /
`DATA_DIR_PROCESSED` are read via `os.getenv(...)` with `data/raw` / `data/processed` as
fallback defaults:

```python
load_dotenv()
RAW = pathlib.Path(os.getenv('DATA_DIR_RAW', 'data/raw'))
PROC = pathlib.Path(os.getenv('DATA_DIR_PROCESSED', 'data/processed'))
RAW.mkdir(parents=True, exist_ok=True)
PROC.mkdir(parents=True, exist_ok=True)
```

`.env` in this folder contains:

```
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

On top of the direct save/load cells, the notebook implements two reusable utilities:

- **`write_df(df, path)`** — routes to `to_csv`/`to_parquet` based on the file suffix
  (`detect_format`), creates any missing parent directories before writing, and raises a clear
  `RuntimeError("Parquet engine not available. Install pyarrow or fastparquet.")` if no Parquet
  engine is installed.
- **`read_df(path)`** — same suffix-based routing for loading, with the same clear error if a
  Parquet engine is missing. CSV loads auto-parse a `date` column back to `datetime64` when
  present, so CSV and Parquet round-trips produce comparable dtypes.

### Validation

A small `validate_loaded(original, reloaded)` helper checks, after every reload:
- `shape_equal` — row/column counts match the original DataFrame
- `date_is_datetime` — the `date` column reloads as `datetime64`
- `price_is_numeric` — the `price` column reloads as a numeric dtype

All three checks pass for both the direct CSV/Parquet save-and-reload and the `write_df`/
`read_df` utility round-trips (see notebook Sections 3 and 4 for the printed results). The
utilities section also demonstrates `write_df` auto-creating a missing nested directory and
`detect_format` rejecting an unsupported file suffix with a clear `ValueError`.

### Assumptions

- The sample dataset (20 rows of synthetic daily `AAPL`-like prices) is small enough that
  format choice doesn't materially affect performance; the format distinction here is about
  fidelity (dtype preservation) and audience (human-readable raw vs. machine-consumed processed),
  not speed.
- `pyarrow` is installed in this environment, so the Parquet path is exercised end-to-end rather
  than only exercising the fallback error message.
