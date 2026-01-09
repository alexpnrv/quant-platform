from pathlib import Path
from quant_platform.reporting.dashboard import Dashboard

class ReportGenerator:
    """
    Generate HTML/PDF performance reports.
    """
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.dashboard = Dashboard()

    def generate_html(self, dates, equity, drawdowns, filename = "report.html"):
        fig_eq = self.dashboard.plot_equity_curve(dates, equity)
        fig_dd = self.dashboard.plot_drawdown(dates, drawdowns)
        output_file = self.output_dir / filename
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(fig_eq.to_html(full_html=True, include_plotlyjs="cdn"))
            f.write(fig_dd.to_html(full_html=True, include_plotlyjs="cdn"))
        return output_file