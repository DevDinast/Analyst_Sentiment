from cleaner import cleaner
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pprint import pprint
import nltk

def analyst():
    analyst = cleaner()
    analyzer = SentimentIntensityAnalyzer()
    for element in ma_list:
        sentiment_score = analyzer.polarity_scores(element['review_text'])
        #if sentiment_score<
        element['sentiment'] = sentiment_score
    return ma_list

resultat = analyst()
pprint(resultat) 
