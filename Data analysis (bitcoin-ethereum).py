


import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd





bitcoin=pd.read_csv('BTC-EUR.csv' , index_col='Date' , parse_dates=True)


bitcoin





bitcoin['Close'].plot(figsize=(9,6))
plt.show()



bitcoin.index





bitcoin['2021']['Close'].plot()





bitcoin['2021-12']['Close'].plot()





bitcoin['2021-12' : '2022-02']['Close'].plot()





bitcoin.loc['2022' , 'Close'].resample('M').plot()
plt.show()





bitcoin.loc['2022' , 'Close'].resample('M').mean().plot()
plt.show()





bitcoin.loc['2022' , 'Close'].resample('2W').plot()
plt.show()





bitcoin.loc['2022' , 'Close'].resample('2W').mean().plot()
plt.show()





bitcoin.loc['2022' , 'Close'].resample('2W').std().plot()
plt.show()





plt.figure(figsize=(12,8))
bitcoin.loc['2022','Close'].plot()
bitcoin.loc['2022' , 'Close'].resample('M').mean().plot(label='moyenne par mois',lw=3,ls=':', alpha=0.8)
bitcoin.loc['2022' , 'Close'].resample('W').mean().plot(label='moyenne par semaine',lw=2,ls='--', alpha=0.8)
plt.legend()
plt.show()





bitcoin.loc['2022','Close'].resample('W').agg(['mean','std','min','max'])





m=bitcoin.loc['2022' , 'Close'].resample('W').agg(['mean','std','min','max'])
plt.figure(figsize=(12,8))
m['mean']['2022'].plot(label='moyenne par semaine')
plt.fill_between(m.index, m['max'], m['min'], alpha=0.2, label='min-max par semaine')
plt.legend()
plt.show()





plt.figure(figsize=(12,8))
bitcoin.loc['2022','Close'].plot()
bitcoin.loc['2022','Close'].rolling(window=7).mean().plot(label='non centre' , ls=':' ,lw=2)
bitcoin.loc['2022','Close'].rolling(window=7 , center=True).mean().plot(label='centre' , ls='--' , lw=3)
bitcoin.loc['2022','Close'].ewm(alpha=0.6).mean().plot(label='moving average')
plt.legend()
plt.show()





plt.figure(figsize=(12,8))
bitcoin.loc['2022-01' , 'Close'].plot()
for i in np.arange(0.2 , 1, 0.2):
    bitcoin.loc['2022-01','Close'].ewm(alpha=i).mean().plot(label=f'ewm {i}', ls='--', alpha=0.8)
plt.legend()
plt.show()





ethereum=pd.read_csv('ETH-EUR.csv' , index_col='Date' , parse_dates=True)





ethereum['2022']['Close'].plot()





btc_eth = pd.merge(bitcoin , ethereum , on='Date' , how='inner' ,  suffixes=('_btc' , '_eth'))





btc_eth[['Close_btc' , 'Close_eth']].plot(subplots=True , figsize=(12,8))





correlations=btc_eth[['Close_btc' , 'Close_eth']].corr()





import seaborn as sns 
sns.heatmap(correlations)







