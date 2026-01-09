import pytest
from quant_platform.market_data.client import MarketDataClient
from quant_platform.market_data.fetcher import MarketDataFetcher

class DummyClient(MarketDataClient):
    async def fetch_price(self, symbol: str) -> float:
        return 100.0

    async def fetch_historical(self, symbol: str, start: str, end: str) -> dict:
        return {"prices": [100, 101, 102]}

@pytest.mark.asyncio
async def test_fetch_latest_prices():
    client = DummyClient()
    fetcher = MarketDataFetcher(client)
    symbols = ["AAPL", "GOOG"]
    prices = await fetcher.fetch_latest_prices(symbols)
    assert prices == {"APPL": 100.0, "GOOG": 100.0}