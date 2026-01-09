import logging
from typing import List, Callable
from quant_platform.backtest.events import MarketEvent, OrderEvent
from quant_platform.backtest.execution import ExecutionHandler

logger = logging.getLogger(__name__)

class BacktestEngine:
    """
    Core event-driven backtesting engine.
    """
    def __init__(self, execution_handler: ExecutionHandler):
        self.execution_handler = execution_handler
        self.strategies: List[Callable[[MarketEvent], List[OrderEvent]]] = []

    def register_strategy(self, strategy: Callable[[MarketEvent], List[OrderEvent]]):
        # Add a strategy to the engine.
        self.strategies.append(strategy)

    def run(self, market_events: List[MarketEvent]):
        # Run the backtest over a sequence of market events.
        for event in market_events:
            for strategy in self.strategies:
                orders = strategy(event)
                for order in orders:
                    self.execution_handler.execute_order(order, event.price)