import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



THRESHOLD_CON_PYLUM = 0
THRESHOLD_UAB_PYLUM = 0

THRESHOLD_CON_FAMILY = 1.4
THRESHOLD_UAB_FAMILY= 9.5

THRESHOLD_CON_GENUS = 2.45
THRESHOLD_UAB_GENUS = 10.6246

THRESHOLD_CORRELATION = .4

UAB = 'UAB'
CON = 'CON'

PYLUM = 'data/ilumina_pylum.csv'
FAMILY = 'data/iluma-family_level.csv'
GENUS = 'data/iluma-genus.csv'

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

    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.show()
    


df = pd.read_csv(GENUS)
#crea_mat_threshold(df, UAB, THRESHOLD_UAB_PYLUM)

crea_mat_corr(df, CON, THRESHOLD_CON_GENUS)