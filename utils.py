import pandas as pd
import streamlit as st

def load_sales_data():
    ev_sales_url = "https://api.iea.org/evs?parameters=EV%20sales&category=Historical&mode=Cars&csv=true"
    ev_sales_df = pd.read_csv(ev_sales_url)
    return ev_sales_df

def load_charging_points_data():
    ev_charging_points_url = "https://api.iea.org/evs?parameters=EV%20charging%20points&category=Historical&mode=EV&csv=true"
    ev_charging_points_df = pd.read_csv(ev_charging_points_url)
    return ev_charging_points_df

def get_current_year_sales(df):
    """Calculate total EV sales for current year"""
    current_year = df['year'].max()
    return df[df['year'] == current_year]['value'].sum()


def get_sales_delta(df):
    """Calculate year-over-year sales growth"""
    current_year = df['year'].max()
    current = df[df['year'] == current_year]['value'].sum()
    previous = df[df['year'] == current_year - 1]['value'].sum()
    return ((current - previous) / previous) * 100

def get_sales_growth(df):
    """Calculate year-over-year sales growth"""
    current_year = df['year'].max()
    current = df[df['year'] == current_year]['value'].sum()
    previous = df[df['year'] == current_year - 1]['value'].sum()
    return ((current - previous) / previous) * 100

def get_sales_growth_delta(df):
    """Calculate year-over-year sales growth"""
    current_year = df['year'].max()
    current = df[df['year'] == current_year]['value'].sum()
    previous = df[df['year'] == current_year - 1]['value'].sum()
    return ((current - previous) / previous) * 100

def get_charging_points(df):
    """Get current year charging points"""
    current_year = df['year'].max()
    return df[df['year'] == current_year]['value'].sum()

def get_charging_points_delta(df):
    """Get year-over-year charging points growth"""
    current_year = df['year'].max()
    current = df[df['year'] == current_year]['value'].sum()
    previous = df[df['year'] == current_year - 1]['value'].sum()
    return ((current - previous) / previous) * 100

def prepare_sales_by_powertrain(df):
    """Prepare data for stacked bar chart"""
    pivot_data = df.pivot_table(
        index='year',
        columns='powertrain',
        values='value',
        aggfunc='sum'
    ).fillna(0)
    return pivot_data

def get_top_sales_by_country(df, year):
    """Get top sales by country for a specific year"""
    yearly_data = df[df['year'] == year]
    sales_by_region = yearly_data.groupby('region')['value'].sum().reset_index()
    total_sales = sales_by_region['value'].sum()
    sales_by_region['percentage'] = (sales_by_region['value'] / total_sales) * 100
    return sales_by_region.sort_values('value', ascending=False)

def get_sales_trends(df, regions, powertrain):
    """Get sales trends for selected regions and powertrain"""
    mask = (df['region'].isin(regions)) & (df['powertrain'] == powertrain)
    trend_data = df[mask].groupby(['year', 'region'])['value'].sum().reset_index()
    return trend_data

