# Script de création de deux graphiques en diagramme circulaires
# pour la visualisation des différents formats au début et à la fin
# de la période: 1735-1774 et 1775-1805

# Marina Giardinetti
# École nationale des Chartes
# 2020



# Déclarer la librairie
library(ggplot2)

# In-fol = 1 / In-4 = 2 / In-8 = 3 / In-12 = 4 / In-16 = 5
# Création du tableau de données (1735-1774)
df <- data.frame(
  Formats = c("1", "2", "3", "4", "5"),
  Manuels = c(2, 7, 9, 7, 2)
)
head(df)

# Création d'un premier graphique
graph <- ggplot(df, aes(x="", y=Manuels, fill=Formats)) +
  geom_bar(width = 1, stat = "identity")
graph

# Définition d'un thème pour les diagrammes circulaires
blank_theme <- theme_minimal()+
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    plot.title=element_text(size=14, face="bold")
  )

# Création du preier diagramme circulaire
cam <- graph + coord_polar("y", start=0)
cam + scale_fill_brewer(palette="Blues") + blank_theme + theme(axis.text.x=element_blank())



# Création du tableau de données (1775-1805)
df2 <- data.frame(
  Formats = c("1", "2", "3", "4", "5"),
  Manuels = c(3, 10, 12, 3, 0)
)
head(df)

# Création du deuxième graphique
graph2 <- ggplot(df2, aes(x="", y=Manuels, fill=Formats)) +
  geom_bar(width = 1, stat = "identity")
graph2

# Création du deuxième diagramme circulaire
cam2 <- graph2 + coord_polar("y", start=0)
cam2 + scale_fill_brewer(palette="Blues") + blank_theme + theme(axis.text.x=element_blank())
