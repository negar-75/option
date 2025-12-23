import numpy as np
import matplotlib.pyplot as plt


def call_payoff (sT, strike_price, premium):
    pnl = np.where(strike_price < sT, sT-strike_price, 0)
    return pnl - premium

spot_price = 900 
sT = np.arange(spot_price*0.95, spot_price*1.1)

#buy a call
strike_price_long =  920
premium_long= 15

payoff_long_call = call_payoff(sT,strike_price_long,premium_long)
print(payoff_long_call)



#sell a call

strike_price_short =  940
premium_short= 10

payoff_short_call = call_payoff(sT,strike_price_short,premium_short) * -1.0
print(payoff_short_call)


#bull call spread payoff

bull_call_spread_pay_off = payoff_long_call + payoff_short_call

print(bull_call_spread_pay_off)


#plot

fig,ax = plt.subplots(figsize = (8,5))
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_call, '--', label = 'long 920 strike call', color='g')
ax.plot(sT,payoff_short_call, '--', label = 'short 920 strike call', color='r')
ax.plot(sT,bull_call_spread_pay_off, label = 'Bull call spread', color='b')
plt.xlabel('Infosys Stock Price')
plt.ylabel('Profit and loss')
plt.legend()
plt.show()




