import os
import json

# Dossier où se trouve ce script
base_dir = os.path.dirname(__file__)

# Chemin vers reviews.json dans le dossier data
file_path = os.path.join(base_dir, '..', 'data', 'reviews.json')
file_path = os.path.abspath(file_path)

# Vérification que le fichier existe
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Le fichier reviews.json est introuvable : {file_path}")

# Lecture du fichier
with open(file_path, 'r', encoding='utf-8') as fichier:
    data = json.load(fichier)

print(data)
