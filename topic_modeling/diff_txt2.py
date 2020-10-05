""" Script de calcul des similitudes entre deux textes


Marina Giardinetti
École Nationale des Chartes
2020
"""

# Libraires utilisées
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer



# Nettoyer et normaliser les textes
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


# Charger les textes à comparer
nouveau_texte=[]
with open("N_De_arte_graphica;_or,_the_art_of_painting-1765_tokens.txt", "r") as f:
	text1 = f.read()

nouveau_texte=[]
with open("N_Bowles_s_youth_assistant_in_drawing-1791_tokens.txt", "r") as f:
	text2 = f.read()



print("La Similarité est :",cosine_sim(text1, text2))




