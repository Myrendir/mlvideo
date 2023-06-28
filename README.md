# Reconnaissance faciale avec Flask

Ce projet implémente un service de reconnaissance faciale à l'aide de Flask, OpenCV et la bibliothèque face_recognition. L'objectif est de détecter si un visage reconnu est présent dans l'image la plus récente obtenue depuis une API.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- Python 3.x installé sur votre machine
- Les packages Python requis : `cv2`, `numpy`, `face_recognition`, `requests` et `PIL`. Vous pouvez les installer en exécutant la commande suivante :

```pip install numpy```  
```pip install face_recognition```  
```pip install requests```  
```pip install pillow```  
```pip install flask```  
```pip install opencv-python===4.5.5.62```  
```pip install tensorflow```  

## Utilisation

1. Clonez ce dépôt ou téléchargez les fichiers du projet.

2. Assurez-vous que le répertoire `images` contient les images des visages connus. Chaque image doit être placée dans un dossier correspondant au nom de la personne représentée. Par exemple :

images/
personne1/
personne1.jpg
personne1_2.jpg
personne2/
personne2.jpg
personne2_2.jpg

3. Assurez-vous d'avoir les fichiers YOLO pré-entrainés (`yolov3.weights` et `yolov3.cfg`) dans le même répertoire que le script Python.
  -> Pour récupérer yolov3.weights : https://github.com/patrick013/Object-Detection---Yolov3/blob/master/model/yolov3.weights
4. Modifiez la variable `last_image` avec l'URL de l'API pour récupérer l'image la plus récente.

5. Exécutez le script Python en utilisant la commande suivante :

```python main.py```

Le serveur Flask démarrera et sera prêt à recevoir des requêtes.

6. Accédez à l'URL `http://localhost:8001` dans votre navigateur ou utilisez un outil comme cURL pour envoyer une requête GET à l'API. Vous recevrez une réponse JSON avec le statut 200 si un visage reconnu est détecté dans l'image la plus récente, ou le statut 204 si aucun visage reconnu n'est détecté.

## Personnalisation

- Vous pouvez ajuster le seuil de tolérance pour la comparaison des visages en modifiant la valeur de `tolerance` dans la boucle `for face_encoding in encodings`.

- Pour utiliser votre propre API pour récupérer l'image la plus récente, remplacez la valeur de `last_image` par l'URL correspondante.

- Vous pouvez personnaliser la logique de récupération des images et de la reconnaissance faciale selon vos besoins en modifiant le code approprié dans la fonction `detect_faces()`.

## Conclusion

Ce projet vous permet de créer un service de reconnaissance faciale simple en utilisant Flask, OpenCV et face_recognition. Vous pouvez l'étendre pour inclure d'autres fonctionnalités telles que la détection d'objets supplémentaires ou l'intégration à d'autres API pour obtenir des images. N'hésitez pas à expérimenter et à adapter le code en fonction de vos besoins.
