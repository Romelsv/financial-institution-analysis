# TASKS.md - Fundamental Scorecard Delivery Plan

## Stage 1 - Environment & Repo Skeleton (must be green before Stage 2)
- [x] Create venv; install pandas, requests, python-dotenv.
- [x] Add .env with ALPHAVANTAGE_API_KEY; set SEC User-Agent constant.
- [x] Scaffold folders: src/ingestion, src/parse, src/metrics, src/tests, notebooks/, data/raw.

## Stage 2 - Ingestion (must pass before parsing)
- [ ] SEC: CIK lookup from SEC tickers JSON; fetch company facts JSON with retry + rate-limit sleep; save raw JSON with timestamp.
- [ ] Alpha Vantage: fetch GLOBAL_QUOTE and OVERVIEW; save raw responses with timestamp; add simple file cache.

## Stage 3 - Parsing & Normalization (period-aware, with tag strategy)
- [ ] Define tag priority map per field (e.g., Revenue: RevenueFromContractWithCustomerExcludingAssessedTax > RevenueFromContractWithCustomerIncludingAssessedTax > legacy Revenues; pre-2018 fallback allowed).
- [ ] Parse annual and quarterly facts into rows keyed by: ticker, period_end, fiscal_period (A/Q1/Q2/Q3/Q4), form, units, source_tag.
- [ ] Extract fields: revenue, gross profit, EBIT, net income, operating CF, capex, total debt (short + long), total assets, equity, current assets/liabilities, interest expense, cash.
- [ ] Normalize units to USD; select latest 5 annual and 4-8 quarterly observations where available.
- [ ] Tests: fixtures for pre-2018 and post-2018 to confirm correct revenue tag selection and fallbacks; assert non-negative revenue and sensible scales.

## Stage 4 - Derived Period Views (TTM) (depends on Stage 3)
- [ ] Build TTM calculators for revenue, EBITDA/EBIT, net income, FCF from quarterly data; label results as TTM.
- [ ] Keep annual vs quarterly vs TTM separated and tagged.
- [ ] Tests: fixture-driven checks for TTM math and period alignment.

## Stage 5 - Metric Engine (pure functions) (depends on Stage 4)
- [ ] Liquidity: current, quick, cash ratios.
- [ ] Leverage: debt/equity, debt/EBITDA, interest coverage.
- [ ] Profitability: gross/operating/net margins; ROE; ROIC (NOPAT/Invested Capital approximation).
- [ ] Cash flow: FCF, FCF margin, OCF margin.
- [ ] Valuation: P/E, P/S, EV/EBITDA, P/B (uses latest price + shares + debt/cash snapshot).
- [ ] Credit risk: Altman Z (public manufacturing formula).
- [ ] Tests: handle divide-by-zero/missing gracefully; return None/flag instead of crashing.

## Stage 6 - Data Alignment for Metrics (depends on Stage 5)
- [ ] Align fundamentals (annual/TTM) to a market snapshot date; store period_end + snapshot_date together.
- [ ] Ensure debt/cash and shares/price align to the same valuation date when computing EV/EBITDA, P/E, P/S.

## Stage 7 - Peer Comparison (depends on Stage 6)
- [ ] Input: list of peer tickers + sector.
- [ ] Compute percentiles for each metric; identify top strengths/weaknesses.
- [ ] Tests: deterministic output with fixture data.

## Stage 8 - Validation Pass (depends on Stage 7)
- [ ] Pick 2-3 tickers; compute metrics; spot-check against 10-K values or a trusted finance site.
- [ ] Log discrepancies; adjust tag mappings or parsing if mismatches occur.

## Stage 9 - Outputs (lightweight) (depends on Stage 8)
- [ ] Emit JSON blob with metadata (ticker, period_end, snapshot_date), raw fields, TTM, metrics, peer percentiles.
- [ ] Optional: simple Markdown/console summary. Defer dashboards/traffic lights until data and metrics are trusted.

## Stage 10 - Documentation (final)
- [ ] Update README with data sources, tag strategy (ASC 606 handling), period handling, and limitations.
- [ ] Add "how to run" steps for fetching, parsing, computing metrics.
