print("Handling the Missing Data\n")


import pandas as pd
from io import StringIO
csv_data = '''  A,B,C,D
1.0,2.0,3.0,4.0
5.0,6.0,99.0,8.0
10.0,11.0,12.0
32.0,,22.0
43.0,,2.0'''

df = pd.read_csv(StringIO(csv_data))
print(df)
print()
print(df.isnull().sum())
print()
print(df.values)
print(df.dropna(axis=0))
print()
print(df.dropna(axis=1))
print()
from sklearn.impute import SimpleImputer
import numpy as np
imr = SimpleImputer(missing_values=np.nan, strategy='mean')
imr = imr.fit(df.values)
imputed_data = imr.transform(df.values)
print(imputed_data)

print()
imr3 = SimpleImputer(missing_values=np.nan, strategy='median')
imr3 = imr3.fit(df.values)
imputed_data3 = imr3.transform(df.values)
print(imputed_data3)

print()
imr2 = SimpleImputer(missing_values=np.nan, strategy='constant')
imr2 = imr2.fit(df.values)
imputed_data2 = imr2.transform(df.values)
print(imputed_data2)

print()
imr1 = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imr1 = imr1.fit(df.values)
imputed_data1 = imr1.transform(df.values)
print(imputed_data1)
print()

print(df.fillna(df.mean()))
print()
print(df.fillna(df.median()))
print()

