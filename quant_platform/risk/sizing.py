def kelly_fraction(win_prob: float, win_loss_ratio: float) -> float:
    # Compute position size fraction using Kelly criterion
    if win_loss_ratio <= 0 or win_prob <= 0 or win_prob >= 1:
        return 0.0
    return (win_prob * (win_loss_ratio + 1) - 1) / win_loss_ratio

def volatility_target_position(cash: float, volatility: float, target_vol: float) -> float:
    # Compute position size to target a desired portfolio volatility
    if volatility <= 0:
        return 0.0
    return cash * (target_vol / volatility)