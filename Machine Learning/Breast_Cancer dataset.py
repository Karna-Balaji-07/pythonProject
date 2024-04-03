from sklearn.datasets import load_breast_cancer
import numpy as np

cancer = load_breast_cancer()
print(f'Cancer.keys() : {cancer.keys()}')

print(f'Shape of the cancer dataset : {cancer.data.shape}')     # shape of the cancer data
#Shape of the cancer dataset : (569, 30) :  569 datapoints with 30 features

print("Sample counts per class:\n{}".format(
 {n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))

print("Feature names:\n{}".format(cancer.feature_names))