import streamlit as st
from utils import data_fetcher
import plotly.graph_objects as go

def render_fund_explorer():
    st.header("Fund Explorer")
    
    symbol = st.text_input("Enter Fund Symbol").upper()
    
    if symbol:
        with st.spinner("Fetching fund data..."):
            fund_data = data_fetcher.get_fund_info(symbol)
            
            if fund_data:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Fund Information")
                    st.write(f"Name: {fund_data['longName']}")
                    st.write(f"Category: {fund_data.get('category', 'N/A')}")
                    st.write(f"Expense Ratio: {fund_data.get('expense_ratio', 'N/A')}")
                    st.write(f"NAV: ${fund_data.get('nav', 'N/A')}")
                    
                with col2:
                    st.subheader("Performance Metrics")
                    metrics = data_fetcher.get_performance_metrics(symbol)
                    
                    for period, return_val in metrics.items():
                        st.metric(period, f"{return_val:.2f}%")
                
                # Historical Performance Chart
                st.subheader("Historical Performance")
                fig = go.Figure()
                hist_data = data_fetcher.get_historical_data(symbol)
                
                fig.add_trace(go.Scatter(
                    x=hist_data.index,
                    y=hist_data['Close'],
                    mode='lines',
                    name=symbol
                ))
                
                fig.update_layout(
                    title=f"{symbol} Price History",
                    xaxis_title="Date",
                    yaxis_title="Price ($)",
                    height=500
                )
                
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("Unable to fetch fund data. Please check the symbol.")
