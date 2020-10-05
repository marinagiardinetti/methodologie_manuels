""""Script de  tokenization, normalisation  et lemmatisation du texte

Marina Giardinetti
École nationale des Chartes
2020
"""

# Librairies utilisées
import nltk
import re
import sys
import stanfordnlp


# Charger le document texte
nouveau_texte=[]
with open("N_Bowle_s_art_of_painting-1783.txt", "r") as f:
	f1 = f.read()


# Tokéniser le texte
texte_tokenise=nltk.word_tokenize(f1)


# Normalisation
	# Supprimer la ponctuation et les chiffres
mots = texte_tokenise
punctuations_chiffres = ['1','2','3','4','5','6','7','8','9','0','!', '"', '#', '$',"'",".", '%', '&',"-", "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
for Mot in mots:
	if Mot not in punctuations_chiffres:
		nouveau_texte.append(Mot)

	# Majuscules => minuscules
texte_minuscule = [line.lower() for line in nouveau_texte]

	# Supprimer les retours à la ligne
texte_normalise = [line.replace("\n", '') for line in texte_minuscule]


# Enregistre ta liste dans ton fichier.txt
with open('N_Bowle_s_art_of_painting-1783_tokens.txt', 'w') as f:
    for item in texte_normalise:
        f.write(f'{item} ')
 
# Récupère ta liste
with open('N_Bowle_s_art_of_painting-1783_tokens.txt', 'r') as f:
    liste = f.read().splitlines()


# Lemmatisation à partir du nouveau fichier de tokens
max_sent_len = 12409608320898
nlp = stanfordnlp.Pipeline(lang="en", processors='tokenize,mwt,pos,lemma', pos_batch_size=max_sent_len)

	# Charger le document texte
nouveau_texte=[]
with open("N_Bowle_s_art_of_painting-1783_tokens.txt", "r") as f:
	f2 = f.read()

	# Lemmatiser
doc = nlp(f2)
with open ('N_Bowle_s_art_of_painting-1783_lemmes.txt', 'w') as f:
	print(*[f'{word.lemma}' for sent in doc.sentences for word in sent.words], sep=' ', file=f)

 
# Récupère ta liste
with open('N_Bowle_s_art_of_painting-1783_lemmes.txt', 'r') as f:
    liste = f.read().splitlines()