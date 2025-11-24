# Financial Analysis MVP - Guided Learning Blueprint

## 1. Objective and Vision
- Purpose: build an automated, institution-grade system that evaluates the financial health of U.S. public companies using free, compliant data (SEC EDGAR filings + Alpha Vantage market data).
- Core question: "Is this company financially healthy and worth investing in?" answered through seven dimensions: liquidity, leverage, profitability, cash flow, valuation, credit risk, and peer positioning.
- Deliverable: an investment scorecard (JSON/HTML/PDF) with indicators, top strengths/risks, peer rankings, and a concise investment thesis.
- Portfolio angle: demonstrates financial literacy, data engineering, API integration, and risk-aware analysis that investors and hiring managers expect.

## 2. Guided Build Strategy (Learn by Doing)
1. Environment setup
   - Create a virtual environment and install `pandas`, `requests`, `python-dotenv`, etc.
   - Store `ALPHAVANTAGE_API_KEY` in `.env`; configure a reusable SEC `User-Agent`.
2. Data ingestion layer
   - Alpha Vantage: quote, overview, and other endpoints for price, market cap, shares, beta.
   - SEC EDGAR: company tickers -> CIK, company facts API for income statement, balance sheet, cash flow.
   - Cache raw JSON responses (filesystem or lightweight DB) to manage rate limits and enable reproducibility.
3. Processing and validation layer
   - Normalize units (USD), select latest 10-K observations, map tags (for example, `RevenueFromContractWithCustomerExcludingAssessedTax` for ASC 606 compliance).
   - Implement parsers with unit tests so each required field (revenue, EBIT, total debt, etc.) is extracted or raises a controlled warning.
4. Computation engine
   - Write pure functions for each metric category (see section 3) with docstrings explaining formulas and intuition.
   - Add guardrails for divide-by-zero, missing values, and inconsistent statements.
5. Scoring and interpretation
   - Define threshold bands that map each metric to Red/Yellow/Green (start with textbook defaults, then refine by industry).
   - Aggregate category signals and capture qualitative insights (top strengths, top risks).
6. Peer analysis module
   - Identify industry peers (via SIC/sector data from Alpha Vantage or manual lists).
   - Compute percentile rankings and highlight relative out/under-performance.
7. Presentation layer
   - Output JSON for programmatic use plus a lightweight HTML dashboard (cards, sparklines, table comparing peers).
   - Document architecture, data governance (rate limits, compliance), and testing strategy for portfolio credibility.
8. Quality and learning enhancements
   - Unit/integration tests for parsers and metric calculations.
   - Logging to explain each processing step (useful when teaching or showcasing).
   - Notebook experiments (`notebooks/financial_institution.ipynb`) for exploratory analysis, kept separate from production code.

## 3. Metrics, Data Needs, and Why They Matter
| Category | Metrics (industry standard) | Required data | Investor insight |
| --- | --- | --- | --- |
| Liquidity | Current Ratio = CA/CL; Quick = (CA - Inventory)/CL; Cash Ratio = Cash/CL | Balance sheet: current assets, liabilities, inventory, cash | Can the firm handle short-term obligations? Prevents "profitable but illiquid" bankruptcies. |
| Leverage | Debt/Equity; Debt/EBITDA; Interest Coverage = EBIT/Interest | Balance sheet debt and equity, income statement EBIT and interest | Shows balance sheet risk and ability to service debt during downturns. |
| Profitability | Gross, Operating, Net Margins; ROE = Net Income/Equity; ROIC = NOPAT/Invested Capital | Income statement revenues/profits, equity, invested capital | Reveals competitive advantage, pricing power, capital efficiency (Buffett-style metrics). |
| Cash Flow | Free Cash Flow = OpCF - CapEx; FCF Margin = FCF/Revenue; OCF Margin | Cash flow statement (operating CF, CapEx), revenue | Validates earnings quality; cash cannot be "managed" like accrual earnings. |
| Valuation | P/E = Market Cap/Net Income; P/S = Market Cap/Revenue; EV/EBITDA; P/B | Market data (price, shares, cap), balance sheet (debt, cash, equity), income statement | Determines if investors overpay or underpay relative to fundamentals. |
| Credit Risk | Altman Z (public manufacturing) = 1.2*WC/TA + 1.4*RE/TA + 3.3*EBIT/TA + 0.6*MC/TL + 1.0*Sales/TA | Working capital, retained earnings, EBIT, market cap, total assets, total liabilities, revenue | Early bankruptcy warning; empirically predicts distress up to two years out. |
| Peer Comparison | Percentile ranks vs. industry averages; relative strengths/weaknesses | Same metrics for peer tickers | Numbers need context; a 10% net margin is great for retail, weak for software. |

> Why we gather each data point: every metric ties directly to a risk investors care about (solvency, leverage, profitability, cash conversion, valuation discipline, credit health, and competitive standing). Pulling from audited SEC filings and a licensed market feed ensures credibility and compliance, which is critical for a resume-worthy project.

## 4. Practical Learning Path
1. Extend the notebook: in `notebooks/financial_institution.ipynb`, extract additional SEC facts (total debt, equity, EBIT, interest expense) and compute a full metric set for AAPL to validate formulas.
2. Build normalization helpers: turn the notebook logic into reusable Python modules with tests (for example, `sec.py`, `alpha_vantage.py`, `metrics.py`).
3. Design thresholds: start with textbook cutoffs (Current Ratio <1.0 red, 1-1.5 yellow, >1.5 green) and adjust after reviewing multiple companies.
4. Implement peer module: pick 3-5 peers, compute percentile placements, and narrate the interpretation (what makes the company stand out or lag).
5. Polish presentation: create the scorecard output and write a short README section explaining methodology, limitations, and future enhancements.
6. Document learnings: keep notes on why each metric matters and how it ties back to investment decisions; this also feeds your portfolio write-up or blog post.

## 5. Suggested Next Steps
- Prioritize parser reliability (unit tests plus caching) so you trust the numbers before styling the dashboard.
- Add logging/notebook commentary describing each metric's intuition to cement your understanding.
- Once a single-company pipeline works, expand to a CLI tool (`python -m app.scorecard --ticker AAPL --peers MSFT,GOOGL`) to showcase engineering maturity.

By following this playbook, you will learn the financial concepts, understand why each metric matters, and build a professional-grade portfolio project rooted in industry standards.
