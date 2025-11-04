import os
import json
from pprint import pprint

dossier_actuel_chemin = os.path.dirname(os.path.abspath(__file__))
fichier_actuel_chemin = os.path.join(dossier_actuel_chemin, "..", "data", "reviews.json")

def loader():
    try:
        with open(fichier_actuel_chemin, 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)
            attribut_chercher = 'review_text'
            ma_list = []  
            for element in donnees:
                if attribut_chercher in element:
                    if element['review_text']:
                        ma_list.append(element)
            return ma_list  
    except FileNotFoundError:
        print("le fichier json est introuvable")
    except json.JSONDecodeError as e:
        print(f"Erreur lors de la lecture du fichier JSON : {e}")

resultat=loader()
pprint(resultat)
