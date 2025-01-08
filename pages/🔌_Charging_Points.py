import streamlit as st
import utils
import plotly.express as px
import plotly.graph_objects as go

# Load data
ev_charging_df = utils.load_charging_points_data()

# Page layout
st.title("🔌 Charging Points")

# Charging Points by Region Section
st.subheader("Charging Points by Region")

# Region filter
selected_region = st.selectbox(
    "Select Region",
    options=sorted(ev_charging_df['region'].unique()),
    index=sorted(ev_charging_df['region'].unique()).index("World")
)

# Filtered bar chart
filtered_data = ev_charging_df[ev_charging_df['region'] == selected_region]
fig_bar = px.bar(
    filtered_data,
    x='year',
    y='value',
    title=f'Charging Points Growth in {selected_region}'
)
st.plotly_chart(fig_bar)


# Get latest year data
latest_year = ev_charging_df['year'].max()

# Top Charging Points by Country Section
st.subheader(f"Top Charging Points by Country {latest_year}")

top_charging_data = utils.get_top_sales_by_country(ev_charging_df, year=latest_year)

col1, col2 = st.columns(2)

with col1:
    # Pie chart
    fig_pie = px.pie(
        top_charging_data,
        values='value',
        names='region',
        title='Distribution by Region'
    )
    st.plotly_chart(fig_pie)

with col2:
    # Data table
    st.dataframe(
        top_charging_data,
        column_config={
            "region": "Region",
            "value": "Number of Points",
            "percentage": st.column_config.ProgressColumn(
                "Share of Total",
                format="%.1f%%",
                min_value=0,
                max_value=100,
            ),
        },
        hide_index=True
    )

# Growth Trends Section
st.subheader("Growth Trends by Region")

# Region selection
selected_regions = st.multiselect(
    "Select Regions",
    options=sorted(ev_charging_df['region'].unique()),
    default=sorted(ev_charging_df['region'].unique())[:3]
)

# Bar chart for multiple regions
trend_data = ev_charging_df[ev_charging_df['region'].isin(selected_regions)]
fig_trends = px.bar(
    trend_data,
    x='year',
    y='value',
    color='region',
    title='Charging Points Growth Trends by Region',
    barmode='group'
)
st.plotly_chart(fig_trends)

