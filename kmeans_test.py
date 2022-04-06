import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from kmeans import KMeans

g1 = np.random.normal(loc=10,scale=1,size=(2,10))
g2 = np.random.normal(loc=0,scale=1,size=(2,10))
g3 = np.random.normal(loc=-5,scale=1,size=(2,10))
data = np.concatenate((g1,g2,g3),axis=1).T
np.random.shuffle(data)
train_data = data.tolist()

classifier = KMeans(3)
classifier.fit(train_data)
centers = classifier.train()
print(centers)