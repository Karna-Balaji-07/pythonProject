import pandas as pd
import numpy as np

print("Creating an empty DataFrame")
df = pd.DataFrame()
print(df)

print("\nCreating a Dataframe using lists")
list1 = ['hello','hi','good','morning','evening','night','afternoon']
df1 = pd.DataFrame(list1)
print(f'DataFrame using list : \n{df1}')

print("\nCreating a DataFrame from dictionary of lists")
list2 = {'Name':['Tom','Jack','John','Prime','Wick'],'Age': [23,34,43,23,55]}
df2 = pd.DataFrame(list2)
print(f'DataFrame using dictionalry of lists : \n{df2}')