#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Time series project on big data 


# In[3]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


# In[4]:


#loading few particular csv files from the dataset 
path = r'E:\Placement 2022-23\Analytics\projects\2-Time Series Data Analysis-20220907T085235Z-001\2-Time Series Data Analysis\individual_stocks_5yr'
company_list=['AAPL_data.csv','GOOG_data.csv','MSFT_data.csv','AMZN_data.csv']
all_data = pd.DataFrame()
for file in company_list:
    current_df = pd.read_csv(path+'/'+file)
    all_data = pd.concat([all_data,current_df])
all_data.shape


# In[5]:


all_data.head()


# In[6]:


all_data.dtypes


# In[7]:


all_data['date'] = pd.to_datetime(all_data['date'])


# In[8]:


all_data.dtypes


# In[9]:


#analysing the closing time of the stocks of the major stock holders as taken above. 
tech_list = all_data['Name'].unique()


# In[10]:


#iterating over the tech list 
plt.figure(figsize=(10,7))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df = all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.xticks(rotation='vertical')
    plt.title(company)

#to view the dates in better way, have to change/convert the string to date format. 


# In[11]:


#analysing the total volume of stock traded each day 
import plotly.express as px 


# In[12]:


#iterating the list 
for company in tech_list:
    df = all_data[all_data['Name']==company]
    fig= px.line(df,x='date',y='volume',title=company)
    fig.show()

#now to zoom in or check a particular data, use the plotly function or feature to cut out that part. 


# In[14]:


df.head()


# In[16]:


#analysing daily rise in price in only aapl dataset 
df1 = pd.read_csv(r'E:\Placement 2022-23\Analytics\projects\2-Time Series Data Analysis-20220907T085235Z-001\2-Time Series Data Analysis\individual_stocks_5yr\AAPL_data.csv')
df1.head()


# In[17]:


df.head()


# In[18]:


df1['Daily_price_change'] = df1['close'] - df1['open'] 


# In[19]:


df1['1day%return'] = ((df1['close'] - df1['open'])/df1['open'])*100 


# In[20]:


df1.head()


# In[21]:


fig = px.line(df1,x='date',y='1day%return',title=company)
fig.show()


# In[22]:


#analysing monthly mean of the close data 
df2=df1.copy()


# In[23]:


df2.dtypes


# In[24]:


df2['date'] = pd.to_datetime(df2['date'])


# In[25]:


df2.set_index('date',inplace=True)


# In[26]:


df2.head()


# In[27]:


#grabbing data between any two dates 
df2['2013-02-08':'2013-02-13']


# In[28]:


#resamplping by month as monthly mean analysis is being done 
df2['close'].resample('M').mean().plot(kind='bar')


# In[29]:


#for year 
df2['close'].resample('Y').mean().plot(kind='bar')


# In[31]:


#analysing the correlation of diff companies stock prices 
aapl = pd.read_csv(r'E:\Placement 2022-23\Analytics\projects\2-Time Series Data Analysis-20220907T085235Z-001\2-Time Series Data Analysis\individual_stocks_5yr\AAPL_data.csv')
aapl.head()


# In[33]:


amzn = pd.read_csv(r'E:\Placement 2022-23\Analytics\projects\2-Time Series Data Analysis-20220907T085235Z-001\2-Time Series Data Analysis\individual_stocks_5yr\AMZN_data.csv')
amzn.head()


# In[34]:


msft = pd.read_csv(r'E:\Placement 2022-23\Analytics\projects\2-Time Series Data Analysis-20220907T085235Z-001\2-Time Series Data Analysis\individual_stocks_5yr\MSFT_data.csv')
msft.head()


# In[35]:


goog = pd.read_csv(r'E:\Placement 2022-23\Analytics\projects\2-Time Series Data Analysis-20220907T085235Z-001\2-Time Series Data Analysis\individual_stocks_5yr\GOOG_data.csv')
goog.head()


# In[36]:


close = pd.DataFrame()


# In[37]:


close['aapl'] = aapl['close']
close['amzn'] = amzn['close'] 
close['msft'] = msft['close']
close['goog'] = goog['close']


# In[38]:


close.head()


# In[39]:


import seaborn as sns


# In[40]:


sns.pairplot(data=close)


# In[42]:


sns.heatmap(close.corr(),annot=True)
#conclusion is amzn and msft are most corr and goog and aapl are least. 


# In[43]:


#analysing the daily return of stocks and their correlation 
data = pd.DataFrame()


# In[44]:


data['aapl_change'] = ((aapl['close'] - aapl['open'])/aapl['close'])*100
data['amzn_change'] = ((amzn['close'] - amzn['open'])/amzn['close'])*100
data['msft_change'] = ((msft['close'] - msft['open'])/msft['close'])*100
data['goog_change'] = ((goog['close'] - goog['open'])/goog['close'])*100
data.head()


# In[45]:


sns.pairplot(data=data)


# In[46]:


sns.heatmap(data.corr(),annot=True)


# In[47]:


#value at risk analysis for different tech companies 
sns.distplot(data['aapl_change'])


# In[48]:


#finding standard deviation 
data['aapl_change'].std
#approx 68% data 


# In[49]:


data['aapl_change'].std()*2
#approx 95% data 


# In[50]:


data['aapl_change'].std()*3
#approx 98% of entire data 


# In[51]:


data['aapl_change'].quantile(0.1)
#says that 90% of the time, worst daily loss wont exceed this value. 


# In[53]:


data.describe().T

