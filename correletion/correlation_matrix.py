import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



THRESHOLD_CON_PYLUM = .005
THRESHOLD_UAB_PYLUM = .02

THRESHOLD_CON_FAMILY = 5
THRESHOLD_UAB_FAMILY= 15

THRESHOLD_CON_GENUS = 3.5
THRESHOLD_UAB_GENUS = 14

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

    correlation_matrix_filtered = correlation_matrix[correlation_matrix.abs() >= .5]

    above_threshold_names = correlation_matrix_filtered.stack().index.tolist()

    sns.heatmap(correlation_matrix_filtered, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.show()

df = pd.read_csv(PYLUM)
#crea_mat_threshold(df, UAB, THRESHOLD_UAB_PYLUM)

crea_mat_corr(df, UAB, THRESHOLD_UAB_PYLUM)