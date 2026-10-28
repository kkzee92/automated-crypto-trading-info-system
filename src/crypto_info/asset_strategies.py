"""Expanded strategies per asset class."""
from dataclasses import dataclass
from typing import Literal, Optional

@dataclass
class Signal:
    asset: str
    asset_class: str
    direction: Literal["long", "short", "neutral", "alert"]
    strength: float
    reason: str
    risk_note: str
    suggested_risk_pct: float = 0.01  # informational position risk guidance

def major_altcoin_momentum(price: float, high_20: float, volume_ratio: float) -> Signal:
    """Breakout-style momentum for major altcoins."""
    if price > high_20 and volume_ratio > 1.5:
        return Signal(
            "SOL", "Major Altcoin", "long", 0.6,
            "Breakout above 20-period high with volume",
            "Higher beta; use smaller size and tighter stops",
            suggested_risk_pct=0.005
        )
    return Signal("SOL", "Major Altcoin", "neutral", 0.2, "No breakout confirmation", "Wait", 0.0)

def defi_tvl_signal(tvl_change_pct: float) -> Signal:
    """Informational signal based on TVL change proxy."""
    if tvl_change_pct > 10:
        return Signal(
            "DEFI-EXAMPLE", "DeFi Token", "long", 0.55,
            f"TVL increased {tvl_change_pct:.1f}%",
            "Smart-contract and dilution risks remain high",
            suggested_risk_pct=0.004
        )
    elif tvl_change_pct < -15:
        return Signal(
            "DEFI-EXAMPLE", "DeFi Token", "alert", 0.8,
            f"Significant TVL outflow {tvl_change_pct:.1f}%",
            "Potential protocol stress",
            suggested_risk_pct=0.0
        )
    return Signal("DEFI-EXAMPLE", "DeFi Token", "neutral", 0.3, "Stable TVL", "Monitor", 0.0)

def volatility_adjusted_btc(realized_vol: float, threshold: float = 0.8) -> Signal:
    if realized_vol > threshold:
        return Signal(
            "BTC", "Bitcoin", "alert", 0.7,
            f"High realized volatility {realized_vol:.2f}",
            "Consider reducing exposure or widening risk parameters",
            suggested_risk_pct=0.005
        )
    return Signal("BTC", "Bitcoin", "neutral", 0.3, "Volatility within normal range", "Standard parameters", 0.01)
