"""
Essai de script pour la détéction automatique des formes.
Non achevé. Il détecte quand même les formes humaines; il faut l'adapter à tout un corpus (et non)
une seule image comme c'est le cas ici.





"""





from imageai.Detection import ObjectDetection
import os
import cv2

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path ,
 "Principles of drawing-1785_000028.jpg"), output_image_path=os.path.join(execution_path , "imagenew2.jpg"))

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    print("--------------------------------")
