# =========================================================
# NEXUS DIGITAL CRM DASHBOARD
# Streamlit dashboard for lead pipeline analysis
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

# Configure the Streamlit page
# wide layout gives more horizontal space for charts
st.set_page_config(
    page_title="Nexus Digital CRM Dashboard",
    layout="wide"
)

# Dashboard title
st.title("Nexus Digital CRM Dashboard")

# Short description for the viewer
st.markdown(
    "Interactive dashboard for monitoring lead performance, "
    "sales efficiency, customer engagement, and revenue quality."
)


# =========================================================
# LOAD DATA
# =========================================================

# Load CRM lead dataset
DATA_PATH = Path(__file__).parent / "leads_data.csv"
df = pd.read_csv(DATA_PATH)

# Convert date columns from text into datetime format
# dayfirst=True is used because the source dates are DD/MM/YYYY
df["created_date"] = pd.to_datetime(
    df["created_date"],
    dayfirst=True,
    errors="coerce"
)

df["last_activity_date"] = pd.to_datetime(
    df["last_activity_date"],
    dayfirst=True,
    errors="coerce"
)

# Create time-based columns for filtering and trend analysis
df["month"] = df["created_date"].dt.month
df["quarter"] = df["created_date"].dt.quarter

# Calculate sales cycle length in days
df["sales_cycle_days"] = (
    df["last_activity_date"] - df["created_date"]
).dt.days


# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("Dashboard Filters")

# Month filter
selected_months = st.sidebar.multiselect(
    "Month",
    options=sorted(df["month"].dropna().unique()),
    default=sorted(df["month"].dropna().unique())
)

# Quarter filter
selected_quarters = st.sidebar.multiselect(
    "Quarter",
    options=sorted(df["quarter"].dropna().unique()),
    default=sorted(df["quarter"].dropna().unique())
)

# Lead source filter
selected_sources = st.sidebar.multiselect(
    "Lead Source",
    options=sorted(df["lead_source"].dropna().unique()),
    default=sorted(df["lead_source"].dropna().unique())
)

# Sales representative filter
selected_reps = st.sidebar.multiselect(
    "Sales Representative",
    options=sorted(df["assigned_rep"].dropna().unique()),
    default=sorted(df["assigned_rep"].dropna().unique())
)

# Apply all selected filters to the dataframe
filtered_df = df[
    (df["month"].isin(selected_months)) &
    (df["quarter"].isin(selected_quarters)) &
    (df["lead_source"].isin(selected_sources)) &
    (df["assigned_rep"].isin(selected_reps))
]

# =========================================================
# EMPTY FILTER HANDLING
# =========================================================

if filtered_df.empty:
    st.warning("No data matches the selected filters. Please adjust the filters.")
    st.stop()


# =========================================================
# KPI CALCULATIONS
# =========================================================

# Total number of leads after filters
total_leads = len(filtered_df)

# Number of won leads
won_leads = (filtered_df["status"] == "Won").sum()

# Number of lost leads
lost_leads = (filtered_df["status"] == "Lost").sum()

# Lead-to-win rate
win_rate = (won_leads / total_leads * 100) if total_leads > 0 else 0

# Filter only won deals
won_df = filtered_df[filtered_df["status"] == "Won"]

# Average value of closed-won deals
avg_deal_value = won_df["deal_value"].mean() if len(won_df) > 0 else 0

# Average response time
# Important: despite the column name, this metric is measured in hours
avg_response_time = (
    filtered_df["days_to_first_contact"].mean()
    if total_leads > 0
    else 0
)

# Average sales cycle in days
avg_sales_cycle = (
    filtered_df["sales_cycle_days"].mean()
    if total_leads > 0
    else 0
)


# =========================================================
# KPI CARDS
# =========================================================

st.markdown("---")
st.header("Executive KPI Overview")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Total Leads", f"{total_leads:,}")
kpi2.metric("Win Rate", f"{win_rate:.2f}%")
kpi3.metric("Avg Won Deal Value", f"${avg_deal_value:,.0f}")
kpi4.metric("Avg Response Time", f"{avg_response_time:.1f} hrs")

kpi5, kpi6, kpi7, kpi8 = st.columns(4)

kpi5.metric("Won Deals", f"{won_leads:,}")
kpi6.metric("Lost Deals", f"{lost_leads:,}")
kpi7.metric("Avg Sales Cycle", f"{avg_sales_cycle:.1f} days")
kpi8.metric(
    "Revenue per Lead",
    f"${(won_df['deal_value'].sum() / total_leads):,.0f}"
    if total_leads > 0
    else "$0"
)


# =========================================================
# VISUALIZATION 1 — SALES FUNNEL
# =========================================================

# Define business order for funnel stages
funnel_order = [
    "New",
    "Contacted",
    "Qualified",
    "Proposal",
    "Negotiation",
    "Won",
    "Lost"
]

# Count leads per funnel stage
funnel_data = (
    filtered_df["status"]
    .value_counts()
    .reindex(funnel_order, fill_value=0)
    .reset_index()
)

funnel_data.columns = ["status", "count"]

