import numpy as np
from quant_platform.risk.metrics import sharpe_ratio, max_drawdown, value_at_risk
from quant_platform.risk.sizing import kelly_fraction, volatility_target_position
from quant_platform.risk.portfolio import Portfolio

def test_metrics():
    returns = np.array([0.01, 0.02, -0.01])
    assert sharpe_ratio(returns) != 0
    assert max_drawdown(np.array([100, 105, 102])) <= 0
    assert value_at_risk(returns) <= 0.02

def test_sizing():
    assert 0.0 <= kelly_fraction(0.6, 2.0) <= 1.0
    assert volatility_target_position(1000, 0.2, 0.1) > 0

def test_portfolio():
    p = Portfolio()
    p.update_position("AAPL", 100)
    p.update_position("GOOG", 200)
    assert p.portfolio_value == 300
    assert isinstance(p.portfolio_sharpe(), float)
    assert isinstance(p.portfolio_drawdown(), float)