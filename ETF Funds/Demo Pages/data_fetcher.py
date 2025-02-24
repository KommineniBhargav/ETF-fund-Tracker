import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

def validate_symbol(symbol):
    """Validate if the symbol exists"""
    try:
        ticker = yf.Ticker(symbol)
        return ticker.info is not None
    except:
        return False

def get_current_price(symbol):
    """Get current price for a symbol"""
    try:
        ticker = yf.Ticker(symbol)
        return ticker.info['regularMarketPrice']
    except:
        return None

def get_daily_change(symbol):
    """Get daily percentage change"""
    try:
        ticker = yf.Ticker(symbol)
        return ((ticker.info['regularMarketPrice'] - ticker.info['previousClose']) 
                / ticker.info['previousClose'] * 100)
    except:
        return None

def get_fund_info(symbol):
    """Get basic fund information"""
    try:
        ticker = yf.Ticker(symbol)
        return ticker.info
    except:
        return None

def get_historical_data(symbol, period="1y"):
    """Get historical price data"""
    try:
        ticker = yf.Ticker(symbol)
        return ticker.history(period=period)
    except:
        return None

def get_performance_metrics(symbol):
    """Calculate performance metrics for different time periods"""
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1y")
        
        current_price = hist['Close'][-1]
        metrics = {
            "1-Day": ((current_price - hist['Close'][-2]) / hist['Close'][-2] * 100),
            "1-Month": ((current_price - hist['Close'][-22]) / hist['Close'][-22] * 100),
            "3-Month": ((current_price - hist['Close'][-66]) / hist['Close'][-66] * 100),
            "YTD": ((current_price - hist['Close'][0]) / hist['Close'][0] * 100)
        }
        
        return metrics
    except:
        return {}
