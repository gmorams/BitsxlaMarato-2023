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

# Calculate the correlation matrix for Cluster 2 samples
correlation_matrix_cluster_2 = cluster_2_samples[features].corr()

# Select the top 200 correlated features
top_200_correlated_features = correlation_matrix_cluster_2.abs().unstack().sort_values(ascending=False).drop_duplicates().index[:200]

# Convert MultiIndex to regular Index
top_200_correlated_features = pd.Index([col[0] for col in top_200_correlated_features])

# Create a graph
G = nx.Graph()

# Add nodes (features)
for feature in top_200_correlated_features:
    G.add_node(feature)

# Add edges based on correlation (excluding edges to itself)
for i in range(len(top_200_correlated_features)):
    for j in range(i + 1, len(top_200_correlated_features)):
        feature_i = top_200_correlated_features[i]
        feature_j = top_200_correlated_features[j]
        correlation = correlation_matrix_cluster_2.loc[feature_i, feature_j]
        if correlation > 0.8 and feature_i != feature_j:
            G.add_edge(feature_i, feature_j)

# Draw the graph with a larger figure size
fig, ax = plt.subplots(figsize=(20, 10))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_size=8, font_color="black", font_weight="bold", node_size=900, node_color="skyblue", edge_color="gray", linewidths=0.5, arrows=False, ax=ax)
plt.title('Graph of Top 200 Correlated Features in Cluster 2', fontsize=14)
plt.show()
