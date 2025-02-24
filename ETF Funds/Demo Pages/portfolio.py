import streamlit as st
import pandas as pd
from utils import data_fetcher, calculations

def render_portfolio_dashboard():
    st.header("Portfolio Dashboard")
    
    # Portfolio Management Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Current Holdings")
        if not st.session_state.portfolio:
            st.info("Your portfolio is empty. Add funds to get started!")
        else:
            portfolio_df = pd.DataFrame(st.session_state.portfolio.items(),
                                    columns=['Symbol', 'Shares'])
            
            # Fetch current prices
            for idx, row in portfolio_df.iterrows():
                price = data_fetcher.get_current_price(row['Symbol'])
                portfolio_df.loc[idx, 'Current Price'] = price
                portfolio_df.loc[idx, 'Value'] = price * row['Shares']
            
            st.dataframe(portfolio_df)
            
            # Portfolio Statistics
            total_value = portfolio_df['Value'].sum()
            st.metric("Total Portfolio Value", f"${total_value:,.2f}")
    
    with col2:
        st.subheader("Add Position")
        symbol = st.text_input("Fund Symbol").upper()
        shares = st.number_input("Number of Shares", min_value=0.0, step=0.01)
        
        if st.button("Add to Portfolio"):
            if symbol and shares > 0:
                if data_fetcher.validate_symbol(symbol):
                    st.session_state.portfolio[symbol] = shares
                    st.success(f"Added {shares} shares of {symbol}")
                else:
                    st.error("Invalid fund symbol")
