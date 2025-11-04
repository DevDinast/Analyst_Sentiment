from loader import loader
from textblob import TextBlob
import re
import emoji
import unicodedata

def cleaner():
    """
    Nettoie les textes des avis pour améliorer l'analyse de sentiment.
    - Convertit en minuscules
    - Remplace les emojis par des tokens
    - Remplace les nombres par [nombre]
    - Supprime les URLs et codes produits
    """
    ma_liste1 = loader()
    ma_liste2 = []

    for element in ma_liste1:
        text = element['review_text'].lower().strip()

        # Remplacer les emojis par des tokens
        text = emoji.demojize(text)  # ex: ":smile:" au lieu de supprimer

        # Remplacer URLs et codes produits
        text = re.sub(r"http\S+|www\S+|URL:|Code produit:\s*\S+", "", text)

        # Remplacer tous les nombres par [nombre]
        text = re.sub(r"\d+", "[nombre]", text)

        # Supprimer les caractères spéciaux inutiles mais garder la ponctuation
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

        ma_liste2.append({
            "reviews_id": element["review_id"],
            "reviews_text": text
        })

    return ma_liste2