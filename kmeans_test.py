import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from kmeans import KMeans

def my_test_clusters():
    # generate data
    g1 = np.random.normal(loc=10,scale=1,size=(2,100))
    g2 = np.random.normal(loc=0,scale=1,size=(2,100))
    g3 = np.random.normal(loc=-5,scale=1,size=(2,100))
    data = np.concatenate((g1,g2,g3),axis=1).T
    np.random.shuffle(data)
    train_data = data.tolist()
    #classify
    classifier = KMeans(6)
    classifier.fit(train_data)
    centers = classifier.train()
    print(centers)
    #plot
    sns.scatterplot(x=g1[0],y=g1[1])
    sns.scatterplot(x=g2[0],y=g2[1])
    sns.scatterplot(x=g3[0],y=g3[1])
    for c in centers:
        sns.scatterplot(x=[c[0]],y=[c[1]], marker="x", s=40)
    plt.show()

def official_test():
    classifier = KMeans(3)
    data = KMeans.get_data("input_1.txt")
    classifier.fit(data)
    centers = classifier.train()
    return centers

t = official_test()
for c in t:
    print(c)
