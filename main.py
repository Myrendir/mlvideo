import cv2
import numpy as np
import face_recognition
import requests
from PIL import Image
import io
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
last_image = 'http://45.147.99.71:3000/api/images/last'
image_dir = './images'

net = cv2.dnn.readNet("yolov3.cfg", "yolov3.weights")
classes = []

person_id = 'person'

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
    response = requests.get(last_image)
    img = Image.open(io.BytesIO(response.content))
    img = np.array(img)

    faces = face_recognition.face_locations(img)
    encodings = face_recognition.face_encodings(img, faces)

    recognized_person = None

    for idx, face_encoding in enumerate(encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)
        if True in matches:
            recognized_person = known_names[idx]
            break

    if recognized_person:
        return jsonify(
            {
                "status": 200,
                "target": recognized_person
            }
        )

    return jsonify({"status": 204})


@app.route('/add_photos', methods=['POST'])
def add_photos():
    if 'name' not in request.form:
        return jsonify({"status": 400, "message": "Missing 'name' parameter."})

    if 'photos' not in request.files:
        return jsonify({"status": 400, "message": "No photos uploaded."})

    name = request.form['name']
    photos = request.files.getlist('photos')

    # Create a directory for the new person
    new_dir_path = os.path.join(image_dir, name)
    os.makedirs(new_dir_path, exist_ok=True)

    # Save the uploaded photos
    for photo in photos:
        if photo.filename == '':
            continue

        # Check if the photo is in JPEG format
        if photo.filename.lower().endswith(('.jpg', '.jpeg')):
            photo_path = os.path.join(new_dir_path, photo.filename)
            photo.save(photo_path)

            # Add the new person to known_faces and known_names
            img = face_recognition.load_image_file(photo_path)
            encodings = face_recognition.face_encodings(img)[0]
            known_faces.append(encodings)
            known_names.append(name)

    return jsonify({"status": 200, "message": "Photos added successfully."})


@app.route('/delete_photos', methods=['POST'])
def delete_photos():
    if 'name' not in request.form:
        return jsonify({"status": 400, "message": "Missing 'name' parameter."})

    name = request.form['name']
    dir_path = os.path.join(image_dir, name)

    if not os.path.exists(dir_path):
        return jsonify({"status": 404, "message": "Folder not found."})

    # Delete the directory and its contents
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        os.rmdir(root)

    # Remove the person from known_faces and known_names
    idx = known_names.index(name)
    del known_faces[idx]
    del known_names[idx]

    return jsonify({"status": 200, "message": "Photos deleted successfully."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
