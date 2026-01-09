from dataclasses import dataclass

@dataclass(frozen=True)
class MarketEvent:
    symbol: str
    price: float
    timestamp: str

@dataclass(frozen=True)
class OrderEvent:
    symbol: str
    quantity: int
    order_type: str # 'BUY' or 'SELL'
    timestamp: str