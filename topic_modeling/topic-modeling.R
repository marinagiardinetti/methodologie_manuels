# Script pour l'étude des titres des manuels de dessin et de peinture.
# Calcul des mots les plus fréquents
# Marina Giardinetti
# Mémoire École des Chartes - 2020


# Librairies nécessaires
library("rJava")
library("mallet")
library("LDAvis")
source("LDAvis_function.R")

# Import du fichier csv. contenant le numéro d'identification du manuel, le titre entier 
# du manuel, la date de publication
titres_manuels <-read.csv("lemmes_titres.tsv", encoding = 'UTF-8', sep = "\t", quote = '', header = TRUE)
summary(titres_manuels)
nrow(titres_manuels)
docs = mallet::mallet.import(rownames(titres_manuels), as.character(titres_manuels[,4]),   "stopwords_long_list.txt", token.regexp = "[\\S]+")


# Charger les documents
topic.model <- MalletLDA(num.topics = 4, alpha.sum = 1, beta = 0.1)
topic.model$loadDocuments(docs)

# Afficher les fréquences de mots
vocabulary <- topic.model$getVocabulary()
head(vocabulary)
word.freqs <- mallet.word.freqs(topic.model)
head(word.freqs)
# Afficher les mots les plus fréquents dans l'ordre de fréquence
tableau<-head(word.freqs[order(word.freqs[, 2], decreasing = TRUE),], n = "40")

# Optimisation des hyperparamètres
topic.model$setAlphaOptimization(20, 50)

# Entraînement du modèle
topic.model$train(200)

# Évaluation des valeurs
topic.model$getAlpha()
topic.model$model$beta

# Probabilité des sujets par documents (normalisés)
doc.topics <- mallet.doc.topics(topic.model, smoothed=TRUE, normalized=TRUE)
topic.words <- mallet.topic.words(topic.model, smoothed=TRUE, normalized=TRUE)

# Afficher les mots les plus caractéristiques de chaque sujet
mallet.topic.labels(topic.model, topic.words = topic.words, 1)
mallet.top.words(topic.model, word.weights = topic.words[1,], num.top.words = 30)

# Afficher le documents ou le sujet 1 est le plys fortement représenté
head(titres_manuels[order(doc.topics[, 1], decreasing = TRUE), 1], n = 200)

# Visualisation avec LDavis
makeLDAvis(topic.model, outDir = tempfile(), openBrowser = TRUE)

# Restrictions par types de manuels
titres_manuels_type = titres_manuels[titres_manuels[,3] == "p",]
nrow(titres_manuels_type)
docs2 = mallet::mallet.import(rownames(titres_manuels_type), as.character(titres_manuels_type[,4]), "stopwords_long_list.txt", token.regexp = "[\\S]+")
topic.model2 <- MalletLDA(num.topics=10, alpha.sum = 1, beta = 0.1)
topic.model2$loadDocuments(docs2)
vocabulary2 <- topic.model2$getVocabulary()
head(vocabulary2)
word.freqs2 <- mallet.word.freqs(topic.model2)
head(word.freqs2)
head(word.freqs2[order(word.freqs2[, 2], decreasing = TRUE),], n = "100")
topic.model2$setAlphaOptimization(20, 50)
topic.model2$train(200)

doc.topics <- mallet.doc.topics(topic.model, smoothed=TRUE, normalized=TRUE)
topic.words <- mallet.topic.words(topic.model, smoothed=TRUE, normalized=TRUE)
mallet.top.words(topic.model, word.weights = topic.words[2,], num.top.words = 5)
makeLDAvis(topic.model, outDir = tempfile(), openBrowser = TRUE)





