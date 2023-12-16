from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import  DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

PYLUM = '../data/ilumina_pylum.csv'
FAMILY = '../data/iluma-family_level.csv'
GENUS = '../data/iluma-genus.csv'

# Load the Iris dataset
df = pd.read_csv(FAMILY)
df['Sample ID'] = df['Sample ID'].apply(lambda x: x[:3])
X = df.drop(columns=['Sample ID'])
y = df['Sample ID']


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Apply PCA for dimensionality reduction

n_components = 20  # Adjust the number of components as needed
pca = PCA(n_components=n_components)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

tree_classifier = DecisionTreeClassifier(max_depth=4)

# Train the SVM classifier on the training data
tree_classifier.fit(X_train, y_train)
# Make predictions on the testing data
predictions = tree_classifier.predict(X_test)
#print(predictions)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")
tree.plot_tree(tree_classifier)
plt.show()