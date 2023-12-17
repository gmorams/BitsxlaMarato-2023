import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, DBSCAN
import numpy as np
from sklearn.neighbors import NearestNeighbors


# from sklearn.datasets import make_blobs
# from sklearn import metrics
# from sklearn.decomposition import PCA
# from sklearn import preprocessing
# from sklearn.cluster import KMeans
# import scipy.cluster.hierarchy as sch

df = pd.read_csv('../data/ilumina_pylum.csv')
df.set_index('Sample ID', inplace=True)

# OPCIÓ 1:
# Fer clustering d'individus
# Veure a quin grup pertanyen
# 1. En cas que no apareguin dels 2 grups indescriminadament, cagada pastoret, més difícil de treure conclusions
# 2. En cas que 

def DBSCAN_clustering(dd):
    n_clust = []
    for i in range(1, 50):
        clustering = DBSCAN(eps=i).fit(dd)
        labels = clustering.labels_

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)
        n_clust.append(n_clusters_)
        print(i, n_clusters_)
    plt.plot(n_clust)
    # plt.xlabel('Data Point Index')
    # plt.ylabel('Epsilon (distance to kth nearest neighbor)')
    plt.savefig('clusters')
    # Max number of clusters: 4 at epsilon 22

    clustering = DBSCAN(eps=9).fit(dd)
    labels = clustering.labels_
    
    clusters = {'UAB': {i:0 for i in range(-1,4)}, 'CON': {i:0 for i in range(-1,4)}}
    for i, label in enumerate(labels):
        print(f"Index {dd.index[i]}: Cluster Label {label}")

        clusters[dd.index[i][:3]][label] += 1
    print('CLUSTERS UAB:',clusters['UAB'])
    print('CLUSTERS CON:',clusters['CON'])
y
DBSCAN_clustering(df)
