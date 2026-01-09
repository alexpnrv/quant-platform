from quant_platform.backtest.events import OrderEvent
import logging

logger = logging.Logger(__name__)

class ExecutionHandler:
    """
    Simulates order execution including slippage and transaction costs.
    """
    def __init__(self, slippage: float = 0.001, transaction_cost: float = 1.0):
        self.slippage = slippage
        self.transaction_cost = transaction_cost

    def execute_order(self, order: OrderEvent, market_price: float) -> float:
        # Calculate executed price for an order.
        if order.order_type == "BUY":
            price = market_price * (1 + self.slippage) + self.transaction_cost
        else:
            price = market_price * (1 - self.slippage) + self.transaction_cost
        logger.info("Executed %s order for %s at %.2f", order.order_type, order.symbol, price)
        return price