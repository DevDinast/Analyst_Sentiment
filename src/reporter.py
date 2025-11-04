import json
from analyzer import analyst  
import os
import csv

# Chemin du dossier output
dossier_actuel_chemin = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(dossier_actuel_chemin, "..", "output")
os.makedirs(output_dir, exist_ok=True)

# Fichiers de sortie
fichier_json = os.path.join(output_dir, "summary.json")
fichier_csv = os.path.join(output_dir, "results.csv")

def reporter():
    avis_analyzes = analyst()

    total_avis = len(avis_analyzes)
    positifs = sum(1 for a in avis_analyzes if a["sentiment"]["label"] == "positif")
    negatifs = sum(1 for a in avis_analyzes if a["sentiment"]["label"] == "negatif")
    neutres = sum(1 for a in avis_analyzes if a["sentiment"]["label"] == "neutre")

    # Création du rapport JSON
    rapport = {
        "total_avis": total_avis,
        "positifs": positifs,
        "negatifs": negatifs,
        "neutres": neutres,
        "details": avis_analyzes
    }

    # 🔹 Sauvegarde JSON
    with open(fichier_json, "w", encoding="utf-8") as f:
        json.dump(rapport, f, indent=4, ensure_ascii=False)
    print(f"\n✅ Rapport JSON sauvegardé dans '{fichier_json}'")

    # 🔹 Création du CSV avec sentiment_final
    # Récupère toutes les clés du premier avis pour faire les colonnes
    if avis_analyzes:
        colonnes = list(avis_analyzes[0].keys()) + ["sentiment_final"]
        with open(fichier_csv, "w", encoding="utf-8", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=colonnes)
            writer.writeheader()
            for avis in avis_analyzes:
                ligne = avis.copy()
                ligne["sentiment_final"] = avis["sentiment"]["label"]
                writer.writerow(ligne)
        print(f"✅ Fichier CSV sauvegardé dans '{fichier_csv}'")

    # 🔹 Affichage console
    print("\n=== RAPPORT DES AVIS ===")
    print(f"Nombre total d'avis : {total_avis}")
    print(f" - Avis positifs : {positifs}")
    print(f" - Avis négatifs : {negatifs}")
    print(f" - Avis neutres  : {neutres}")

# Appel de la fonction
reporter()
