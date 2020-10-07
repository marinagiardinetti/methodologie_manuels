""" Script de reconstitution informatique des instructions d'un manuel de dessin: 
The Principles of drawing, 1764. Dessin du visage.

Python3.7
Marina Giardinetti
Gabriel Maire
2020
"""

# Librairies utilisées
import numpy as np
import cv2

# Création de la matrice de données vide
	# La planche de dessin
canvas = np.ones((600,600,3), dtype="uint8") * 255

# Dessiner l'oval
	# Le placement sur la feuille, la forme (d'un oeuf) et les mesures:
center_coordinates = (300,300) 
axesLength = (120, 200) 
angle = 360
startAngle = 0
endAngle = 360
color = (0, 0, 0) 
thickness = 2
	# Dessin de l'oval:
image= cv2.ellipse(canvas, center_coordinates,axesLength,angle,startAngle,endAngle,color,thickness)  

# Paramètres pour les traits / esquisses du visage (à effacer ensuite)
thickness2 = 1
#color2=('w')

# Dessiner la droite qui divise en 2 le visage
	# Mesures de la droite
start1=(0,300)
end1=(600,300)
	# Tracer la droite
droite=cv2.line(canvas,start1,end1,color,thickness2)

# Dessiner la première droite divisant le visage en 4 parties (gauche)
	# Mesures de la droite
start2=(0,400)
end2=(600,400)
	# Tracer la droite
droite2=cv2.line(canvas,start2,end2,color,thickness2)

# Dessiner la dernière droite divisant le visage en 4 partie (droite)
	# Mesures de la droite
start3=(0,200)
end3=(600,200)
	# Tracer la droite
droite3=cv2.line(canvas,start3,end3,color,thickness2)

# Dessiner la droite qui divise la largeur à gauche
	# Mesures de la droite
start4=(276,0)
end4=(276,600)
	# Tracer la droite
droite4=cv2.line(canvas,start4,end4,color,thickness2)

# Dessiner la deuxième droite dans la largeur du visage
	# Mesures de la droite
start5=(228,0)
end5=(228,600)
	# Tracer la droite
droite5=cv2.line(canvas,start5,end5,color,thickness2)

# Dessiner la troisième droite dans la largeur du visage
	# Mesures de la droite
start6=(324,0)
end6=(324,600)
	# Tracer la droite
droite6=cv2.line(canvas,start6,end6,color,thickness2)

# Dessiner la dernière droite dans la largeur du visage
	# Mesures de la droite
start7=(376,0)
end7=(376,600)
	# Tracer la droite
droite7=cv2.line(canvas,start7,end7,color,thickness2)

# Dessiner les yeux
	# Mesures pour les yeux
im2=(24,50) 
	# Tracer le premier oeil
centre_yeux1=(250,250)
yeux1= cv2.ellipse(canvas, centre_yeux1,im2,angle,startAngle,endAngle,color,thickness)  
	# Tracer le deuxième oeil
centre_yeux2=(350,250)
yeux2= cv2.ellipse(canvas, centre_yeux2,im2,angle,startAngle,endAngle,color,thickness)  

# Dessiner le nez
	# Mesures pour le nez
im3=(30,20)
centre_nez=(300,350)
	# Tracer le nez
nez=cv2.ellipse(canvas, centre_nez,im3,angle,startAngle,endAngle,color,thickness) 

# Dessiner la bouche
	# Mesures pour la bouche
angle=180
startAngle = -180
endAngle= 0
im2=(40,20) 
thickness3 = 6
centre_bouche=(300,400)
	# Tracer la bouche
bouche= cv2.ellipse(canvas, centre_bouche,im2,angle,startAngle,endAngle,color,thickness3)  

# Enregistrer le dessin créée
window_name = "image" 
cv2.imwrite('image.png',image)