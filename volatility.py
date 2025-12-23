import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('mock_aaple.csv', index_col= ['Date'])


data['log Returns'] = np.log(data['Adj Close'] / data['Adj Close'].shift(1)) 

data['5 day Historical Volatility'] = 100*data['log Returns'].rolling(window=4).std()*np.sqrt(4)
print(data)