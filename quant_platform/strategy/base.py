from abc import ABC, abstractmethod
from typing import List
from quant_platform.backtest.events import MarketEvent, OrderEvent

class StrategyBase(ABC):
    """
    Abstract base class for all trading strategies.
    """
    @abstractmethod
    def generate_signals(self, event: MarketEvent) -> List[OrderEvent]:
        # Generate orders based on market event.
        pass