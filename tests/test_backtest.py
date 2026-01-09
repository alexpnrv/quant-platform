import pytest
from quant_platform.backtest.engine import BacktestEngine
from quant_platform.backtest.execution import ExecutionHandler
from quant_platform.backtest.events import MarketEvent, OrderEvent

def dummy_strategy(event: MarketEvent):
    return [OrderEvent(symbol=event.symbol, quantity=10, order_type="BUY", timestamp=event.timestamp)]

def test_backtest_execution(caplog):
    execution_handler = ExecutionHandler(slippage=0, transaction_cost=0)
    engine = BacktestEngine(execution_handler)
    engine.register_strategy(dummy_strategy)
    events = [MarketEvent(symbol="AAPL", price=100, timestamp="2026-01-09T10:00:00")]
    with caplog.at_level("INFO"):
        engine.run(events)
    assert "Executed BUY order for AAPL at 100.0" in caplog.text