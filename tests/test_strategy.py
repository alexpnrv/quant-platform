from quant_platform.strategy.example import DummyMomentumStrategy
from quant_platform.backtest.events import MarketEvent

def test_dummy_strategy():
    strategy = DummyMomentumStrategy()
    event = MarketEvent(symbol="AAPL", price=100, timestamp="2026-01-09T10:10:00:00")
    signals = strategy.generate_signals(event)
    assert len(signals) == 1
    assert signals[0].symbol == "AAPL"
    assert signals[0].order_type == "BUY"