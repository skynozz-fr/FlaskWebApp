# Devoir Python - Gestion d'un site web avec Flask

## Introduction
Ce projet consiste à développer un site web simple utilisant le framework Flask en Python. Le site permet l'inscription, la connexion et la déconnexion des utilisateurs, ainsi que l'accès à différentes pages en fonction de leur statut de connexion.

## Structure du projet
- **app.py** : Le fichier principal de l'application Flask, contenant toutes les routes et la logique métier.
- **database.py** : Ce fichier contient la classe `MySQLDatabase` qui gère la connexion à la base de données MySQL.
- **templates/** : Ce répertoire contient tous les fichiers HTML utilisés pour afficher les pages du site.
- **static/** : Ce répertoire contient les fichiers statiques tels que les fichiers CSS, JavaScript, les images, etc.
- **sql/** : Ce répertoire contient le script SQL pour la création de la base de données.

## Configuration
Avant de lancer l'application, assurez-vous de configurer les informations de connexion à votre base de données MySQL dans le fichier app.py :
```python
# Connexion à la base de données MySQL
db = MySQLDatabase(host="localhost", user="votre_utilisateur", password="votre_mot_de_passe", database="FlaskSql")
