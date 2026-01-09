import pandas as pd
from quant_platform.reporting.dashboard import Dashboard
from quant_platform.reporting.report import ReportGenerator

def test_dashboard_plot():
    dates = pd.date_range(start="2026-01-01", periods=5)
    equity = [100, 102, 101, 105, 107]
    drawdowns = [0, -0.02, -0.01, 0, 0.01]
    fig_eq = Dashboard.plot_equity_curve(dates, equity)
    fig_dd = Dashboard.plot_drawdown(dates, drawdowns)
    assert fig_eq is not None
    assert fig_dd is not None

def test_report_generation(tmp_path):
    dates = pd.date_range(start="2026-01-01", periods=5)
    equity = [100, 102, 101, 105, 107]
    drawdowns = [0, -0.02, -0.01, 0, 0.01]
    report_gen = ReportGenerator(output_dir=tmp_path)
    output_file = report_gen.generate_html(dates, equity, drawdowns, filename="test.html")
    assert output_file.exists()