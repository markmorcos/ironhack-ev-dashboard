import streamlit as st
import utils
import plotly.express as px
import plotly.graph_objects as go

# Load data
ev_sales_df = utils.load_sales_data()

# Page layout
st.title("📈 EV Sales")

# EV Sales by Region Section
st.subheader("EV Sales by Region")

# Region filter
selected_region = st.selectbox(
    "Select Region",
    options=sorted(ev_sales_df['region'].unique()),
    index=sorted(ev_sales_df['region'].unique()).index("World")
)

# Filtered stacked bar chart
filtered_data = ev_sales_df[ev_sales_df['region'] == selected_region]
fig_stacked = px.bar(
    filtered_data,
    x='year',
    y='value',
    color='powertrain',
    title=f'EV Sales Trend in {selected_region}'
)
st.plotly_chart(fig_stacked)

# Top Sales by Country Section
st.subheader("Top Sales by Country 2023")

# Get latest year data
latest_year = ev_sales_df['year'].max()
top_sales_data = utils.get_top_sales_by_country(ev_sales_df, year=latest_year)

col1, col2 = st.columns(2)

with col1:
    # Pie chart
    fig_pie = px.pie(
        top_sales_data,
        values='value',
        names='region',
        title='Market Share by Region'
    )
    st.plotly_chart(fig_pie)

with col2:
    # Bar chart
    st.dataframe(
        top_sales_data,
        column_config={
            "region": "Region",
            "value": "Sales Volume",
            "percentage": st.column_config.ProgressColumn(
                "Market Share",
                format="%.1f%%",
                min_value=0,
                max_value=100,
            ),
        },
        hide_index=True
    )

# Sales Trends Section
st.subheader("Sales Trends by Region")

# Filters
col1, col2 = st.columns(2)
with col1:
    selected_regions = st.multiselect(
        "Select Regions",
        options=sorted(ev_sales_df['region'].unique()),
        default=sorted(ev_sales_df['region'].unique())[:3]
    )
with col2:
    selected_powertrain = st.selectbox(
        "Select Powertrain",
        options=sorted(ev_sales_df['powertrain'].unique())
    )

# Line chart
trend_data = utils.get_sales_trends(
    ev_sales_df,
    regions=selected_regions,
    powertrain=selected_powertrain
)
fig_trends = px.line(
    trend_data,
    x='year',
    y='value',
    color='region',
    title=f'{selected_powertrain} Sales Trends by Region'
)
st.plotly_chart(fig_trends)
