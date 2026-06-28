# Nexus Lead Analytics

Lead pipeline analysis for **Nexus Digital** (2024 CRM data). This project identifies sales funnel bottlenecks, evaluates acquisition channel performance, and surfaces actionable recommendations for conversion and revenue growth.

## Project Overview

The analysis covers:

- **Funnel analysis** — stage distribution, drop-off, and win rate
- **Channel performance** — lead volume, conversion rate, and revenue by source
- **Campaign deep dive** — campaign-level conversion and realized revenue
- **Sales rep performance** — conversion, response time, and deal value by rep

## Files

| File | Description |
|------|-------------|
| `miniproject.ipynb` | Full analysis notebook with visualizations and business insights |
| `leads_data.csv` | 2024 lead pipeline dataset (600+ records) |

## Tech Stack

- Python 3
- pandas, NumPy
- matplotlib, seaborn
- Jupyter Notebook

## Getting Started

1. Clone the repository and open the project folder.
2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. Launch the notebook:

   ```bash
   jupyter notebook miniproject.ipynb
   ```

4. Run all cells from top to bottom. The notebook loads `leads_data.csv` from the same directory.

## Dataset

`leads_data.csv` includes lead demographics, acquisition metadata, funnel status, sales assignment, engagement timing, and deal value fields such as:

- `lead_source`, `campaign_name`, `status`, `assigned_rep`
- `lead_score`, `days_to_first_contact`, `deal_value`

## Author

Gary Hass
