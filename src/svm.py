from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

PYLUM = '../data/ilumina_pylum.csv'
FAMILY = '../data/iluma-family_level.csv'
GENUS = '../data/iluma-genus.csv'

# Load the Iris dataset
df = pd.read_csv(FAMILY)
df['Sample ID'] = df['Sample ID'].apply(lambda x: x[:3])
X = df.drop(columns=['Sample ID'])
X = X[['Campylobacteraceae', 'Prevotellaceae', 'Peptostreptococcaceae', 'Oxalobacteraceae', 'Bradyrhizobiaceae', 'Veillonellaceae', 'Lactobacillaceae']]
y = df['Sample ID']


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

print(len(y_train), len(y_test))

# Apply PCA for dimensionality reduction

"""

# Create an SVM classifier
for comp in np.linspace(2,20,1):
    n_components = int(comp)  # Adjust the number of components as needed
    pca = PCA(n_components=n_components)
    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.transform(X_test)
    for g in np.linspace(0.01,1,10):
        for c in np.linspace(.001, 5,20):
            svm_classifier = SVC(kernel='rbf', C=c,gamma=g, class_weight='balanced')

            # Train the SVM classifier on the training data
            svm_classifier.fit(X_train, y_train)

            # Make predictions on the testing data
            predictions = svm_classifier.predict(X_test)
            #print(predictions)

            # Evaluate the accuracy of the model
            accuracy = accuracy_score(y_test, predictions)
            print("C = ", c)
            print("comp = ", comp)
            print("gamma = ", g)
            print(f"Accuracy: {accuracy * 100:.2f}%")

"""
n_components = 2  # Adjust the number of components as needed
pca = PCA(n_components=n_components)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

svm_classifier = SVC(kernel='rbf', C=0.5,gamma=0.01, class_weight='balanced')

# Train the SVM classifier on the training data
svm_classifier.fit(X_train, y_train)
# Make predictions on the testing data
predictions = svm_classifier.predict(X_test)
print(predictions)
print(y_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")

