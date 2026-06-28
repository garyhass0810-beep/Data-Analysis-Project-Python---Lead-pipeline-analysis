# Data Analysis Project — CRM Lead Pipeline Analysis

## Project Overview

This project analyzes a CRM lead pipeline dataset for **Nexus Digital**, a B2B SaaS company managing inbound and outbound sales leads.

The goal of this analysis was to identify performance bottlenecks across the sales funnel, evaluate lead quality, measure revenue efficiency, and recommend actionable KPIs for business decision-makers.

This project simulates the work of a real-world **Data Analyst / Revenue Operations Analyst**, combining exploratory data analysis (EDA), KPI design, and interactive dashboard development.

---
## Live Dashboard

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://data-analysis-project-python---lead-pipeline-analysis-zek5yg2u.streamlit.app/)

🚀 Explore the interactive dashboard here:
https://data-analysis-project-python---lead-pipeline-analysis-zek5yg2u.streamlit.app/

---
## Business Objectives

The analysis focused on answering key business questions:

* Which lead sources generate the highest conversion rates?
* Which industries and company sizes produce the most valuable deals?
* What factors influence conversion performance?
* Where are leads being lost in the sales funnel?
* Which KPIs should management monitor regularly?

---

## Dataset

The dataset contains **600 CRM leads** with sales lifecycle information, including:

* Lead source
* Industry
* Company size
* Lead score
* Sales representative
* Deal value
* Sales status
* Lost deal reason
* Created date
* First contact timing
* Last activity date

---

## Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Plotly**
* **Jupyter Notebook**
* **Streamlit**
* **Git / GitHub**

---

# Analysis Scope

## Part 1 — Exploratory Data Analysis (EDA)

Performed full exploratory analysis including:

* Data cleaning & preprocessing
* Missing value inspection
* Sales funnel analysis
* Lead source performance analysis
* Industry segmentation
* Company size segmentation
* Sales representative performance
* Lost deal reason analysis
* Seasonality & monthly trends
* Lead score effectiveness analysis

---

## Part 2 — KPI Framework

Designed a business KPI framework for ongoing performance monitoring.

Key KPIs include:

* Lead-to-Win Rate
* Average First Response Time
* No Response Loss Rate
* Average Won Deal Value
* Sales Cycle Length
* Revenue per Lead
* Rep Conversion Rate
* High-Score Lead Conversion Rate

---

## Part 3 — Interactive Dashboard (Streamlit)

An interactive dashboard was built using **Streamlit**, **Pandas**, and **Plotly** to transform the notebook analysis into a business-friendly decision-making tool.

The dashboard enables users to dynamically explore CRM performance through interactive filters and real-time KPI recalculations.

### Dashboard Features

Interactive filtering by:

* Lead source
* Industry
* Company size
* Sales representative

Executive KPI cards displaying:

* Total Leads
* Win Rate
* Average Won Deal Value
* Average Response Time

Interactive visualizations:

* Sales Funnel Distribution
* Lead Source Conversion Performance
* Monthly Conversion Trends
* Lost Deal Reason Analysis
* Sales Representative Performance
* Industry Revenue Comparison

### Business Value

The dashboard enables leadership teams to:

* Monitor pipeline health in real time
* Identify funnel bottlenecks faster
* Compare channel performance dynamically
* Detect underperforming sales segments
* Support data-driven operational decisions

---

## Key Findings

### 1. Lead-to-Win Rate is Low

Overall conversion from lead to customer was only **8.33%**, indicating significant funnel leakage.

### 2. Response Speed Matters

Leads contacted faster showed better conversion performance, making response time a critical leading indicator.

### 3. No Response is the Biggest Loss Driver

**30.8%** of lost deals were caused by lack of customer response, making it the largest preventable loss category.

### 4. Enterprise Clients Generate Highest Revenue

Enterprise customers produced the highest average deal values but also had longer sales cycles.

### 5. Strong Performance Variance Between Sales Reps

Conversion rates varied significantly across sales representatives, suggesting coaching opportunities and process inconsistencies.

---

## Business Recommendations

Based on the analysis, recommended actions include:

* Improve lead response SLA
* Prioritize high-score leads
* Increase focus on high-value enterprise accounts
* Reduce no-response losses with automated follow-ups
* Monitor KPI dashboard for ongoing optimization

---

## Repository Structure

```bash
.
├── .gitignore
├── dashboard.py
├── leads_data.csv
├── miniproject.ipynb
├── requirements.txt
└── README.md
```

---

## Future Improvements

Planned next steps:

* Build predictive lead scoring model
* Add conversion probability forecasting
* Automate executive reporting
* Enhance dashboard with advanced business insights

---

## Author

**Gary Hass**
Business Process Specialist at Samsung | Aspiring Data Analyst

Focused on analytics, business intelligence, process optimization, and data-driven decision making.
