"""Demo runner for the information system."""
from .strategies import btc_trend_signal, eth_ratio_signal, stablecoin_peg_alert

def run_demo():
    print("=== Crypto Trading Information System - Demo ===\n")
    print("Disclaimer: Educational signals only. Not financial advice.\n")

    # Synthetic example values
    btc = btc_trend_signal(price=67000, ema20=65000, ema50=62000)
    eth = eth_ratio_signal(eth_btc_ratio=0.038, ratio_ema=0.036)
    stable = stablecoin_peg_alert(price=0.9998)

    for s in [btc, eth, stable]:
        print(f"{s.asset} ({s.asset_class}): {s.direction.upper()} | strength={s.strength:.2f}")
        print(f"  Reason: {s.reason}")
        print(f"  Risk: {s.risk_note}\n")

if __name__ == "__main__":
    run_demo()
