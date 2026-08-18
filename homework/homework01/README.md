# Visa/Mastercard Pairs Trading Strategy
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Statistical arbitrage desks running market-neutral pairs strategies need to continuously verify that the economic relationships underlying their pairs still hold, since a cointegrated pair that breaks down can turn a market-neutral position into a directional bet without warning. The problem that this project addresses is whether the historically cointegrated relationship between Visa and Mastercard remains stable enough to support a rules-based pairs trading strategy, and if so, whether the strategy generates positive risk-adjusted returns after realistic transaction costs. The primary stakeholder is a Portfolio Manager deciding whether to allocate capital to this pair; the user monitoring the position day-to-day is a quant analyst. The useful answer is predictive and strategy-oriented: a daily long/short/flat signal derived from the spread's z-score, supported by a backtest reporting Sharpe ratio, maximum drawdown, and turnover after transaction costs.

## Stakeholder & User
- **Stakeholder (decides):** Portfolio Manager running a market-neutral / stat-arb book, who decides whether to allocate capital to the Visa/Mastercard pair.
- **User (operates the output):** Quant analyst who monitors the spread daily and flags entry/exit signals for the PM.
- **Timing:** Decisions are made daily, based on the current spread z-score and cointegration status.

## Useful Answer & Decision
- **Type:** Predictive / strategy-oriented (not purely descriptive or diagnostic).
- **Metric/artifact:** Daily long/short/flat signal derived from the spread's z-score, plus a cointegration status flag (intact vs. showing signs of breakdown).
- **Supporting evidence:** Backtest report with Sharpe ratio, maximum drawdown, and turnover after realistic transaction costs.
- **Decision supported:** Enter, hold, or exit the pairs position within the stat-arb book.

## Assumptions & Constraints
- The Visa/Mastercard spread is assumed to be stationary and mean-reverting over the sample period.
- Sufficient liquidity exists in both names to enter/exit positions without material slippage.
- Position sizing assumes a realistic capital allocation limit (capacity constraint), consistent with the practical limits discussed in the ETF mini-case.
- Transaction cost estimates are approximate and may understate real-world costs (bid-ask spread, market impact).
- Historical price relationships are assumed to reflect a genuine, ongoing economic link (shared exposure to consumer payment volume), not a coincidental correlation.

## Known Unknowns / Risks
- **Cointegration breakdown:** The Visa/Mastercard relationship could weaken or break down due to a regulatory, competitive, or business-model shift (e.g., new entrants, regulatory action on interchange fees).
- **Regime changes:** Broader market regime shifts (rate environment, risk sentiment) could disrupt the historical spread behavior even if the underlying business relationship holds.
- **Cost drift:** Real transaction costs may differ from assumed costs, especially during periods of stress or lower liquidity, eroding backtested returns.
- **Benchmark/comparison mismatch:** Care is needed to ensure backtested performance is judged against an appropriate risk-adjusted benchmark, not just raw returns.
- **Monitoring plan:** Re-test cointegration and re-estimate the spread model on a rolling basis to catch relationship breakdown early rather than after losses accumulate.

## Lifecycle Mapping
- **Goal:** Inform daily stat-arb allocation decisions for the Visa/Mastercard pair → **Stage:** Problem Framing & Scoping (Stage 01) → **Deliverable:** Scoping paragraph + stakeholder memo + repo skeleton.
- **Goal:** Confirm the pair is still statistically tradeable → **Stage:** (future) Data & Modeling → **Deliverable:** Cointegration test results + spread model.
- **Goal:** Validate strategy profitability → **Stage:** (future) Backtesting & Evaluation → **Deliverable:** Backtest report (Sharpe, drawdown, turnover) after transaction costs.

## Repo Plan
`data/`, `src/`, `notebooks/`, `docs/`, `model/`, `reports/`
- `data/raw/` — raw price history for Visa and Mastercard
- `data/processed/` — cleaned/aligned price series, computed spread
- `src/` — reusable functions (cointegration tests, z-score/signal generation, backtest engine)
- `notebooks/` — exploratory analysis and backtesting notebooks
- `model/` — serialized model objects and strategy parameters
- `reports/` — backtest results, performance metrics, and analysis reports
- `docs/` — stakeholder memo and this README
- **Cadence:** Repo updated as each stage's deliverable is completed; strategy signals (once built) would refresh daily.
