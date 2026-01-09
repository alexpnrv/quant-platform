import asyncio
import logging
from typing import List

from quant_platform.market_data.client import MarketDataClient

logger = logging.getLogger(__name__)

class MarketDataFetcher:
    """
    Asynchronous market data fetcher for multiple symbols.
    """
    def __init__(self, client: MarketDataClient):
        self.client = client

    async def fetch_latest_prices(self, symbols: List[str]) -> dict:
        tasks = [self.client.fetch_price(sym) for sym in symbols]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        prices = {}
        for sym, res in zip(symbols, results):
            if isinstance(res, Exception):
                logger.error("Failed to fetch %s: %s", sym, res)
            else:
                prices[sym] = res
        return prices