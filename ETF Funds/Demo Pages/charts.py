import streamlit as st
import plotly.graph_objects as go
from utils import data_fetcher

def render_fund_comparison():
    st.header("Fund Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        symbol1 = st.text_input("First Fund Symbol").upper()
    with col2:
        symbol2 = st.text_input("Second Fund Symbol").upper()
    
    if symbol1 and symbol2:
        with st.spinner("Generating comparison..."):
            # Fetch historical data for both funds
            hist_data1 = data_fetcher.get_historical_data(symbol1)
            hist_data2 = data_fetcher.get_historical_data(symbol2)
            
            if hist_data1 is not None and hist_data2 is not None:
                # Performance Comparison Chart
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=hist_data1.index,
                    y=hist_data1['Close'],
                    mode='lines',
                    name=symbol1
                ))
                
                fig.add_trace(go.Scatter(
                    x=hist_data2.index,
                    y=hist_data2['Close'],
                    mode='lines',
                    name=symbol2
                ))
                
                fig.update_layout(
                    title="Price Comparison",
                    xaxis_title="Date",
                    yaxis_title="Price ($)",
                    height=500
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Comparison Metrics
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader(f"{symbol1} Metrics")
                    metrics1 = data_fetcher.get_performance_metrics(symbol1)
                    for period, value in metrics1.items():
                        st.metric(period, f"{value:.2f}%")
                
                with col2:
                    st.subheader(f"{symbol2} Metrics")
                    metrics2 = data_fetcher.get_performance_metrics(symbol2)
                    for period, value in metrics2.items():
                        st.metric(period, f"{value:.2f}%")
            else:
                st.error("Unable to fetch data for one or both symbols")
