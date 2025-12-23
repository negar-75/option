import numpy as np #numerical computing
import matplotlib.pyplot as plt #chart creating

# PUT PAYOFF 


def put_payoff(sT,strike_price,premium):
    pnl = np.where(sT < strike_price, strike_price - sT,0)
    return pnl - premium
spot_price = 890
#creating dataset for sT as +/- 10% from spot price
sT = np.arange(spot_price*0.9, spot_price*1.1)

#buy a put

strike_long_price = 880
premium_long = 15


payoff_long_put= put_payoff(sT,strike_long_price,premium_long)

#sell a put
strike_short_price = 860
premium_short = 10


payoff_short_put= put_payoff(sT,strike_short_price,premium_short)* -1.0

bear_put_spread = payoff_long_put + payoff_short_put


#plot the graph

fig,ax = plt.subplots(figsize=(8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_put, '--' ,label = 'long 880 strike put', color='g')
ax.plot(sT,payoff_short_put, '--' ,label = 'short 870 strike put', color='r')
ax.plot(sT,bear_put_spread, label = 'Bear put spread', color='b')
plt.xlabel('infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()




