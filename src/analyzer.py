from cleaner import cleaner
from pprint import pprint
from textblob_fr import PatternTagger, PatternAnalyzer
from textblob import Blobber

# Crée un Blobber FR
tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

def analyst():
    new_list2 = cleaner()
    ma_liste3 = []

    for element in new_list2:
        text = element["reviews_text"]
        if not text.strip():  # Gestion des avis vides
            sentiment = {'polarity': 0.0, 'subjectivity': 0.0}
        else:
            blob = tb(text)
            sentiment = {'polarity': blob.sentiment[0], 'subjectivity': blob.sentiment[1]}

        element['sentiment'] = sentiment
        ma_liste3.append(element)

    return ma_liste3

resultats = analyst()
pprint(resultats)
