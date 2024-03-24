import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

# Doit être le même que dans data.py
nombre_colonne = 50

dossier_data = 'datas/'

for fichier in os.listdir(dossier_data):
    # Vérification d'un fichier data
    if not fichier[-4:] == '.csv' and not fichier[:4] == 'data':
        continue
    # Import des données :
    data = pd.read_csv(dossier_data + fichier, sep=',')

    # Affichage du dataframe pandas :
    donnees = [f'a{i}' for i in range(nombre_colonne)]
    donnees.append('type_chute')
    df = pd.DataFrame(data[donnees])

    # Classification par k plus proches voisins :
    model = KNeighborsClassifier(n_neighbors=5)
    y = df['type_chute']
    X = df.drop('type_chute', axis=1)
    model.fit(X, y)
    predictions = model.predict(X)

    # Précision du modèle :
    print(f"\n Précision pour {fichier} :\n", model.score(X, y))

    # Matrice de confusion :
    confusion_matrix = metrics.confusion_matrix(y, predictions)

    # Affichage de la matrice de confusion
    fig, ax = plt.subplots()
    ax.matshow(confusion_matrix)

    type_chute = ['Escalier', 'Marche Arret', 'Marche Rapide', 'Sur Place']

    fig.suptitle(f'Matrice de confusion pour {fichier}')
    ax.set_xticks(np.arange(len(type_chute)))
    ax.set_yticks(np.arange(len(type_chute)))
    ax.set_xticklabels(type_chute)
    ax.set_yticklabels(type_chute)

    for (i, j), z in np.ndenumerate(confusion_matrix):
        ax.text(j, i, '{:0}'.format(z), ha='center', va='center')
    plt.show()
