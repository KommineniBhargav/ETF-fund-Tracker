import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

from components import portfolio, fund_info, charts, watchlist
from utils import data_fetcher, calculations

st.set_page_config(
    page_title="ETF & Mutual Fund Tracker",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}
if 'watchlist' not in st.session_state:
    st.session_state.watchlist = set()

def main():
    st.title("ETF & Mutual Fund Tracker")
    
    # Main navigation
    tab1, tab2, tab3, tab4 = st.tabs([
        "Portfolio Dashboard", 
        "Fund Explorer",
        "Compare Funds",
        "Watchlist"
    ])
    
    with tab1:
        portfolio.render_portfolio_dashboard()
    
    with tab2:
        fund_info.render_fund_explorer()
    
    with tab3:
        charts.render_fund_comparison()
        
    with tab4:
        watchlist.render_watchlist()

if __name__ == "__main__":
    main()
