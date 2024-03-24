import os

import pandas as pd

chemin_fichier_data_ax = 'datas/data_ax.csv'
chemin_fichier_data_ay = 'datas/data_ay.csv'
chemin_fichier_data_az = 'datas/data_az.csv'
chemin_fichier_data_atotal = 'datas/data_atotal.csv'
dossier_datas_brute = 'datas/brut/'
nombre_colonne = 20
sep = ","

# Création des fichiers de data

with open(chemin_fichier_data_ax, 'w') as file:
    for i in range(nombre_colonne):
        file.write(f'a{i}{sep}')
    file.write('type_chute\n')
    print('Fichier data ax créée')

with open(chemin_fichier_data_ay, 'w') as file:
    for i in range(nombre_colonne):
        file.write(f'a{i}{sep}')
    file.write('type_chute\n')
    print('Fichier data ay créée')

with open(chemin_fichier_data_az, 'w') as file:
    for i in range(nombre_colonne):
        file.write(f'a{i}{sep}')
    file.write('type_chute\n')
    print('Fichier data az créée')

with open(chemin_fichier_data_atotal, 'w') as file:
    for i in range(nombre_colonne):
        file.write(f'a{i}{sep}')
    file.write('type_chute\n')
    print('Fichier data atotal créée')

# Ajout des données brut au fichier data

for fichier in os.listdir(dossier_datas_brute):
    # Import données
    data = pd.read_csv(dossier_datas_brute + fichier, sep=',')

    # Définition du type de chute
    type_chute = -1
    if fichier.startswith('escalier'):
        type_chute = 0
    elif fichier.startswith('marche_arret'):
        type_chute = 1
    elif fichier.startswith('marche_rapide'):
        type_chute = 2
    elif fichier.startswith('sur_place'):
        type_chute = 3

    # Création du dataframe pandas :
    donnees = ['time', 'ax', 'ay', 'az', 'atotal']
    df = pd.DataFrame(data[donnees])

    if df.shape[0] < nombre_colonne:
        print(f'Le fichier {fichier} ne contient pas assez de données')
    else:
        ax_list = [element for element in df['ax']]
        ay_list = [element for element in df['ay']]
        az_list = [element for element in df['az']]
        atotal_list = [element for element in df['atotal']]

        with open(chemin_fichier_data_ax, 'a') as file:
            for i in range(int((df.shape[0] - nombre_colonne) / 2), int((df.shape[0] + nombre_colonne) / 2)):
                file.write(f'{ax_list[i]}{sep}')
            file.write(f'{type_chute}\n')

        with open(chemin_fichier_data_ay, 'a') as file:
            for i in range(int((df.shape[0] - nombre_colonne) / 2), int((df.shape[0] + nombre_colonne) / 2)):
                file.write(f'{ay_list[i]}{sep}')
            file.write(f'{type_chute}\n')

        with open(chemin_fichier_data_az, 'a') as file:
            for i in range(int((df.shape[0] - nombre_colonne) / 2), int((df.shape[0] + nombre_colonne) / 2)):
                file.write(f'{az_list[i]}{sep}')
            file.write(f'{type_chute}\n')

        with open(chemin_fichier_data_atotal, 'a') as file:
            for i in range(int((df.shape[0] - nombre_colonne) / 2), int((df.shape[0] + nombre_colonne) / 2)):
                file.write(f'{atotal_list[i]}{sep}')
            file.write(f'{type_chute}\n')
