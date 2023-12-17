import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import pygraphviz as pgv



THRESHOLD_CON_PYLUM = 0
THRESHOLD_UAB_PYLUM = 0

THRESHOLD_CON_FAMILY = 1.4
THRESHOLD_UAB_FAMILY= 4.5

THRESHOLD_CON_GENUS = 2.45
THRESHOLD_UAB_GENUS = 10.6246

THRESHOLD_CORRELATION = .4
LOWER_THRESHOLD_CORRELATION = -.25

UAB = 'UAB'
CON = 'CON'

PYLUM = '../data/ilumina_pylum.csv'
FAMILY = '../data/iluma-family_level.csv'
GENUS = '../data/iluma-genus.csv'

def crea_mat_threshold(df, cas, threshold):

    df['Sample ID'] = df['Sample ID'].apply(lambda x: x[:3])
    df_reduced = df[df['Sample ID'] == cas]
    df_2 = df_reduced.drop(columns=['Sample ID'])

    column_sum = df_2.sum().astype(float)

    filtered_columns = column_sum[column_sum >= threshold].index
    eliminated_columns = column_sum[column_sum < threshold].index

    print(eliminated_columns)

    filtered_df = df[filtered_columns]

    correlation_matrix = filtered_df.corr()

    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.show()

def crea_mat_corr(df, cas, threshold):

    df['Sample ID'] = df['Sample ID'].apply(lambda x: x[:3])
    df_reduced = df[df['Sample ID'] == cas]
    df_2 = df_reduced.drop(columns=['Sample ID'])

    column_sum = df_2.sum().astype(float)

    filtered_columns = column_sum[column_sum >= threshold].index
    eliminated_columns = column_sum[column_sum < threshold].index

    print(eliminated_columns)

    filtered_df = df[filtered_columns]

    correlation_matrix = filtered_df.corr()

    cor_matrix = filtered_df.corr().abs()

    # Selecting upper triangle of correlation matrix
    upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),
                                      k=1).astype(bool))
    print(); print(upper_tri)

    # Finding index of feature columns with correlation greater than 0.95
    to_keep = [column for column in upper_tri.columns if any((THRESHOLD_CORRELATION < cor_matrix[column]) & (cor_matrix[column] < 1))]
    print("to drop"); print(to_keep)

    # Droping Marked Features
    df1 = filtered_df[to_keep]
    print(); print(df1)

    correlation_matrix = df1.corr()

    return correlation_matrix

def print_mat(correlation_matrix):

    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.show()


def draw_graph(corr_matrix):
    G = nx.Graph()
    G.add_nodes_from(corr_matrix.columns)

    # Add edges based on the correlation values
    for i in range(len(corr_matrix.columns)):
        for j in range(i + 1, len(corr_matrix.columns)):
            correlation_value = corr_matrix.iloc[i, j]
            if correlation_value > 0.5 or correlation_value < -0.2:  # You can adjust the threshold as needed
                edge_color = 'green' if correlation_value > 0 else 'red'
                G.add_edge(corr_matrix.columns[i], corr_matrix.columns[j], color=edge_color)

    # Draw the graph
    pos = nx.spring_layout(G)  # You can use different layout algorithms

    # Extract edge colors from edge attributes
    edge_colors = [G[u][v]['color'] for u, v in G.edges()]

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=1000, font_size=8, edge_color=edge_colors, linewidths=2)

    # Draw edge labels with correlation values
    edge_labels = {(u, v): f"{G[u][v]['color']} {corr_matrix.loc[u, v]:.2f}" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title('Graph based on Correlation Matrix')
    plt.show()

def create_graph(corr_matrix):
    G = nx.Graph()
    G.add_nodes_from(corr_matrix.columns)

    # Add edges based on the correlation values
    for i in range(len(corr_matrix.columns)):
        for j in range(i + 1, len(corr_matrix.columns)):
            correlation_value = corr_matrix.iloc[i, j]
            if correlation_value > THRESHOLD_CORRELATION or correlation_value < LOWER_THRESHOLD_CORRELATION:  # You can adjust the threshold as needed
                edge_color = 'green' if correlation_value > 0 else 'red'
                edge_width = abs(correlation_value) * 20  # Adjust the multiplier for edge width
                G.add_edge(corr_matrix.columns[i], corr_matrix.columns[j], color=edge_color, width=edge_width)

    # Export the graph to a .dot file
    nx.drawing.nx_agraph.write_dot(G, "correlation_graph.dot")

    # Plot the .dot file using PyGraphviz
    graph = pgv.AGraph("correlation_graph.dot")
    graph.layout(prog="circo")  # Use a layout algorithm, e.g., "neato"

    for edge in graph.edges():
        edge_color = G[edge[0]][edge[1]]['color']
        edge_width = G[edge[0]][edge[1]]['width']
        edge.attr.update(color=edge_color, penwidth=edge_width)

    # Save the plot as an image (optional)
    output_image_file = "correlation_graph.png"
    graph.draw(output_image_file, format="png", prog="circo")


df = pd.read_csv(PYLUM)
#crea_mat_threshold(df, UAB, THRESHOLD_UAB_PYLUM)

corr_mat = crea_mat_corr(df, UAB, THRESHOLD_UAB_PYLUM)
#print_mat(corr_mat)
#draw_graph(corr_mat)
create_graph(corr_mat)
