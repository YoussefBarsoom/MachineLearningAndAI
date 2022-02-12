import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset= pd.read_csv('Ads_CTR_Optimisation.csv')


#implement UCB
import math
N=10000
d=10
ads_selected = []
bounds = []
numOfSelection= [0] * d
sumOfReward = [0] * d
totalReward = 0
for n in range(0,N):
    ad=0
    maxUB=0
    for i in range(0,10):
        if (numOfSelection[i]>0):
            averageReward = sumOfReward[i]/numOfSelection[i]
            marginOfError = math.sqrt(3/2 * math.log(n+1) /numOfSelection[i])
            upperBound = averageReward + marginOfError
        else:
            upperBound = 1e400
        if upperBound > maxUB:
            maxUB = upperBound
            bounds.append(maxUB)
            ad = i
    ads_selected.append(ad)
    numOfSelection[ad] = numOfSelection[ad]+1
    reward = dataset.values[n,ad]
    sumOfReward[ad] = sumOfReward[ad] + reward
    totalReward= totalReward + reward

        