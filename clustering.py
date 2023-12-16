import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import numpy as np


# from sklearn.datasets import make_blobs
# from sklearn import metrics
# from sklearn.decomposition import PCA
# from sklearn import preprocessing
# from sklearn.cluster import KMeans
# import scipy.cluster.hierarchy as sch

df = pd.read_csv('data/Metadata_and_relative_abundance_of_seminal_microbiota_from_idiopathic_infertile_patients_and_donors.csv')

# OPCIÓ 1:
# Fer clustering d'individus
# Veure a quin grup pertanyen
# 1. En cas que no apareguin dels 2 grups indescriminadament, cagada pastoret, més difícil de treure conclusions
# 2. En cas que 