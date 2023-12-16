import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


data = pd.read_csv('data/pylum_level.csv')
data.set_index('Sample ID', inplace=True)

TWSS = []

for k in np.arange(1,11):
    km = KMeans(n_init=10, init='random',n_clusters = k, random_state=7).fit(data)
    TWSS.append(km.inertia_)

print(TWSS)

plt.plot(TWSS)
plt.savefig('clusters')