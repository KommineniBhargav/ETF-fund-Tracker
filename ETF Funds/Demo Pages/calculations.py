import numpy as np
import pandas as pd

def calculate_returns(prices):
    """Calculate percentage returns"""
    return (prices.pct_change() * 100).dropna()

def calculate_volatility(returns, period=252):
    """Calculate annualized volatility"""
    return returns.std() * np.sqrt(period)

def calculate_sharpe_ratio(returns, risk_free_rate=0.02, period=252):
    """Calculate Sharpe ratio"""
    excess_returns = returns - risk_free_rate/period
    return np.sqrt(period) * excess_returns.mean() / returns.std()

def calculate_drawdown(prices):
    """Calculate maximum drawdown"""
    rolling_max = prices.expanding().max()
    drawdown = (prices - rolling_max) / rolling_max
    return drawdown.min()

def calculate_portfolio_metrics(holdings):
    """Calculate portfolio-level metrics"""
    total_value = 0
    weighted_returns = 0
    
    for symbol, shares in holdings.items():
        price = get_current_price(symbol)
        position_value = price * shares
        total_value += position_value
        
        returns = calculate_returns(get_historical_data(symbol)['Close'])
        weighted_returns += returns.mean() * (position_value / total_value)
    
    return {
        'total_value': total_value,
        'weighted_returns': weighted_returns
    }
