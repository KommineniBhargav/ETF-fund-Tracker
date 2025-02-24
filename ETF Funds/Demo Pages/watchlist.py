import streamlit as st
from utils import data_fetcher

def render_watchlist():
    st.header("Watchlist")
    
    # Add to watchlist
    col1, col2 = st.columns([2, 1])
    
    with col1:
        new_symbol = st.text_input("Add Fund to Watchlist").upper()
        if st.button("Add"):
            if new_symbol:
                if data_fetcher.validate_symbol(new_symbol):
                    st.session_state.watchlist.add(new_symbol)
                    st.success(f"Added {new_symbol} to watchlist")
                else:
                    st.error("Invalid fund symbol")
    
    # Display watchlist
    if st.session_state.watchlist:
        watchlist_data = []
        for symbol in st.session_state.watchlist:
            price = data_fetcher.get_current_price(symbol)
            change = data_fetcher.get_daily_change(symbol)
            watchlist_data.append({
                "Symbol": symbol,
                "Price": f"${price:.2f}",
                "Daily Change": f"{change:.2f}%"
            })
        
        st.dataframe(watchlist_data)
        
        if st.button("Clear Watchlist"):
            st.session_state.watchlist.clear()
            st.success("Watchlist cleared")
    else:
        st.info("Your watchlist is empty. Add funds to track them.")
