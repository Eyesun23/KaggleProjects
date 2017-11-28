#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Project: Emergency 911 Calls

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.show()

df1 = pd.read_csv('911.csv')
df1.info()
df1.head()

df1['zip'].value_counts().head(5)

df1['twp'].value_counts().head(5)

df1['title'].nunique()

x = df1['title'].iloc[0]
x.split(':')[0]
df1['Reason'] = df1['title'].apply(lambda title: title.split(':')[0])
df1['Reason']

df1['Reason'].value_counts().head(1)

sns.countplot(x='Reason',data=df1,palette='viridis')

df1['timeStamp'] = pd.to_datetime(df1['timeStamp'])
type(df1['timeStamp'].iloc[0])

time = df1['timeStamp'].iloc[0]
time.hour
time.dayofweek
time.month

df1['Hour'] = df1['timeStamp'].apply(lambda time: time.hour)
df1['Month'] = df1['timeStamp'].apply(lambda time: time.month)
df1['Day of Week'] = df1['timeStamp'].apply(lambda time: time.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df1['Day of Week'] = df1['Day of Week'].map(dmap)
df1.head()
sns.countplot(x='Day of Week', data=df1,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())

t= df1['timeStamp'].iloc[0]
df1['Date'] = df1['timeStamp'].apply(lambda t:t.date())
t.date()
df1.head()

byMonth = df1.groupby('Month').count()
byMonth.head()

df1.groupby('Date').count().head()
df1.groupby('Date').count()['lat']
df1.groupby('Date').count()['lat'].plot()
plt.tight_layout()


df1[df1['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
plt.tight_layout()


#unstack method
df1.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()

plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')

sns.clustermap(dayMonth,cmap='viridis')


