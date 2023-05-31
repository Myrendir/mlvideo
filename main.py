import cv2
import numpy as np
import face_recognition
import requests
from PIL import Image
import io
import os
from flask import Flask, jsonify

app = Flask(__name__)
last_image = 'http://45.147.99.71:3000/api/images/last'
image_dir = './images'

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []

person_id = 'person'

# Charger les images des visages connus
known_faces = []
known_names = []

for dir_name in os.listdir(image_dir):
    dir_path = os.path.join(image_dir, dir_name)
    if os.path.isdir(dir_path):
        for image_name in os.listdir(dir_path):
            image_path = os.path.join(dir_path, image_name)
            if os.path.isfile(image_path):
                img = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(img)[0]
                known_faces.append(encodings)
                known_names.append(dir_name)


@app.route('/')
def detect_faces():
    # Récupérer l'URL de la dernière image depuis l'API
    response = requests.get(last_image)
    img = Image.open(io.BytesIO(response.content))
    img = np.array(img)

    # Faire la reconnaissance faciale
    faces = face_recognition.face_locations(img)
    encodings = face_recognition.face_encodings(img, faces)

    for face_encoding in encodings:
        # Comparer les visages connus avec les visages détectés
        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)

        # Si le visage détecté est connu, renvoyer une réponse 200
        if True in matches:
            return jsonify({"status": 200})

    # Si aucun visage reconnu n'est détecté, renvoyer une réponse 204
    return jsonify({"status": 204})


if __name__ == '__main__':
    app.run()
