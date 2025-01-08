import streamlit as st
import utils

# Load data
ev_sales_df = utils.load_sales_data()
ev_charging_df = utils.load_charging_points_data()

# Page layout
st.title("EV Dashboard")
st.subheader("World Summary")

# Expander for data source
with st.expander("About the data"):
    st.write("Data sourced from International Energy Agency (IEA) Global EV Database")

# Metric cards row
col1, col2, col3 = st.columns(3)

# Calculate metrics (you'll need to implement these calculations in utils.py)
current_sales = utils.get_current_year_sales(ev_sales_df)
current_sales_delta = utils.get_sales_delta(ev_sales_df)
sales_growth = utils.get_sales_growth(ev_sales_df)
sales_growth_delta = utils.get_sales_growth_delta(ev_sales_df)
charging_points = utils.get_charging_points(ev_charging_df)
charging_points_delta = utils.get_charging_points_delta(ev_charging_df)

with col1:
    st.metric(
        "Global EV Sales",
        f"{current_sales/1e6:.1f}M",
        f"{current_sales_delta:+.1f}%",
        help="Total EV sales in current year"
    )

with col2:
    st.metric(
        "Sales Growth",
        f"{sales_growth:.1f}M",
        f"{sales_growth_delta:+.1f}%",
        help="Year-over-year sales growth"
    )

with col3:
    st.metric(
        "Charging Points",
        f"{charging_points/1e3:.1f}K",
        f"{charging_points_delta:+.1f}%",
        help="Total public charging points"
    )

# Stacked bar chart
st.subheader("EV Sales by Powertrain Type")
chart_data = utils.prepare_sales_by_powertrain(ev_sales_df)
st.bar_chart(chart_data)
