import plotly.graph_objects as go

class Dashboard:
    """
    Generate interactive visualizations for trading performance.
    """
    @staticmethod
    def plot_equity_curve(dates, equity):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=equity, mode="lines", name="Equity Curve"))
        fig.update_layout(title="Equity Curve", xaxis_title="Date", yaxis_title="Portfolio Value")
        return fig

    @staticmethod
    def plot_drawdown(dates, drawdowns):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=drawdowns, mode="lines", name="Drawdown"))
        fig.update_layout(title="Drawdown", xaxis_title="Date", yaxis_title="Drawdown")
        return fig