import numpy as np

def sharpe_ratio(returns: np.ndarray, risk_free_rate: float = 0.0) -> float:
    mean = np.mean(returns) - risk_free_rate
    std = np.std(returns)
    if std == 0:
        return 0.0
    return float(mean / std)

def max_drawdown(prices: np.ndarray) -> float:
    cumulative_max = np.maximum.accumulate(prices)
    drawdowns = (prices - cumulative_max) / cumulative_max
    return float(np.min(drawdowns))

def value_at_risk(returns: np.ndarray, confidence_level: float = 0.05) -> float:
    return float(np.percentile(returns, 100 * confidence_level))