import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler


# genus
#df = pd.read_csv('data/iluma-genus.csv')  

# family
df = pd.read_csv('../data/iluma-family_level.csv') 

# pylum
# df = pd.read_csv('data/ilumina_pylum.csv')  

# Select relevant features for clustering, excluir la primera columna de Sample ID  (les primeres 60 cols)
features = df.columns[1:61]

# Normalize the data
df_normalized = df[features].div(df[features].sum(axis=1), axis=0) * 100


for k in range(3,7):   # 4 va be

    # Choose the number of clusters (n_clusters)
    n_clusters = k

    # Perform agglomerative clustering
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    df['cluster'] = model.fit_predict(df[features])


    # Set option to display all rows
    pd.set_option('display.max_rows', None)

   
    # Initialize counters
    contCluster_UAB = np.zeros(n_clusters, dtype=int)
    contCluster_CON = np.zeros(n_clusters, dtype=int)

    # Loop through the DataFrame rows
    for i in range(len(df)):
        sample_id = df.at[i, 'Sample ID']
        cluster_label = df.at[i, 'cluster']

        # Check 'UAB' or 'CON' and update the corresponding counter
        if 'UAB' in sample_id:
            contCluster_UAB[cluster_label] += 1
        elif 'CON' in sample_id:
            contCluster_CON[cluster_label] += 1

    # Print the counts
    print("\nNumero de clusters:", k)
    for cluster_label in range(n_clusters):
        percentage_UAB = contCluster_UAB[cluster_label] / len(df[df['Sample ID'].str.contains('UAB')]) * 100
        print(f"Cluster UAB {cluster_label}: {percentage_UAB:.2f}%")
    print("\n")
    for cluster_label in range(n_clusters):
        percentage_CON = contCluster_CON[cluster_label] / len(df[df['Sample ID'].str.contains('CON')]) * 100
        print(f"Cluster CON {cluster_label}: {percentage_CON:.2f}%")
    print("-------------------")

        
# Visualize the dendrogram
linked = linkage(df_normalized, 'ward')
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Dendrogram')
plt.xlabel('Sample ID')
plt.ylabel('Distance')
plt.show()
        
