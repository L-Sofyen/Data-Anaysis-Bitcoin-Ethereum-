#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd


# In[12]:


bitcoin=pd.read_csv('BTC-EUR.csv' , index_col='Date' , parse_dates=True)


# In[13]:


bitcoin


# In[14]:


bitcoin['Close'].plot(figsize=(9,6))
plt.show()


# In[15]:


bitcoin.index


# In[17]:


bitcoin['2021']['Close'].plot()


# In[18]:


bitcoin['2021-12']['Close'].plot()


# In[20]:


bitcoin['2021-12' : '2022-02']['Close'].plot()


# In[23]:


bitcoin.loc['2022' , 'Close'].resample('M').plot()
plt.show()


# In[24]:


bitcoin.loc['2022' , 'Close'].resample('M').mean().plot()
plt.show()


# In[26]:


bitcoin.loc['2022' , 'Close'].resample('2W').plot()
plt.show()


# In[27]:


bitcoin.loc['2022' , 'Close'].resample('2W').mean().plot()
plt.show()


# In[28]:


bitcoin.loc['2022' , 'Close'].resample('2W').std().plot()
plt.show()


# In[29]:


plt.figure(figsize=(12,8))
bitcoin.loc['2022','Close'].plot()
bitcoin.loc['2022' , 'Close'].resample('M').mean().plot(label='moyenne par mois',lw=3,ls=':', alpha=0.8)
bitcoin.loc['2022' , 'Close'].resample('W').mean().plot(label='moyenne par semaine',lw=2,ls='--', alpha=0.8)
plt.legend()
plt.show()


# In[30]:


bitcoin.loc['2022','Close'].resample('W').agg(['mean','std','min','max'])


# In[34]:


m=bitcoin.loc['2022' , 'Close'].resample('W').agg(['mean','std','min','max'])
plt.figure(figsize=(12,8))
m['mean']['2022'].plot(label='moyenne par semaine')
plt.fill_between(m.index, m['max'], m['min'], alpha=0.2, label='min-max par semaine')
plt.legend()
plt.show()


# In[41]:


plt.figure(figsize=(12,8))
bitcoin.loc['2022','Close'].plot()
bitcoin.loc['2022','Close'].rolling(window=7).mean().plot(label='non centre' , ls=':' ,lw=2)
bitcoin.loc['2022','Close'].rolling(window=7 , center=True).mean().plot(label='centre' , ls='--' , lw=3)
bitcoin.loc['2022','Close'].ewm(alpha=0.6).mean().plot(label='moving average')
plt.legend()
plt.show()


# In[53]:


plt.figure(figsize=(12,8))
bitcoin.loc['2022-01' , 'Close'].plot()
for i in np.arange(0.2 , 1, 0.2):
    bitcoin.loc['2022-01','Close'].ewm(alpha=i).mean().plot(label=f'ewm {i}', ls='--', alpha=0.8)
plt.legend()
plt.show()


# In[54]:


ethereum=pd.read_csv('ETH-EUR.csv' , index_col='Date' , parse_dates=True)


# In[55]:


ethereum['2022']['Close'].plot()


# In[59]:


btc_eth = pd.merge(bitcoin , ethereum , on='Date' , how='inner' ,  suffixes=('_btc' , '_eth'))


# In[62]:


btc_eth[['Close_btc' , 'Close_eth']].plot(subplots=True , figsize=(12,8))


# In[65]:


correlations=btc_eth[['Close_btc' , 'Close_eth']].corr()


# In[66]:


import seaborn as sns 
sns.heatmap(correlations)


# In[ ]:




