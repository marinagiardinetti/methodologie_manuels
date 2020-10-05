# Script pour l'étude des titres des manuels de dessin et de peinture.
# Y-a-t'il une évolution de la taille des titres au fil de la période?
# Marina Giardinetti
# Mémoire École des Chartes - 2020



# Librairie pour le graphique
library(ggplot2)

# Import du fichier csv. contenant le numéro d'identification du manuel, le titre entier 
# du manuel, la date de publication
titres_manuels <-read.csv2("titres_manuels.csv", header=TRUE, encoding = 'UTF-8', stringsAsFactors = FALSE)
summary(titres_manuels)

# Exemple: afficher le titre du 4ème manuel
titres_manuels[[4,2]]

# Calcul du nombre de caractères du titre du 4ème manuel
nchar(titres_manuels[4,2])

# Il semble plus pertinent de calculer le nombre de mots plutôt que le nombre de caractères.

# Séléction de la colonne des titres et de celle des dates
colonne_titres <- titres_manuels[,2]
colonne_dates <-titres_manuels[,1]
# On garde la structure de 39 éléments: chaque élément ici devient un vecteur de mots
ma_liste_de_mots <- (strsplit(colonne_titres," ")) 

# Exemple: afficher le titre du 5ème manuel
colonne_titres[5]
# On découpe le titre en mots
strsplit(colonne_titres[5],split = " ")

# Faire une boucle pour accéder aux nombres de mots pour chaque ouvrage:
# D'abord crééer un vecteur rempli de 0 avec autant d'éléments qu'il y aura d'ouvrages
nombre_mots = numeric(nrow(titres_manuels))
for(i in 1:nrow(titres_manuels)){
  nombre_mots[i]<- length(gregexpr(colonne_titres[i],pattern  = " ")[[1]])
}
nombre_mots

# Calculer la moyenne du nombre de mots des 38 manuels
mean(nombre_mots)

# Calculer la médiane dunombre de mots des 38 manuels
median(nombre_mots)

# Création du graphique: 
graphique_bâtons<-barplot(nombre_mots, colonne_dates, names.arg=colonne_dates, 
                          ylab="Nombre de mots par manuels", ylim=c(0,250), main="Évolution de la taille des titres des manuels sur la période")
graphique_bâtons


