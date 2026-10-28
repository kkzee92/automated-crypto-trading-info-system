# Trading Strategies by Asset Class

All strategies generate **informational signals** only. Position sizing and risk parameters are recommendations, not automated orders.

## 1. Bitcoin (BTC)

**Characteristics:** Highest liquidity, store-of-value narrative, lower relative volatility than most alts.

**Strategies:**
- **Trend Following:** Dual moving average crossover (e.g., 20/50 EMA) or Donchian channel breakout. Best in strong directional regimes.
- **DCA Signal:** Time-based or volatility-adjusted accumulation signals when below long-term moving average.
- **Volatility Regime Filter:** Reduce exposure or widen stops when realized volatility exceeds threshold (e.g., 30-day realized vol > 80%).

**Risk Notes:** Still subject to large drawdowns. Prefer spot or low-leverage.

## 2. Ethereum (ETH)

**Characteristics:** Smart-contract platform, gas fees as activity proxy, often correlated with BTC but with relative strength cycles.

**Strategies:**
- **ETH/BTC Ratio Trend:** Trade relative strength (long ETH / short BTC equivalent when ratio in uptrend).
- **Activity Proxy:** Rising gas fees or transaction counts as short-term momentum confirmation.
- **Post-upgrade Event Windows:** Heightened volatility around network upgrades — informational alerts only.

## 3. Major Altcoins (e.g., SOL, AVAX, top 20 by liquidity)

**Characteristics:** Higher beta to BTC, thinner order books, more prone to false breakouts.

**Strategies:**
- **Momentum / Breakout:** Price break of recent range with volume confirmation. Tighter stops required.
- **Relative Strength Ranking:** Prefer assets outperforming BTC on a rolling basis.
- **Risk Adjustment:** Smaller position sizes (e.g., 0.5-1% risk per idea vs 1-2% for BTC).

## 4. Stablecoins (USDT, USDC, DAI, etc.)

**Characteristics:** Designed for peg stability. Primary risks are depeg events and counterparty/reserve quality.

**Strategies:**
- **Peg Monitoring:** Alert when price deviates > 0.5% from $1.00 on major venues.
- **Yield Opportunity Signals:** Informational flags for high-yield venues (with strong risk warnings on smart-contract and counterparty risk).
- **Flight-to-Safety:** Increased stablecoin demand as risk-off signal for risk assets.

## 5. DeFi Tokens

**Characteristics:** Protocol-specific risks (smart contract, governance, incentive dilution). High volatility.

**Strategies:**
- **TVL / Usage Proxies:** Rising total value locked or protocol revenue as bullish informational signal.
- **Incentive Dilution Alerts:** Large unlocks or emission schedules.
- **Relative Value:** Protocol token vs its underlying assets or competitors.

## Cross-Asset Risk Framework

- Maximum portfolio heat: define total risk budget.
- Correlation awareness: most crypto assets are positively correlated in stress.
- Kill-switch recommendation: manual override or daily loss limit alerts.
- Always benchmark against simple buy-and-hold BTC.

**Enhancement Path:** Strategies can be further refined with on-chain data (when available), funding rates (for perpetuals), or sentiment proxies. All enhancements must pass security and risk review.
