'''
Pandas head() method is used to return top n (5 by default) rows of a data frame or series.

Pandas tail() method is used to return bottom n (5 by default) rows of a data frame or series.

'''

import pandas as pd
import numpy as np

data = pd.read_csv("nba.csv")
data_top = data.head()
print(data_top)
data1 = data["Weight"]
dat = data1.head(n=9)
print(f'Top 9 rows of weight : \n{dat}')
n=9
series = data["Name"]
top = series.head(n=n)
print(top)

print()
data2 = data.tail(n=6)
print(f'The last 6 rows of table : \n{data2}')
data3 = data["Salary"]
dat1 = data3.tail(n=8)
print(dat1)
