""""Script de nettoyage du texte:
- suppression des chiffres
- suppression des lettres seules (erreurs d'océrisation)

Marina Giardinetti
École nationale des Chartes
2020
"""

# Librairies utilisées
import os
import re
import sys

# Importer le texte
nouveau_texte=[]
with open("The_artist_s_vade-mecum-1776.txt", "r") as f:
	f1 = f.read()

# Expression régulière pour les lettres seules
exp = r'(?i)\b[a-zA-Z]\b'
content = re.sub(exp, "", f1, flags=re.M)

# Expression régulière pour les chiffres
exp2 = r'(\d+)[^ ]*'
content2 = re.sub(exp2, "", content, flags=re.M)

# Enregistrer le texte nettoyé dans un nouveau fichier texte
with open('N_The_artist_s_vade-mecum-1776.txt', 'w') as f:
    f.write(content2)

















