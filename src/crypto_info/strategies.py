"""Asset-class specific signal generators (informational only)."""
from dataclasses import dataclass
from typing import Literal

@dataclass
class Signal:
    asset: str
    asset_class: str
    direction: Literal["long", "short", "neutral", "alert"]
    strength: float  # 0.0 to 1.0
    reason: str
    risk_note: str

def btc_trend_signal(price: float, ema20: float, ema50: float) -> Signal:
    """Simple dual-EMA trend signal for Bitcoin."""
    if ema20 > ema50 and price > ema20:
        return Signal("BTC", "Bitcoin", "long", 0.7, "Price above rising EMAs", "Medium volatility regime")
    elif ema20 < ema50 and price < ema20:
        return Signal("BTC", "Bitcoin", "short", 0.6, "Price below falling EMAs", "Bearish regime")
    return Signal("BTC", "Bitcoin", "neutral", 0.3, "No clear trend", "Wait for confirmation")

def eth_ratio_signal(eth_btc_ratio: float, ratio_ema: float) -> Signal:
    if eth_btc_ratio > ratio_ema * 1.02:
        return Signal("ETH", "Ethereum", "long", 0.65, "ETH/BTC ratio strengthening", "Relative strength")
    return Signal("ETH", "Ethereum", "neutral", 0.4, "ETH/BTC ratio not outperforming", "Monitor BTC correlation")

def stablecoin_peg_alert(price: float) -> Signal:
    deviation = abs(price - 1.0)
    if deviation > 0.005:
        return Signal("USDC", "Stablecoin", "alert", min(1.0, deviation * 50), f"Peg deviation {deviation*100:.2f}%", "Monitor reserves and venues")
    return Signal("USDC", "Stablecoin", "neutral", 0.1, "Peg stable", "Normal")
