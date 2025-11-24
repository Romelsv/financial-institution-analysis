# Financial Analysis Scorecard Guide (Beginner-Friendly)

## What This Project Does (Plain English)
- Goal: judge whether a U.S. public company looks financially healthy and reasonably priced.
- Data: audited financials from SEC EDGAR + market/price data from Alpha Vantage (both compliant and free).
- Output (phase 1 focus): clean, validated financial fields and accurate metrics. Visual scoring (traffic lights, dashboards) comes later once data quality and calculations are solid.

## Why Each Statement/Data Source Matters
- Balance Sheet (what the company owns/owes today): used for liquidity (bill-paying ability) and leverage (debt risk) checks.
- Income Statement (sales and profits): used for margins, return on equity/capital, and interest coverage (can profits pay interest?).
- Cash Flow Statement (cash in/out): used to see if profits become cash; fuels dividends, buybacks, reinvestment.
- Market Data (price, shares, debt, cash): tells us what investors pay vs. what the business earns/owns (valuation multiples).
- Peer Info (industry/sector): adds context; a "good" margin in retail may be weak in software.

## Core Metrics (Meaning + Why Investors Use Them)
- Liquidity (near-term survival)
  - Current Ratio = Current Assets / Current Liabilities
  - Quick Ratio = (Current Assets - Inventory) / Current Liabilities
  - Cash Ratio = Cash / Current Liabilities
  - Why: Companies fail from cash crunches even when profitable on paper.
- Leverage (debt risk)
  - Debt/Equity; Debt/EBITDA; Interest Coverage = EBIT / Interest Expense
  - Why: Debt magnifies gains/losses; weak coverage signals distress risk.
- Profitability (business quality)
  - Gross/Operating/Net Margins; ROE; ROIC
  - Why: Margins show pricing power/cost control; ROE/ROIC show capital efficiency.
- Cash Flow (earnings quality)
  - Free Cash Flow (FCF) = Operating CF - CapEx; FCF Margin = FCF / Revenue
  - Why: Cash is harder to manipulate; funds dividends, buybacks, growth.
- Valuation (price vs. fundamentals)
  - P/E; P/S; EV/EBITDA; P/B
  - Why: Overpaying hurts returns; these anchor price to earnings, sales, assets, or enterprise value.
- Credit Risk
  - Altman Z-Score = 1.2*(Working Capital/Total Assets) + 1.4*(Retained Earnings/Total Assets) + 3.3*(EBIT/Total Assets) + 0.6*(Market Cap/Total Liabilities) + 1.0*(Sales/Total Assets)
  - Why: Empirical early-warning model for bankruptcy risk.
- Peer Comparison
  - Percentile ranks vs. sector for each metric
  - Why: Benchmarks strengths/weaknesses; avoids judging in isolation.

## Industry References (widely used standards)
- CFA Institute curriculum: liquidity, leverage, profitability, cash flow, and valuation ratios are core topics in "Financial Reporting and Analysis" and "Equity Valuation".
- McKinsey & Company, "Valuation": uses EV/EBITDA, P/E, P/S, P/B, ROIC, FCF as standard diagnostics and DCF inputs.
- Aswath Damodaran (NYU), "Investment Valuation" and online notes: standardizes EV/EBITDA, P/E, P/S, ROE/ROIC, free cash flow.
- Altman Z-Score: Edward Altman, Journal of Finance (1968); still referenced in credit/risk models and rating-agency style analysis.
- Quick Ratio, Current Ratio, Interest Coverage: appear in Moody's/S&P-style credit frameworks and bank loan covenants.
- SEC EDGAR: authoritative source of audited filings; Alpha Vantage: common licensed API for prototyping and education.

## Beginner-Friendly Build Path (Data + Metrics First)
1) Fetch data: SEC company facts (financials) + Alpha Vantage (price/market cap); cache responses to respect rate limits.
2) Normalize: choose latest 10-K values, ensure USD, map consistent tags (e.g., RevenueFromContractWithCustomerExcludingAssessedTax for ASC 606 revenue).
3) Field extraction: revenue, EBIT, net income, total debt, equity, cash, current assets/liabilities, interest, operating CF, CapEx. Add validation (missing/zero checks).
4) Compute metrics: implement the formulas above as small functions with docstrings explaining meaning and use; include divide-by-zero and missing-data guards.
5) Verify accuracy: spot-check computed metrics against a trusted source (10-K totals or a finance site) for a few tickers.
6) Add peer context: pick 3-5 peers; compute percentiles to show relative strength/weakness.
7) Only after metrics are trusted: layer on traffic-light scoring and dashboard/HTML if desired.

## Checklist (step-by-step)
- [ ] Set up env: virtualenv, install pandas, requests, python-dotenv; add SEC User-Agent and ALPHAVANTAGE_API_KEY in .env.
- [ ] Write fetchers: Alpha Vantage (quote/overview) and SEC (CIK lookup, company facts); add simple caching.
- [ ] Parse & normalize: extract key fields (revenue, EBIT, net income, total debt, equity, cash, current assets/liabilities, interest, operating CF, CapEx); ensure USD and latest 10-K.
- [ ] Implement metrics: liquidity, leverage, profitability, cash flow, valuation, Altman Z; handle divide-by-zero/missing safely.
- [ ] Validate: compare a few metrics to a trusted source to confirm accuracy.
- [ ] Peer view: select peers, compute percentiles to benchmark.
- [ ] (Later) Add thresholds/traffic lights and dashboard once metrics are stable.
- [ ] Document: keep short explanations of each metric's meaning and data source for portfolio clarity.
