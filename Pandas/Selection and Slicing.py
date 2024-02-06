print("DEALING WITH ROWS AND COLUMNS IN PANDAS DATAFRAME")

print("\nColumn Selection")
import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(data)
print(df["Name"])
print()
print(df[["Age","Address"]])


print("\nColumn Addition")
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
df = pd.DataFrame(data)
address = ["Kochi","Aluva","Delhi","Chennai"]
df['Address'] = address
print(df)

print("\nColumn Deletion")
data = pd.read_csv("nba.csv")
data.drop(["Team","Weight","Number"], axis=1,inplace=True)
print(data)


print("\n\n DEALING WITH ROWS")
print("\nRow Selection")
'''Pandas provide a unique method to retrieve rows from a Data frame.

DataFrame.loc[]

method is used to retrieve rows from Pandas DataFrame. Rows can also be selected by passing integer location to an iloc[] function. '''

data = pd.read_csv("nba.csv",index_col="Name")
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first,"\n\n",second)

print("\nRow Addition ")
