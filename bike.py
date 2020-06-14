# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np


'''
... functions definition below ...
'''

def isNotEmpty(can):
    
    if len(can) == 0:
        return False 
    else:
        return True


def skyline(arr):
    
    candidate = []
    for item in arr:
        candidate.append(item)
        while isNotEmpty(cadidate): 
            print('hi')
            
    

'''
program begin
'''
df = pd.read_csv('day.csv')

df2 = df[['instant', 'season', 'mnth', 'holiday', 'weekday', 
          'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'cnt']]

print(df2.head(5))
#a = np.mean(df2, axis=0)
print(df2)
array = df2.to_numpy()

skyline(array)

print(array)
