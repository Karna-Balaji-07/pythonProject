import pandas as pd
import numpy as np

data = [1,2,3,4,5]
sr = pd.Series(data)
print(sr)

print("Creating a series from an array")
arr = np.array([9,8,7,6,5,4,3])
sr1 = pd.Series(arr)
print(sr1)

data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
sr2 = pd.Series(data)
print(sr2[:4])
sr3 = pd.Series(data,index=[2,4,6,8,10,12,14,16,18,20,22,24,26])
print(sr3[10])
print(sr3[20])