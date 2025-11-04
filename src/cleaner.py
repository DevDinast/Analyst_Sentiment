from loader import loader
import nltk
from pprint import pprint
import re
import emoji
import unicodedata

def cleaner():
 ma_liste1=loader()
 ma_liste2=[]
 for element in ma_liste1:
    text = element['review_text'].lower().strip()
    text=emoji.replace_emoji(text,'')
    text = re.sub(r"http\S+|www\S+|URL:|Code produit:\s*\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

    ma_liste2.append(text)
 return ma_liste2 

