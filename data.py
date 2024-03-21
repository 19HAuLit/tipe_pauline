import pandas as pd
import os


data = pd.read_csv('acceleration_2023-11-09_17-57-14.csv',sep=',')

#Affichage du dataframe pandas :
donnees = ['time','ax','ay','az','atotal']
df=pd.DataFrame(data[donnees])

ax_list = [element for element in df['ax']]

nom_fichier = 'data_ax.csv'

if not os.path.exists(nom_fichier):
    with open(nom_fichier, 'w') as file:
        for i in range(len(ax_list)):
            file.write(f'a{i},')
        file.write('type_chute\n')
        print('Fichier créée')


with open(nom_fichier, 'a') as file:
    for ax in ax_list:
        file.write(f'{ax},')
    file.write('0\n')
    print('Nouvelle données ajoutées')