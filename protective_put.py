import numpy as np
import matplotlib.pyplot as plt

def put_payoff(sT,strike_price,premium):
    pnl = np.where(sT < strike_price, strike_price - sT,0)
    return pnl - premium

spot_price = 700
stock_purchase_price = 700

strike_price_put = 700
premium =  20
sT = np.arange(0.9*spot_price, 1.1*spot_price)

payoff_long_put = put_payoff(sT,strike_price_put,premium)

payoff_auro_pharma_stock = sT - stock_purchase_price

protective_put_payoff = payoff_long_put + payoff_auro_pharma_stock


fig,ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_put,'--',label= 'long put', color = 'g')
ax.plot(sT,payoff_auro_pharma_stock,'--',label= 'long Pharma stock', color = 'r')
ax.plot(sT,protective_put_payoff,label= 'protective put', color = 'b')
plt.xlabel('Stock price')
plt.ylabel('PNL')

plt.legend()
plt.show()