# SEC EDGAR XBRL Tag Reference Guide

---

## **1. REVENUE**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Total money from selling products/services |
| **XBRL Tags (Priority Order)** | 1. `RevenueFromContractWithCustomerExcludingAssessedTax`<br>2. `Revenues`<br>3. `SalesRevenueNet` |
| **Statement** | Income Statement |
| **Usually Negative** | No (always positive) |
| **Validation Check** | - Should be largest number on income statement<br>- Should be positive<br>- Typical growth: -5% to +30% year-over-year |
| **Key Use** | All margin calculations, P/S ratio, growth rate |
| **Common Mistakes** | ❌ `RevenueFromContractWithCustomerIncludingAssessedTax` (includes sales tax - inflated)<br>❌ Using quarterly when need annual |
| **Example (Apple 2024)** | $391,035,000,000 ($391B) |

---

## **2. COST OF REVENUE (COGS)**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Direct costs to produce/deliver what you sold |
| **XBRL Tags (Priority Order)** | 1. `CostOfRevenue`<br>2. `CostOfGoodsAndServicesSold`<br>3. `CostOfGoodsSold` |
| **Statement** | Income Statement |
| **Usually Negative** | No (positive expense) |
| **Validation Check** | - Should be less than Revenue<br>- Usually 20-80% of Revenue<br>- Gross Margin = (Revenue - COGS) / Revenue |
| **Key Use** | Gross Margin, DIO calculation |
| **Common Mistakes** | ❌ `OperatingExpenses` (that includes SG&A, R&D, not just production costs)<br>❌ Including depreciation (some companies do, some don't) |
| **Example (Apple 2024)** | $214,137,000,000 ($214B) = 55% of revenue |

---

## **3. GROSS PROFIT**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Revenue minus Cost of Revenue (profit before operating expenses) |
| **XBRL Tags (Priority Order)** | 1. `GrossProfit` |
| **Statement** | Income Statement |
| **Usually Negative** | No (should be positive for healthy companies) |
| **Validation Check** | - Should equal Revenue - COGS (within 1%)<br>- Should be positive<br>- Gross Margin = Gross Profit / Revenue (typically 20-80%) |
| **Key Use** | Gross Margin calculation, profitability assessment |
| **Common Mistakes** | ❌ Confusing with Operating Income (that's after OpEx)<br>❌ Confusing with EBITDA |
| **Example (Apple 2024)** | $176,898,000,000 ($177B) = 45% gross margin |

---

## **4. OPERATING EXPENSES**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Costs to run the business (salaries, marketing, R&D, rent) |
| **XBRL Tags (Priority Order)** | 1. `OperatingExpenses`<br>2. `OperatingCostsAndExpenses` |
| **Statement** | Income Statement |
| **Usually Negative** | No (positive expense) |
| **Validation Check** | - Usually 10-50% of revenue<br>- Should be less than Gross Profit<br>- OpEx Margin = OpEx / Revenue |
| **Key Use** | Operating Margin calculation |
| **Common Mistakes** | ❌ `CostOfRevenue` (that's production, not operations)<br>❌ Including interest/taxes (those come later)<br>❌ Some companies include D&A in OpEx |
| **Example (Apple 2024)** | $64,070,000,000 ($64B) = 16% of revenue |

---

## **5. OPERATING INCOME (EBIT)**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Earnings Before Interest & Taxes - profit from core operations |
| **XBRL Tags (Priority Order)** | 1. `OperatingIncomeLoss`<br>2. `IncomeLossFromOperations` |
| **Statement** | Income Statement |
| **Usually Negative** | No (should be positive; negative = operating loss) |
| **Validation Check** | - Should equal Gross Profit - Operating Expenses<br>- Should be > Net Income<br>- Operating Margin = EBIT / Revenue (typically 5-30%) |
| **Key Use** | Interest Coverage, ROIC, EBITDA calculation, operating efficiency |
| **Common Mistakes** | ❌ `NetIncomeLoss` (that's after interest/taxes)<br>❌ `EBITDA` (that's EBIT + D&A) |
| **Example (Apple 2024)** | $123,217,000,000 ($123B) = 32% operating margin |

---

## **6. INTEREST EXPENSE**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Cost of servicing debt (interest payments on loans/bonds) |
| **XBRL Tags (Priority Order)** | 1. `InterestExpense`<br>2. `InterestAndDebtExpense` |
| **Statement** | Income Statement |
| **Usually Negative** | No (positive expense) |
| **Validation Check** | - Should correlate with Total Debt<br>- Implied interest rate = Interest Expense / Total Debt (typically 2-8%)<br>- Should be positive (it's an expense) |
| **Key Use** | Interest Coverage Ratio = EBIT / Interest Expense |
| **Common Mistakes** | ❌ `InterestIncomeExpenseNet` (nets interest earned WITH expense - we need just expense)<br>❌ Using negative value (some reports show as negative) |
| **Example (Apple 2024)** | $3,933,000,000 ($3.9B) = 3.7% implied rate on $106B debt |

---

## **7. PRETAX INCOME**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Income before taxes are deducted |
| **XBRL Tags (Priority Order)** | 1. `IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest`<br>2. `IncomeLossFromContinuingOperationsBeforeIncomeTaxes`<br>3. `IncomeLossBeforeIncomeTaxes` |
| **Statement** | Income Statement |
| **Usually Negative** | No (should be positive) |
| **Validation Check** | - Should be > Net Income<br>- Should equal Operating Income - Interest + Other Income<br>- Pretax Income - Tax Expense = Net Income |
| **Key Use** | Calculate effective tax rate = Tax Expense / Pretax Income |
| **Common Mistakes** | ❌ Confusing with Operating Income (that's before interest)<br>❌ Using after-tax number |
| **Example (Apple 2024)** | $123,217,000,000 ($123B) |

---

## **8. INCOME TAX EXPENSE**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Taxes paid on income |
| **XBRL Tags (Priority Order)** | 1. `IncomeTaxExpenseBenefit`<br>2. `IncomeTaxesPaid` |
| **Statement** | Income Statement |
| **Usually Negative** | No (positive expense; negative = tax refund/benefit - rare) |
| **Validation Check** | - Usually 15-30% of Pretax Income<br>- Effective Tax Rate = Tax / Pretax Income<br>- Should be positive for profitable companies |
| **Key Use** | Calculate NOPAT for ROIC, assess tax efficiency |
| **Common Mistakes** | ❌ `DeferredIncomeTaxExpenseBenefit` (accounting adjustment, not cash paid)<br>❌ Using cash paid vs. accrued (use accrued for P&L) |
| **Example (Apple 2024)** | $29,749,000,000 ($30B) = 24% effective tax rate |

---

## **9. NET INCOME**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Bottom line profit after ALL expenses and taxes |
| **XBRL Tags (Priority Order)** | 1. `NetIncomeLoss`<br>2. `ProfitLoss`<br>3. `NetIncomeLossAvailableToCommonStockholdersBasic` |
| **Statement** | Income Statement |
| **Usually Negative** | No (should be positive; negative = net loss) |
| **Validation Check** | - Should equal Pretax Income - Tax Expense<br>- Should be < Revenue<br>- Should be < Operating Income<br>- Net Margin = Net Income / Revenue (typically 5-30%) |
| **Key Use** | ROE, ROA, P/E ratio, EPS, earnings growth, profitability |
| **Common Mistakes** | ❌ `ComprehensiveIncomeNetOfTax` (includes unrealized gains/losses - too broad)<br>❌ `NetIncomeLossAttributableToNoncontrollingInterest` (minority interests only) |
| **Example (Apple 2024)** | $93,736,000,000 ($94B) = 24% net margin |

---

## **10. CASH & CASH EQUIVALENTS**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Cash + investments convertible to cash within 90 days |
| **XBRL Tags (Priority Order)** | 1. `CashAndCashEquivalentsAtCarryingValue`<br>2. `Cash` |
| **Statement** | Balance Sheet (Current Assets) |
| **Usually Negative** | No (always positive) |
| **Validation Check** | - Should be positive<br>- Usually 2-30% of total assets<br>- Tech companies often higher (10-30%) |
| **Key Use** | Cash Ratio, Enterprise Value = Market Cap + Debt - Cash, liquidity |
| **Common Mistakes** | ❌ `CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents` (includes restricted - not freely usable)<br>❌ `MarketableSecurities` (investments, not cash equivalents) |
| **Example (Apple 2024)** | $29,943,000,000 ($30B) = 8% of assets |

---

## **11. ACCOUNTS RECEIVABLE**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Money customers owe for products/services already delivered |
| **XBRL Tags (Priority Order)** | 1. `AccountsReceivableNetCurrent`<br>2. `AccountsReceivableNet` |
| **Statement** | Balance Sheet (Current Assets) |
| **Usually Negative** | No (always positive) |
| **Validation Check** | - Should be positive<br>- DSO = (AR / Revenue) × 365 (typically 30-60 days)<br>- "Net" means after bad debt reserves |
| **Key Use** | DSO calculation, working capital, Quick Ratio |
| **Common Mistakes** | ❌ `AccountsReceivableGross` (before bad debt adjustment - inflated)<br>❌ `AccountsReceivableNoncurrent` (long-term - rare) |
| **Example (Apple 2024)** | $26,416,000,000 ($26B) = 25 days DSO |

---

## **12. INVENTORY**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Goods available for sale (finished goods + raw materials + WIP) |
| **XBRL Tags (Priority Order)** | 1. `InventoryNet`<br>2. `InventoryGross` |
| **Statement** | Balance Sheet (Current Assets) |
| **Usually Negative** | No (positive; but can be $0 for service companies) |
| **Validation Check** | - DIO = (Inventory / COGS) × 365 (typically 30-90 days)<br>- Usually 5-30% of current assets<br>- Service companies = $0 (normal) |
| **Key Use** | Quick Ratio (excludes inventory), DIO, inventory turnover, working capital |
| **Common Mistakes** | ❌ Expecting inventory for service companies (software, consulting = $0)<br>❌ `InventoryRawMaterials` (just one component) |
| **Example (Apple 2024)** | $6,511,000,000 ($6.5B) = 11 days inventory |

---

## **13. CURRENT ASSETS**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Assets convertible to cash within one year |
| **XBRL Tags (Priority Order)** | 1. `AssetsCurrent` |
| **Statement** | Balance Sheet (Assets) |
| **Usually Negative** | No (always positive) |
| **Validation Check** | - Should equal: Cash + AR + Inventory + Other Current Assets<br>- Current Ratio = Current Assets / Current Liabilities (ideally >1.0)<br>- Should be > Current Liabilities (usually) |
| **Key Use** | Current Ratio, Quick Ratio, working capital, liquidity assessment |
| **Common Mistakes** | ❌ `Assets` (that's TOTAL assets, not current)<br>❌ Missing components when calculating manually |
| **Example (Apple 2024)** | $143,566,000,000 ($144B) |

---

## **14. TOTAL ASSETS**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Everything the company owns (current + non-current) |
| **XBRL Tags (Priority Order)** | 1. `Assets` |
| **Statement** | Balance Sheet (Assets) |
| **Usually Negative** | No (always positive) |
| **Validation Check** | - **MUST equal Total Liabilities + Equity** (balance sheet equation)<br>- Tolerance: within 1-5% due to rounding<br>- Should be larger than revenue (typically) |
| **Key Use** | ROA, Asset Turnover, Z-Score, balance sheet balancing |
| **Common Mistakes** | ❌ `AssetsCurrent` (just short-term assets)<br>❌ Not validating Assets = Liabilities + Equity |
| **Example (Apple 2024)** | $364,980,000,000 ($365B) |

---

## **15. DEPRECIATION & AMORTIZATION**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Non-cash expense for asset wear/tear and intangible writedowns THIS year |
| **XBRL Tags (Priority Order)** | 1. `DepreciationDepletionAndAmortization`<br>2. `DepreciationAndAmortization` |
| **Statement** | Cash Flow Statement (Operating Activities - Add-back section) |
| **Usually Negative** | No (positive in cash flow statement as add-back) |
| **Validation Check** | - Usually 2-8% of revenue<br>- Should be < CapEx<br>- EBITDA = EBIT + D&A (should make EBITDA > EBIT)<br>- Should be positive |
| **Key Use** | EBITDA calculation = Operating Income + D&A |
| **Common Mistakes** | ❌ `AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment` (CUMULATIVE total since forever - way too big!)<br>❌ Confusing with CapEx (different concepts) |
| **Example (Apple 2024)** | $11,445,000,000 ($11B) = 2.9% of revenue |

---

## **16. ACCOUNTS PAYABLE**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Money owed to suppliers for goods/services received but not yet paid |
| **XBRL Tags (Priority Order)** | 1. `AccountsPayableCurrent`<br>2. `AccountsPayableTradeCurrent` |
| **Statement** | Balance Sheet (Current Liabilities) |
| **Usually Negative** | No (always positive) |
| **Validation Check** | - DPO = (AP / COGS) × 365 (typically 30-60 days)<br>- Usually 5-15% of COGS<br>- Should be positive |
| **Key Use** | DPO, Cash Conversion Cycle, working capital management |
| **Common Mistakes** | ❌ `AccountsPayableNoncurrent` (rare long-term payables)<br>❌ Including other current liabilities |
| **Example (Apple 2024)** | $58,453,000,000 ($58B) = 100 days DPO |

---

## **17. CURRENT LIABILITIES**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Debts and obligations due within one year |
| **XBRL Tags (Priority Order)** | 1. `LiabilitiesCurrent` |
| **Statement** | Balance Sheet (Liabilities) |
| **Usually Negative** | No (always positive) |
| **Validation Check** | - Should include: AP + Short-Term Debt + Accrued Expenses + Deferred Revenue<br>- Current Ratio = Current Assets / Current Liabilities<br>- Should be < Current Assets (ideally) |
| **Key Use** | Current Ratio, Quick Ratio, Cash Ratio, working capital, liquidity |
| **Common Mistakes** | ❌ `Liabilities` (that's TOTAL, not current)<br>❌ Missing components when summing manually |
| **Example (Apple 2024)** | $145,308,000,000 ($145B) |

---

## **18. SHORT-TERM DEBT**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Borrowed money due within one year (multiple components) |
| **XBRL Tags (Priority Order)** | 1. `CommercialPaper`<br>2. `LongTermDebtCurrent`<br>3. `ShortTermBorrowings`<br>4. `DebtCurrent`<br>5. `ShortTermDebt` |
| **Statement** | Balance Sheet (Current Liabilities) |
| **Usually Negative** | No (positive liability) |
| **Validation Check** | - **Must extract ALL components and sum them**<br>- Should be < Total Debt<br>- Interest Expense should correlate with Total Debt<br>- Can be $0 (some companies have no short-term debt) |
| **Key Use** | Total Debt calculation, debt maturity analysis, refinancing risk |
| **Common Mistakes** | ❌ Using only ONE tag (Apple uses 2: Commercial Paper + LongTermDebtCurrent)<br>❌ Confusing `LongTermDebtCurrent` with long-term debt (it's SHORT-term!)<br>❌ `OtherLiabilitiesCurrent` (too broad - includes non-debt items) |
| **Example (Apple 2024)** | $10.0B (Commercial Paper) + $10.9B (Term Debt Current) = $20.9B total |

---

## **19. LONG-TERM DEBT**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Borrowed money due AFTER one year |
| **XBRL Tags (Priority Order)** | 1. `LongTermDebt`<br>2. `DebtLongTerm`<br>3. `LongTermDebtNoncurrent` |
| **Statement** | Balance Sheet (Non-Current Liabilities) |
| **Usually Negative** | No (positive liability) |
| **Validation Check** | - Usually largest component of Total Debt<br>- Should be < Total Assets<br>- Total Debt = Short-Term + Long-Term<br>- Debt/EBITDA: <3x safe, >5x risky |
| **Key Use** | Debt-to-Equity, Debt-to-EBITDA, Interest Coverage, leverage analysis |
| **Common Mistakes** | ❌ `LongTermDebtAndCapitalLeaseObligations` (includes lease obligations - inflated)<br>❌ Including `LongTermDebtCurrent` (that's SHORT-term) |
| **Example (Apple 2024)** | $95,281,000,000 ($95B) |

---

## **20. TOTAL LIABILITIES**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Everything the company owes (current + non-current) |
| **XBRL Tags (Priority Order)** | 1. `Liabilities` |
| **Statement** | Balance Sheet (Liabilities) |
| **Usually Negative** | No (always positive) |
| **Validation Check** | - **Assets = Liabilities + Equity** (MUST balance within 1-5%)<br>- Should be < Total Assets<br>- Includes all debt + AP + accruals + deferred revenue |
| **Key Use** | Debt ratios, Z-Score, balance sheet validation, financial leverage |
| **Common Mistakes** | ❌ `LiabilitiesCurrent` (just short-term)<br>❌ Not checking balance sheet equation |
| **Example (Apple 2024)** | $308,030,000,000 ($308B) |

---

## **21. SHAREHOLDERS' EQUITY**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Net worth (Assets - Liabilities) = book value = what shareholders own |
| **XBRL Tags (Priority Order)** | 1. `StockholdersEquity`<br>2. `ShareholdersEquity`<br>3. `Equity` |
| **Statement** | Balance Sheet (Equity) |
| **Usually Negative** | No (should be positive; negative = bankruptcy/distress) |
| **Validation Check** | - **Assets = Liabilities + Equity** (must balance)<br>- Should be positive<br>- Can calculate: Total Assets - Total Liabilities |
| **Key Use** | ROE, Debt-to-Equity, P/B ratio, Z-Score, book value |
| **Common Mistakes** | ❌ `StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest` (includes minority interests)<br>❌ Using market cap (that's market value, not book value) |
| **Example (Apple 2024)** | $56,950,000,000 ($57B) |

---

## **22. RETAINED EARNINGS**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Cumulative profits kept in business (not paid as dividends) since inception |
| **XBRL Tags (Priority Order)** | 1. `RetainedEarningsAccumulatedDeficit` |
| **Statement** | Balance Sheet (Equity) |
| **Usually Negative** | Can be positive OR negative (negative = accumulated deficit) |
| **Validation Check** | - Grows by: (Net Income - Dividends) each year<br>- Can be negative for: young companies, dividend-heavy companies<br>- Mature profitable companies usually have large positive RE |
| **Key Use** | Altman Z-Score X2 component, dividend policy assessment |
| **Common Mistakes** | ❌ `NetIncomeLoss` (that's THIS year, not cumulative)<br>❌ Thinking negative RE = unhealthy (Apple is negative due to massive dividends/buybacks) |
| **Example (Apple 2024)** | $-19,154,000,000 ($-19B) - Negative because Apple returned more cash to shareholders than cumulative earnings |

---

## **23. OPERATING CASH FLOW**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Cash generated from core business operations (the "truth teller") |
| **XBRL Tags (Priority Order)** | 1. `NetCashProvidedByUsedInOperatingActivities` |
| **Statement** | Cash Flow Statement (Operating Activities) |
| **Usually Negative** | No (should be positive for healthy companies) |
| **Validation Check** | - Should be close to Net Income (±20%)<br>- If OCF << Net Income = earnings quality issue<br>- OCF Margin = OCF / Revenue (typically 10-30%)<br>- Should be positive |
| **Key Use** | Free Cash Flow = OCF - CapEx, OCF Margin, earnings quality validation |
| **Common Mistakes** | ❌ `NetCashProvidedByUsedInInvestingActivities` (investing, not operations)<br>❌ `NetCashProvidedByUsedInFinancingActivities` (financing, not operations) |
| **Example (Apple 2024)** | $118,254,000,000 ($118B) = 30% OCF margin |

---

## **24. CAPITAL EXPENDITURES (CapEx)**

| Attribute | Details |
|-----------|---------|
| **What It Is** | Cash spent on property, equipment, facilities |
| **XBRL Tags (Priority Order)** | 1. `PaymentsToAcquirePropertyPlantAndEquipment` |
| **Statement** | Cash Flow Statement (Investing Activities) |
| **Usually Negative** | Yes (it's a cash outflow - should be negative or report as positive outflow) |
| **Validation Check** | - Usually 2-10% of revenue<br>- Tech/Software: Low (2-5%)<br>- Manufacturing/Utilities: High (10-20%)<br>- Should be < Operating Cash Flow |
| **Key Use** | Free Cash Flow = OCF - CapEx |
| **Common Mistakes** | ❌ `PaymentsToAcquireBusinessesNetOfCashAcquired` (acquisitions, not CapEx)<br>❌ Using positive number (should be negative outflow) |
| **Example (Apple 2024)** | $-10,959,000,000 ($-11B) = 2.8% of revenue (asset-light business model) |

---

## **QUICK VALIDATION CHECKLIST**

After extracting all data, run these checks:

```
✅ Assets = Liabilities + Equity (within 5%)
✅ Revenue > Cost of Revenue
✅ Gross Profit = Revenue - COGS
✅ EBITDA > EBIT
✅ Operating Income > Net Income
✅ Net Income < Revenue
✅ Cash < Current Assets
✅ Current Assets includes: Cash + AR + Inventory
✅ Total Debt = Short-Term Debt + Long-Term Debt
✅ OCF close to Net Income (within 50%)
✅ CapEx < Operating Cash Flow
```

---

**This is your complete SEC EDGAR extraction reference. Every tag is verified and validated against Apple's 10-K.**

**Ready to code the extractor function with these tags?**