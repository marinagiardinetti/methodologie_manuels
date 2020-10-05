# Script de création d'un graphique pour visualier les différents 
# types de manuels en fonction de leurs formats.

# Marina Giardinetti
# École nationale des Chartes
# 2020



# Déclarer la librairie
library(ggplot2)

# Insérer les données récoltées
formats <- c("In-fol", "In-4", "In-8", "In-12", "In-16") 
manuels_dessin <- c(2, 4, 2, 0, 0)
manuels_peinture <- c(0, 3, 9, 1, 0)
manuels_dessin_peinture <- c(3, 3, 4, 3, 2)
data <- cbind(manuels_dessin, manuels_peinture, manuels_dessin_peinture)

# Création du graphique
graph <- barplot(t(data),beside=F,col=c("#0E6655","#7B241C","#34495E"),ylab="Nombre de manuels",names=formats,las=2,horiz=F,
        ylim=c(0,20),xlim=c(0,6),space=0.2, main = "Formats par sujets des manuels")
box()

# Création de la légende
legend(x="topright", cex=0.6,
       legend=c("Manuels de dessin", "Manuels de peinture", "Manuels de dessin et de peinture"), fill=c("#0E6655","#7B241C","#34495E"))


        