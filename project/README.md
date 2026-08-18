# Visa/Mastercard Pairs Trading Strategy — Project

Cumulative course project, carried across the whole semester. Started in Stage 01
(problem framing) and built out stage by stage; see [docs/problem-framing-memo.md](docs/problem-framing-memo.md)
for the full scoping memo (problem statement, stakeholder, assumptions, risks, lifecycle mapping).

## Setup
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and fill in real values (`.env` is gitignored, never commit it).
3. Open `notebooks/project_pipeline.ipynb` and run the setup cell at the top before anything else.

## Structure
- `data/raw/` — inputs, direct and unedited from the source
- `data/processed/` — anything derived from raw data by code (deletable/re-creatable)
- `notebooks/` — project notebooks (`project_pipeline.ipynb` is the single running notebook, started Stage 04)
- `src/` — reusable functions imported by the notebook
- `reports/` — deliverables for a reader; `reports/images/` holds saved figures
- `model/` — saved model objects
- `docs/` — internal design notes (memos, personas, assumptions)
