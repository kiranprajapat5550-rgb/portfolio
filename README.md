# Kiran Kumar — Portfolio

Responsive, mobile-friendly portfolio for browser-based reporting tools, operations workflows and approval-based AI concepts.

## Live site

https://kiranprajapat5550-rgb.github.io/portfolio/

## Professional links

- **Portfolio:** https://kiranprajapat5550-rgb.github.io/portfolio/
- **Résumé:** https://kiranprajapat5550-rgb.github.io/portfolio/resume.html
- **LinkedIn:** https://www.linkedin.com/in/kiran-kumar-ai-automation/
- **GitHub profile:** https://github.com/kiranprajapat5550-rgb

## Featured projects

- **Retail Store Cash Flow Dashboard:** [Open demo](samples/retail-store-cash-flow-dashboard.html) · [Fictional sample CSV](samples/retail-store-cash-flow-sample.csv)
- **Python Inventory Analytics:** [Analysis script](scripts/analytics.py) · [Fictional sample CSV](sample-data/python-inventory-analytics-sample.csv) · [Automated tests](tests/test_analytics.py)
- **Advanced Sales Analytics:** [Open demo](samples/advanced-sales-analytics.html)
- **Clinic Booking Automation:** [Open concept](samples/clinic-booking-automation.html)
- **AI Employee Approval Desk:** [Open concept](samples/ai-employee-agent.html)

Portfolio demos are prototypes, not claims of live client deployments. Sample datasets are fictional unless explicitly stated otherwise.

## Interactive tools

- **Advanced Sales Analytics** — upload a CSV to calculate gross/net sales, unique orders, average order value and monthly/category summaries.
- **Inventory Health Checker** — review low/zero stock, expiry windows and long gaps since last movement.
- **Clinic Appointment Tracker** — test appointment references, time-slot overlap checks, status changes and CSV export.
- **AI Employee Approval Desk** — review a simulated proposal queue and export the local audit trail.

Open these from the **Interactive tools** section on the homepage.

## Additional skill labs

- **Social Content Planner** (`tools/social-content-planner.html`) — create a seven-day template-based social content plan and export CSV.
- **On-page SEO Review Checklist** (`tools/seo-review-checklist.html`) — track manual SEO review checks and export a review report.

These are local browser demos. The content planner uses a fixed template library (not live AI generation); the SEO checklist does not crawl pages or predict rankings. Review generated plans and checklist findings before using them.

## Digital marketing campaign lab

- `tools/digital-marketing-campaign-lab.html` — plan campaign objectives, audience, budget and creative angle; enter campaign metrics; calculate CTR, CPC, conversion rate and ROAS; export campaign data to CSV.
- Starter campaign figures are fictional. This is a browser-only demonstration with no live ad-account connection or performance prediction. Keep attribution settings and metric definitions consistent when comparing real campaigns.

## Retail Store Cash Flow Dashboard

- `samples/retail-store-cash-flow-dashboard.html` — responsive portfolio dashboard with cash-flow KPI cards, a daily closing-cash trend, weekly inflow/outflow comparison, weekly summary and expense breakdown.
- **All dashboard figures are fictional sample data**, created for portfolio demonstration. This is a static prototype with no live bank, POS, accounting or store-system connection. Some example KPI values may not reconcile across every displayed section; validate source definitions and totals before operational use.

## Fictional sample CSVs

- `sample-data/sales-sample.csv` — example order lines for the Sales Analytics tool.
- `sample-data/inventory-sample.csv` — example stock rows for the Inventory Health Checker.

The sample data is fictional. Use the **Download sample data** links inside the relevant tools to try them.

## Python inventory analytics

- `scripts/analytics.py` — pandas-based CSV analysis for annual demand, annual usage value, ABC-XYZ segmentation, a simple reorder-point estimate and review flags.
- `sample-data/python-inventory-analytics-sample.csv` — fictional sample rows for trying the script.
- `tests/test_analytics.py` — unit tests for key calculations and invalid inputs.
- `.github/workflows/python-tests.yml` — automated test run on relevant pushes and pull requests.

### Run locally

Install Python 3.10+ and the listed dependency, then run from the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/analytics.py sample-data/python-inventory-analytics-sample.csv --output inventory_analysis.csv
python -m unittest discover -s tests -v
```

The reorder point is a basic estimate: average daily demand × lead time + supplied safety stock. ABC-XYZ thresholds are simple configurable heuristics, not a universal inventory policy. Validate units, seasonality, supplier variability and business rules before using results operationally. Sample rows are fictional.

## Privacy and limitations

The sales and inventory tools process the selected CSV locally in the browser. The appointment tracker and approval desk keep their temporary entries in page memory only. These prototypes do not connect to live business systems, external accounts, clinic calendars or real AI agents. Do not upload sensitive personal, patient, financial or confidential business data. Validate all output before using it for decisions.

## Publish with GitHub Pages

GitHub Actions deploys the repository to GitHub Pages when changes are pushed to `main`. Check the **Actions** tab if the latest update has not appeared yet.

## Project pages

- `samples/advanced-sales-analytics.html`
- `samples/inventory-health-report.html`
- `samples/clinic-booking-automation.html`
- `samples/ai-employee-agent.html`

No credentials or API tokens are included in this repository.
## CEO cash-flow report sample

- `samples/ceo-cash-flow-report.html` — executive summary, KPI cards, weekly summary and management notes.
- `samples/retail-store-cash-flow-sample.csv` — fictional weekly cash-flow figures that can be opened in Excel or another spreadsheet app.
- All figures are fictional demonstration data. No real client, bank, POS, or accounting data is connected.
