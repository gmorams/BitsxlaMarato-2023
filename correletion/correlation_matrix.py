import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

THRESHOLD_CON_PYLUM = .005
THRESHOLD_UAB_PYLUM = .02

THRESHOLD_CON_FAMILY = .005
THRESHOLD_UAB_FAMILY= 100

THRESHOLD_CON_GENUS = .005
THRESHOLD_UAB_GENUS = .02

PYLUM = 'data/ilumina_pylum.csv'
FAMILY = 'data/iluma-family_level.csv'
GENUS = 'data/iluma-genus.csv'

def crea_mat(df, cas, threshold):

    df['Sample ID'] = df['Sample ID'].apply(lambda x: x[:3])
    df_reduced = df[df['Sample ID'] == cas]
    df_2 = df_reduced.drop(columns=['Sample ID'])

    column_sum = df_2.sum().astype(float)

    filtered_columns = column_sum[column_sum >= threshold].index
    eliminated_columns = column_sum[column_sum < threshold].index

    print(eliminated_columns)

    filtered_df = df[filtered_columns]


    # Calculate correlation matrix
    correlation_matrix = filtered_df.corr()
    # Plot the correlation matrix using seaborn
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.show()

df = pd.read_csv(PYLUM)
crea_mat(df, 'UAB', THRESHOLD_UAB_PYLUM)