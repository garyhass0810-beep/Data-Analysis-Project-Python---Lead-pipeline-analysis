# Nexus Lead Analytics

Lead pipeline analysis for **Nexus Digital** (2024 CRM data). This project identifies sales funnel bottlenecks, evaluates acquisition channel performance, and surfaces actionable recommendations for conversion and revenue growth.

---

## Project Overview

The analysis covers:

- **Funnel analysis** — stage distribution, drop-off, and win rate
- **Channel performance** — lead volume, conversion rate, and revenue by source
- **Campaign deep dive** — campaign-level conversion and realized revenue
- **Sales rep performance** — conversion, response time, and deal value by rep
- **KPI framework** — business metrics for ongoing performance monitoring
- **Interactive dashboard** — Streamlit-based analytics dashboard for dynamic exploration

## Dashboard Preview

This project includes a fully interactive Streamlit dashboard featuring:

- Executive KPI cards
- Sales funnel analysis
- Lead source performance
- Monthly conversion trends
- Lost deal breakdown
- Sales rep performance
- Industry benchmarking
- [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://data-analysis-project-python---lead-pipeline-analysis-zek5yg2u.streamlit.app/)

### Live Dashboard
 Explore the interactive dashboard here:  
https://data-analysis-project-python---lead-pipeline-analysis-zek5yg2u.streamlit.app/

## Key Business Questions

This project aims to answer:

- Which lead sources generate the highest conversion rates?
- Where are leads dropping off in the sales funnel?
- Which industries and company sizes produce the most valuable deals?
- Which sales reps perform best?
- What KPIs should management monitor continuously?

---

## Files

| File | Description |
|------|-------------|
| `miniproject.ipynb` | Full analysis notebook with visualizations and business insights |
| `dashboard.py` | Interactive Streamlit dashboard |
| `leads_data.csv` | 2024 lead pipeline dataset (600+ records) |

---

## Tech Stack

- Python 3
- pandas
- NumPy
- matplotlib
- Plotly
- Streamlit
- Jupyter Notebook
- Git / GitHub

---

## Interactive Dashboard

The project includes an interactive **Streamlit dashboard** with:

- Executive KPI cards
- Sales funnel visualization
- Lead source conversion analysis
- Monthly conversion trends
- Lost deal reason breakdown
- Sales representative performance
- Industry performance comparison

### Run Dashboard Locally

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

---

## Analysis Scope

### Part 1 — Exploratory Data Analysis
- Data cleaning
- Funnel analysis
- Channel performance
- Rep performance
- Segmentation analysis
- Trend analysis

### Part 2 — KPI Framework
Key KPIs designed for management:

- Lead-to-Win Rate
- Average First Response Time
- No Response Loss Rate
- Average Won Deal Value
- Sales Cycle Length
- Revenue per Lead
- Rep Conversion Rate
- High-Score Lead Conversion Rate

### Part 3 — Dashboard Development
Interactive business dashboard built using Streamlit.

---

## Getting Started

### Run Notebook

```bash
pip install pandas numpy matplotlib plotly jupyter
jupyter notebook miniproject.ipynb
```

Run all cells from top to bottom. The notebook loads `leads_data.csv` from the same directory.

---

## Dataset

`leads_data.csv` includes lead demographics, acquisition metadata, funnel status, sales assignment, engagement timing, and deal value fields such as:

- `lead_source`
- `campaign_name`
- `status`
- `assigned_rep`
- `lead_score`
- `days_to_first_contact`
- `deal_value`

---

## Author

**Gary Hass**  
Business Process Specialist @ Samsung | Aspiring Data Analyst  
Python • SQL • Excel • Business Analytics
