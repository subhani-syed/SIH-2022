## Importing Basic Packages

import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt


## Data of states,locations,jobs and regions

states=pd.read_csv('states.csv')

states=list(states)


locations=pd.read_csv('Locations.csv')

locations=list(locations)

jobs=pd.read_csv('jobs.csv')

jobs=list(jobs)


regions=['South','North','East','West','Central']

branches=['CSE/IT','MEC','CIV','CHEM','ECE','EEE']

## Considering past 10 years

years=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

## Mapping jobs into concerned Branches

chem=jobs[0:10]

cse=jobs[10:20]

ece=jobs[20:29]

ece.append('Instrumentation engineer')

eee=jobs[29:39]

eee.remove('Instrumentation engineer')

eee.append(jobs[39])


mec=jobs[40:50]

civ=jobs[50:60]

## Mapping locations to their concerned states

m={}

for i in range(len(states)):
    m[states[i]]=locations[i*3:(i+1)*3]

m['Tamil Nadu'].append('Chennai')

m['Kerala'].remove('Chennai')

m['Andhra Pradesh'].append('Visakhapatnam')
m['Tamil Nadu'].remove('Visakhapatnam')

m['Goa'].remove('Srinagar')
m['Goa'].remove('Jammu')
m['Jammu and Kashmir'].append('Srinagar')
m['Jammu and Kashmir'].append('Jammu')
m['Himachal Pradesh'].append('Shimla')
m['Himachal Pradesh'].append('Bilaspur')

m['Jammu and Kashmir'].remove('Shimla')
m['Jammu and Kashmir'].remove('Bilaspur')
m['Jammu and Kashmir'].remove('Dehradun')
m['Himachal Pradesh'].remove('Chandigarh')
m['Himachal Pradesh'].remove('Roorkee')
m['Himachal Pradesh'].remove('Haridwar')
m['Uttarakhand'].append('Haridwar')
m['Uttarakhand'].append('Roorkee')
m['Uttarakhand'].append('Dehradun')


m['Uttarakhand'].remove('Amritsar')
m['Uttarakhand'].remove('Jalandhar')
m['Uttarakhand'].remove('Lucknow')
m['Punjab'].append('Amritsar')
m['Punjab'].append('Jalandhar')
m['Punjab'].append('Chandigarh')


m['Uttar Pradesh'].append('Lucknow')
m['Uttar Pradesh'].append('Allahabad')
m['Uttar Pradesh'].append('Noida')
m['Uttar Pradesh'].append('Kanpur')

m['Punjab'].remove('Allahabad')
m['Punjab'].remove('Noida')
m['Punjab'].remove('Kanpur')
m['Uttar Pradesh'].remove('Kolkata')
m['Uttar Pradesh'].remove('Durgapur')
m['Uttar Pradesh'].remove('Howrah')

for v in m['West Bengal']:
    m['Seven Sisters'].append(v)

m['West Bengal'].clear()


m['West Bengal'].append('Durgapur')
m['West Bengal'].append('Kolkata')
m['West Bengal'].append('Howrah')

for v in m['Rajasthan']:
    m['Seven Sisters'].append(v)
m['Rajasthan'].clear()
for v in m['Gujarat']:
    m['Rajasthan'].append(v)
m['Gujarat'].clear()    
for v in m['Haryana']:
    m['Gujarat'].append(v)
m['Gujarat'].append('Vadodara')
m['Haryana'].clear()    
for v in m['Maharashtra']:
    m['Haryana'].append(v)
m['Haryana'].remove('Vadodara')
m['Maharashtra'].clear()    
for v in m['Madhya Pradesh']:
    m['Maharashtra'].append(v)
m['Madhya Pradesh'].clear()    
for v in m['Chattisgarh']:
    m['Madhya Pradesh'].append(v)
