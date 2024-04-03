print("Handling the categorical data\n")

import pandas as pd
df = pd.DataFrame([
    ['green','M',10.1,'class2'],
    ['red','L',13.5,'class1'],
    ['blue','XL',15.3,'class2'],
    ['black','M',151.3,'class3']]
)
df.columns = ['color','size','price','label']
print(df)
print()
size_mapping = {'XL':2,'L':1,'M':0}
df['size'] = df['size'].map(size_mapping)
print(df)
print()

int_size_mapping = {v:k for k,v in size_mapping.items()}
a = df['size'].map(int_size_mapping)
print(a)

# Label encoding
#when we have more than 2 labels, multiple classificaltion
import numpy as np
class_mapping = {label: idx for idx, label in enumerate(np.unique(df['label']))}
print(class_mapping)
print()
df['label'] = df['label'].map(class_mapping)
print(df)
print()
inv_class_mapping = {v:k for k,v in class_mapping.items()}
df['label'] = df['label'].map(inv_class_mapping)
print(df)

