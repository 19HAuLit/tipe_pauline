# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 08:58:27 2023

@author: Yohan
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


#Import des données :
data = pd.read_csv('donne _final_11.csv',sep=';')

#Affichage du dataframe pandas :
donnees = ['a1','a2','a3','a4','a5','a6','a7','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18','a19','a20','a21','a22','a23','a24','a25','a26','a27','type_chute']
df=pd.DataFrame(data[donnees])
print(df)


#Classification par k plus proches voisins :
model= KNeighborsClassifier(n_neighbors=5)
y = df['type_chute']
X = df.drop('type_chute',axis=1)
model.fit(X,y)
predictions = model.predict(X)


#Précision du modèle :
print("\n Précision :\n",model.score(X,y))

#Matrice de confusion :
from sklearn import metrics
confusion_matrix = metrics.confusion_matrix(y, predictions)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['Chute classique', 'Chute roulade (avalanche)'])
cm_display.plot()
plt.show()





