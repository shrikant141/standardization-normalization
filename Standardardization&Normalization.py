# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:06:20 2021

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

seed = pd.read_csv("F:/DataSets/Seeds_data.csv")

def std_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

# scaled data frame (considering the numerical part of data)
stand = std_func(seed)
stand.describe()

print(stand)
