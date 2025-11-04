# main.py
from loader import loader
from cleaner import cleaner
from analyzer import analyst
from reporter import reporter

def main():
    
    print("🚀 Démarrage du programme ...")

    # 1️⃣ Charger les avis bruts
    avis = loader()

    # 2️⃣ Nettoyer les textes
    avis_nettoyes = cleaner(avis)

    # 3️⃣ Analyser les sentiments
    avis_analyzes = analyst(avis_nettoyes)

    # 4️⃣ Générer le rapport et les fichiers
    reporter(avis_analyzes)

    print("\n Pipeline terminé avec succès !")


    resultat=main()
    print (resultat)
