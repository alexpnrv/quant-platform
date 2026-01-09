from typing import List
from quant_platform.strategy.base import StrategyBase
from quant_platform.backtest.events import MarketEvent, OrderEvent

class DummyMomentumStrategy(StrategyBase):
    """
    Example momentum strategy generating simple buy signals.
    """
    def generate_signals(self, event: MarketEvent) -> List[OrderEvent]:
        return [OrderEvent(symbol=event.symbol, quantity=10, order_type="BUY", timestamp=event.timestamp)]