m['Chattisgarh'].clear()
m['Chattisgarh'].append('Raigarh')
m['Chattisgarh'].append('Raipur')
m['Orissa'].remove('Raigarh')
m['Orissa'].remove('Raipur')
m['Orissa'].append('Rourkela')
m['Orissa'].append('Puri')
m['Bihar'].remove('Rourkela')
m['Bihar'].remove('Puri')
m['Bihar'].append('Gaya')
m['Jharkhnad'].append('Jamshedpur')
m['Jharkhnad'].remove('Gaya')


## Mapping states to their concerned regions

n={}


n['South']=states[:6]

n['North']=states[6:11]

n['East']=states[11:13]

n['West']=states[13:16]

n['Central']=states[16:]


## Creation of randomised Dataset

jobr=[]
for i in range(9438):
    x=random.randint(0,59)
    jobr.append(jobs[x])

locr=[]
for i in range(9438):
    x=random.randint(0,66)
    locr.append(locations[x])

yearr=[]
for i in range(9438):
    x=random.randint(0,10)
    yearr.append(years[x])

data=pd.DataFrame(list(zip(yearr,jobr,locr)),columns =['YEAR','JOB_TITLE','JOB_LOCATION'])

## Feature Extraction

### Determination of Branches 

branch=[]
for c in data['JOB_TITLE']:
    if c in cse:
        branch.append('CSE/IT')
    elif c in ece:
        branch.append('ECE')
    elif c in eee:
        branch.append('EEE')
    elif c in mec:
        branch.append('MEC')
    elif c in civ:
        branch.append('CIV')
    else:
        branch.append('CHEM')

data['BRANCH']=branch


### Determination of States

stater=[]
for v in data['JOB_LOCATION']:
    for w in m:
        if v in m[w]:
            stater.append(w)
            break

data['LOC_STATE']=stater


### Determination of Regions

regionr=[]
for v in data['LOC_STATE']:
    for w in n:
        if v in n[w]:
            regionr.append(w)
            break

data['LOC_REGION']=regionr

data=data[['YEAR','JOB_TITLE','BRANCH','JOB_LOCATION','LOC_STATE','LOC_REGION']]


## Considering next 5 years for prediction

x_pred=[2022,2023,2024,2025,2026]

## Considering possible queries to create training and test datasets

### Query data generation and feature extraction

yui=[]
for i in range(50):
    x=random.randint(0,5)
    yui.append(branches[x])

tyu=[]
for i in range(50):
    x=random.randint(0,21)
    tyu.append(states[x])

query=pd.DataFrame(list(zip(yui,tyu)),columns =['BRANCH','LOC_STATE'])

regionq=[]
for v in query['LOC_STATE']:
    for w in n:
        if v in n[w]:
            regionq.append(w)
            break

query['LOC_REGION']=regionq

## Feature scaling

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))

## Generation of training dataset 

train_x=[]
train_y=[]

for index,row in query.iterrows():
    y1=[]
    x_train=[]
    p=data.loc[(data['BRANCH']==row['BRANCH']) & (data['LOC_STATE']==row['LOC_STATE']) & (data['LOC_REGION']==row['LOC_REGION'])]
    for i in years:
        y=p.loc[p['YEAR']==i].shape[0]
        y*=98
        y1.append(y)
    y1=np.array(y1[:8])
    y1=y1.reshape(-1,1)
    scaled = sc.fit_transform(y1)
    for j in range(scaled.shape[0]-3):
        x_train.append(scaled[j:j+3,])
        train_y.append(scaled[j+3][0])
    train_x.append(np.array(x_train))
train_x=np.array(train_x)
train_y=np.array(train_y)

train_x=train_x.reshape(250,3,1)


## Model Building

# pip install tensorflow

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

regressor = Sequential()

regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (train_x.shape[1], 1)))

regressor.add(Dropout(rate = 0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(rate = 0.2))

regressor.add(LSTM(units = 50, return_sequences = False))
regressor.add(Dropout(rate = 0.2))

regressor.add(Dense(units = 1))

## Model Compilation

regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

## Model Training

regressor.fit(x = train_x, y = train_y, batch_size = 15, epochs = 50)