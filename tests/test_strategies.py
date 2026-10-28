from crypto_info.strategies import btc_trend_signal, stablecoin_peg_alert
from crypto_info.asset_strategies import major_altcoin_momentum

def test_btc_bullish():
    s = btc_trend_signal(100, 90, 80)
    assert s.direction == "long"
    assert s.asset_class == "Bitcoin"

def test_stablecoin_alert():
    s = stablecoin_peg_alert(0.99)
    assert s.direction == "alert"

def test_altcoin_no_breakout():
    s = major_altcoin_momentum(100, 105, 1.0)
    assert s.direction == "neutral"
