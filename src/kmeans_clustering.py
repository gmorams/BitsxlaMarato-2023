import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
 
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')


# Cargar tus datos desde el archivo CSV
data = pd.read_csv('iluma-family_level.csv')

# Seleccionar las columnas de bacterias para el clustering
bacteria_columns = data.columns[1:]  # Ajusta esto según la estructura de tu archivo CSV

# Filtrar solo las columnas de bacterias
bacteria_data = data[bacteria_columns]

# Normalizar los datos (especialmente importante para K-Means)
scaler = StandardScaler()
bacteria_data_scaled = scaler.fit_transform(bacteria_data)

# Probar diferentes valores de k
k_values = range(2, 11)  # Puedes ajustar este rango según tus necesidades
scores = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(bacteria_data_scaled)
    score = kmeans.score(bacteria_data_scaled)
    scores.append(score)  # Convertir a positivo para que un score más alto sea mejor

# Graficar Elbow Curve usando score
plt.figure(figsize=(10, 6))
plt.plot(k_values, scores, marker='o')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()