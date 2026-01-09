from abc import ABC, abstractmethod

class MarketDataClient(ABC):
    """
    Abstract base class for all market data clients.
    """
    @abstractmethod
    async def fetch_price(self, symbols: str) -> float:
        # Fetch the latest price for the given symbol.
        pass

    @abstractmethod
    async def fetch_historical(self, symbol: str, start: str, end: str) -> dict:
        # Fetch historical price data between start and end dates
        pass