import argparse
from quant_platform.backtest.engine import BacktestEngine
from quant_platform.backtest.execution import ExecutionHandler
from quant_platform.strategy.example import DummyMomentumStrategy
from quant_platform.reporting.report import ReportGenerator
from pathlib import Path
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Quant Platform CLI")
    parser.add_argument("--backtest", action="store_true", help="Run a backtest")
    parser.add_argument("--report", action="store_true", help="Run performance report")
    args = parser.parse_args()

    if args.backtest:
        execution_handler = ExecutionHandler()
        engine = BacktestEngine(execution_handler)
        engine.register_strategy(DummyMomentumStrategy().generate_signals)
        # market_data = [pd.Series({"symbol": "AAPL", "price": 100, "timestamp": "2026-01-09T10:00:00"})]
        print("Backtest completed (demo)")

    if args.report:
        output_dir = Path("reports")
        report_gen = ReportGenerator(output_dir)
        dates = pd.date_range(start="2026-01-01", periods=5)
        equity = [100, 102, 101, 105, 107]
        drawdowns = [0, -0.02, -0.01, 0, 0.01]
        report_file = report_gen.generate_html(dates, equity, drawdowns)
        print(f"Report generated at {report_file}")

if __name__ == '__main__':
    main()