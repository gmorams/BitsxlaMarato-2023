# amb network
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from sklearn.cluster import AgglomerativeClustering

# Load the data
df = pd.read_csv('../data/iluma-family_level.csv')

# Select relevant features for clustering, excluding the first column of Sample ID (the first 60 cols)
features = df.columns[1:61]

# Choose the number of clusters
n_clusters = 4

# Perform agglomerative clustering
model = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
df['cluster'] = model.fit_predict(df[features])

# Select samples from Cluster 2
cluster_2_samples = df[df['cluster'] == 2]

# Create a graph
G = nx.Graph()

# Add nodes (features)
for feature in features:
    G.add_node(feature)

# Add edges based on correlation
for i in range(len(features)):
    for j in range(i + 1, len(features)):
        feature_i = features[i]
        feature_j = features[j]
        correlation = cluster_2_samples[[feature_i, feature_j]].corr().iloc[0, 1]
        if correlation > 0.8:
            G.add_edge(feature_i, feature_j)

# Draw the graph with a larger figure size
fig, ax = plt.subplots(figsize=(20, 10))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_size=8, font_color="black", font_weight="bold", node_size=800, node_color="skyblue", edge_color="gray", linewidths=0.5, arrows=False, ax=ax)
plt.title('Graph of Correlated Features in Cluster 2', fontsize=16)
plt.show()

