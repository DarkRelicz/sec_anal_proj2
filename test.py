# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# reading the data and looking at the first five rows of the data
data=pd.read_csv("Wholesale customers data.csv")
print(data.head())

# statistics of the data
print(data.describe())