# Create bar chart for funnel stage distribution
fig_funnel = px.bar(
    funnel_data,
    x="status",
    y="count",
    title="Lead Distribution by Funnel Stage",
    labels={
        "status": "Funnel Stage",
        "count": "Number of Leads"
    }
)


# =========================================================
# VISUALIZATION 2 — LEAD SOURCE PERFORMANCE
# =========================================================

# Group leads by acquisition channel
source_perf = (
    filtered_df.groupby("lead_source")
    .agg(
        total_leads=("lead_id", "count"),
        won_leads=("status", lambda x: (x == "Won").sum())
    )
    .reset_index()
)

# Calculate conversion rate per source
source_perf["conversion_rate"] = (
    source_perf["won_leads"] / source_perf["total_leads"] * 100
)

# Create bar chart
fig_source = px.bar(
    source_perf,
    x="lead_source",
    y="conversion_rate",
    title="Conversion Rate by Lead Source",
    labels={
        "lead_source": "Lead Source",
        "conversion_rate": "Conversion Rate (%)"
    }
)


# =========================================================
# VISUALIZATION 3 — MONTHLY CONVERSION TREND
# =========================================================

# Group by month
monthly_perf = (
    filtered_df.groupby("month")
    .agg(
        total_leads=("lead_id", "count"),
        won_leads=("status", lambda x: (x == "Won").sum())
    )
    .reset_index()
)

# Calculate monthly conversion rate
monthly_perf["conversion_rate"] = (
    monthly_perf["won_leads"] / monthly_perf["total_leads"] * 100
)

# Create line chart
fig_month = px.line(
    monthly_perf,
    x="month",
    y="conversion_rate",
    markers=True,
    title="Monthly Conversion Rate",
    labels={
        "month": "Month",
        "conversion_rate": "Conversion Rate (%)"
    }
)

# =========================================================
# VISUALIZATION 4 — LOST DEAL REASONS
# =========================================================

lost_df = filtered_df[filtered_df["status"] == "Lost"]

if lost_df.empty:
    fig_lost = None
else:
    lost_reason_counts = (
        lost_df["lost_reason"]
        .value_counts()
        .reset_index()
    )

    lost_reason_counts.columns = ["lost_reason", "count"]

    fig_lost = px.pie(
        lost_reason_counts,
        names="lost_reason",
        values="count",
        title="Lost Deal Reasons"
    )


# =========================================================
# VISUALIZATION 5 — SALES REP PERFORMANCE
# =========================================================

# Group by sales rep
rep_perf = (
    filtered_df.groupby("assigned_rep")
    .agg(
        total_leads=("lead_id", "count"),
        won_leads=("status", lambda x: (x == "Won").sum())
    )
    .reset_index()
)

# Calculate conversion rate per rep
rep_perf["conversion_rate"] = (
    rep_perf["won_leads"] / rep_perf["total_leads"] * 100
)

# Create bar chart
fig_rep = px.bar(
    rep_perf,
    x="assigned_rep",
    y="conversion_rate",
    title="Conversion Rate by Sales Rep",
    labels={
        "assigned_rep": "Sales Representative",
        "conversion_rate": "Conversion Rate (%)"
    }
)


# =========================================================
# VISUALIZATION 6 — INDUSTRY PERFORMANCE
# =========================================================

# Group by industry
industry_perf = (
    filtered_df.groupby("industry")
    .agg(
        total_leads=("lead_id", "count"),
        won_leads=("status", lambda x: (x == "Won").sum()),
        avg_deal_value=("deal_value", "mean")
    )
    .reset_index()
)

# Calculate conversion rate
industry_perf["conversion_rate"] = (
    industry_perf["won_leads"] / industry_perf["total_leads"] * 100
)

# Create bubble chart
# X = conversion rate
# Y = average deal value
# Bubble size = lead volume
fig_industry = px.scatter(
    industry_perf,
    x="conversion_rate",
    y="avg_deal_value",
    size="total_leads",
    hover_name="industry",
    title="Industry Performance: Conversion vs Deal Value",
    labels={
        "conversion_rate": "Conversion Rate (%)",
        "avg_deal_value": "Average Deal Value (USD)",
        "total_leads": "Total Leads"
    }
)


# =========================================================
# DASHBOARD LAYOUT
# =========================================================

st.markdown("---")
st.header("Pipeline Overview")

left_col, right_col = st.columns(2)

with left_col:
    st.plotly_chart(fig_funnel, use_container_width=True)

with right_col:
    st.plotly_chart(fig_source, use_container_width=True)


st.markdown("---")
st.header("Trends & Loss Analysis")

left_col, right_col = st.columns(2)

with left_col:
    st.plotly_chart(fig_month, use_container_width=True)

with right_col:
    if fig_lost is not None:
        st.plotly_chart(fig_lost, use_container_width=True)
    else:
        st.info("No lost deals for the selected filters.")


st.markdown("---")
st.header("Team & Segment Performance")

left_col, right_col = st.columns(2)

with left_col:
    st.plotly_chart(fig_rep, use_container_width=True)

with right_col:
    st.plotly_chart(fig_industry, use_container_width=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")
st.caption(
    "Dashboard built with Streamlit, Pandas, and Plotly. "
    "Filters update all KPIs and visualizations dynamically."
)