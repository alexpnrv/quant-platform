from typing import Dict
import numpy as np
from quant_platform.risk.metrics import sharpe_ratio, max_drawdown

class Portfolio:
    """
    Simple portfolio representation.
    """
    def __init__(self):
        self.positions: Dict[str, float] = {}
        self.history: Dict[str, list] = {}

    def update_position(self, symbol: str, value: float):
        self.positions[symbol] = value
        self.history.setdefault(symbol, []).append(value)

    def portfolio_value(self) -> float:
        return sum(self.positions.values())

    def portfolio_sharpe(self) -> float:
        returns = np.diff(list(self.positions.values()), prepend=0)
        return sharpe_ratio(np.array(returns))

    def portfolio_drawdown(self) -> float:
        values = np.array(list(self.positions.values()))
        return max_drawdown(values)