"""Enhanced demo for the information system."""
from .strategies import btc_trend_signal, eth_ratio_signal, stablecoin_peg_alert
from .asset_strategies import major_altcoin_momentum, defi_tvl_signal, volatility_adjusted_btc

def run_demo():
    print("=== Automated Crypto Trading Information System ===")
    print("Educational / paper-trading signals only. Not financial advice.\n")

    signals = [
        btc_trend_signal(67000, 65000, 62000),
        eth_ratio_signal(0.038, 0.036),
        stablecoin_peg_alert(0.9992),
        major_altcoin_momentum(180, 175, 1.8),
        defi_tvl_signal(12.5),
        volatility_adjusted_btc(0.92),
    ]

    for s in signals:
        print(f"{s.asset} [{s.asset_class}]: {s.direction.upper()} (strength {s.strength:.2f})")
        print(f"  Reason: {s.reason}")
        print(f"  Risk note: {s.risk_note}")
        if hasattr(s, "suggested_risk_pct"):
            print(f"  Suggested risk per idea: {s.suggested_risk_pct*100:.1f}%")
        print()

if __name__ == "__main__":
    run_demo()
