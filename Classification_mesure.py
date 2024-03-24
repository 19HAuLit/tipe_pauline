import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

nombre_colonne = 20
dossier_data = 'datas/'

for fichier in os.listdir(dossier_data):
    if not fichier[-4:] == '.csv':
        continue
    # Import des données :
    data = pd.read_csv(dossier_data + fichier, sep=',')

    # Affichage du dataframe pandas :
    donnees = [f'a{i}' for i in range(nombre_colonne)]
    donnees.append('type_chute')
    df = pd.DataFrame(data[donnees])
    print(df)

    # Classification par k plus proches voisins :
    model = KNeighborsClassifier(n_neighbors=5)
    y = df['type_chute']
    X = df.drop('type_chute', axis=1)
    model.fit(X, y)
    predictions = model.predict(X)

    # Précision du modèle :
    print("\n Précision :\n", model.score(X, y))

    # Matrice de confusion :
    confusion_matrix = metrics.confusion_matrix(y, predictions)

    # Affichage de la matrice de confusion
    fig, ax = plt.subplots()
    ax.matshow(confusion_matrix)

    fig.suptitle(f'Matrice de confusion pour {fichier}')

    for (i, j), z in np.ndenumerate(confusion_matrix):
        ax.text(j, i, '{:0}'.format(z), ha='center', va='center')
    plt.show()
