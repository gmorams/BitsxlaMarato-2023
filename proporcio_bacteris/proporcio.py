import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df_pylum = pd.read_csv('../data/ilumina_pylum.csv')
df_family = pd.read_csv('../data/iluma-family_level.csv')
df_genus = pd.read_csv('../data/iluma-genus.csv')

df_pylum['Sample ID'] = df_pylum['Sample ID'].apply(lambda x: x[:3])
df_family['Sample ID'] = df_family['Sample ID'].apply(lambda x: x[:3])
df_genus['Sample ID'] = df_genus['Sample ID'].apply(lambda x: x[:3])

def filtrar_casos(df):    
    df['Sample ID'] = df['Sample ID'].apply(lambda x: x[:3])
    df_UAB = df[df['Sample ID'] == 'UAB']
    df_CON = df[df['Sample ID'] == 'CON']
    df_UAB = df_UAB.drop(columns=['Sample ID'])
    df_CON = df_CON.drop(columns=['Sample ID'])
    df_CON.reset_index(inplace=True)

    return df_UAB, df_CON

def calcular_shannon(df): 
    num_cases = len(df)
    shannon = {i:0 for i in range(num_cases)}

    # Iterem sobre les bacteries
    for col in df.columns:
        # Iterem sobre els casos, per calcular l'índex
        for i in range(num_cases):
            proporcio = float(df[col][i])/100
            if proporcio > 0:
                shannon[i] -= proporcio*math.log10(proporcio)  
    return shannon

dfs = [df_pylum, df_family, df_genus]

shannon_means =[]
shannon_std = []
for df in dfs:
    df_UAB, df_CON = filtrar_casos(df_pylum)

    shannon_result_UAB = calcular_shannon(df_UAB)
    shannon_result_CON = calcular_shannon(df_CON)
    
    shannon_result_mean_UAB = sum(shannon_result_UAB.values())/len(shannon_result_UAB)
    shannon_result_mean_CON = sum(shannon_result_CON.values())/len(shannon_result_CON)

    shannon_result_variance_UAB = sum([((x - shannon_result_mean_UAB) ** 2) for x in shannon_result_UAB.values()]) / len(shannon_result_UAB.values()) 
    shannon_result_variance_CON = sum([((x - shannon_result_mean_CON) ** 2) for x in shannon_result_CON.values()]) / len(shannon_result_CON.values()) 


    shannon_means.append((shannon_result_mean_UAB, shannon_result_mean_CON))
    shannon_std.append((shannon_result_variance_UAB, shannon_result_variance_CON))


print('________________')
print('PYLUM:')
print('Patients diversity:', 'MEAN:', shannon_means[0][0], 'VARIANCE:', shannon_std[0][0])

print('Control diversity:', 'MEAN:', shannon_means[0][1], 'VARIANCE:', shannon_std[0][1])
print('________________')

print('FAMILY:')
print('Patients diversity:', 'MEAN:', shannon_means[1][0], 'VARIANCE:', shannon_std[1][0])
print('Control diversity:', 'MEAN:', shannon_means[1][1], 'VARIANCE:', shannon_std[1][1])
print('________________')

print('GENUS:')
print('Patients diversity:', 'MEAN:', shannon_means[2][0], 'VARIANCE:', shannon_std[2][0])
print('Control diversity:', 'MEAN:', shannon_means[2][1], 'VARIANCE:', shannon_std[2][1])



