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

Accédez à l'URL http://localhost:8001 dans votre navigateur ou utilisez un outil comme cURL pour envoyer des requêtes à l'API. Voici les différentes routes disponibles :

1. GET / : Cette route effectue la détection des visages dans l'image la plus récente et renvoie une réponse JSON.
   - Statut de la réponse : 200 si un visage reconnu est détecté dans l'image la plus récente, 204 si aucun visage reconnu n'est détecté.
   - Réponse JSON :
     - Pour le statut 200 (visage reconnu) :
       ```
       {
         "status": 200,
         "target": "Nom de la personne reconnue"
       }
       ```
     - Pour le statut 204 (aucun visage reconnu) :
       ```
       {
         "status": 204
       }
       ```

2. POST /add_photos : Cette route permet d'ajouter des photos pour l'entraînement du modèle de reconnaissance faciale.
   - Paramètres :
     - name : Le nom de la personne associée aux photos.
     - photos : Les fichiers de photos à télécharger.
   - Réponse JSON :
     - Pour le statut 200 (succès) :
       ```
       {
         "status": 200,
         "message": "Photos ajoutées avec succès."
       }
       ```
     - Pour le statut 400 (mauvaise requête) :
       ```
       {
         "status": 400,
         "message": "Paramètre 'name' manquant."
       }
       ```
       ou
       ```
       {
         "status": 400,
         "message": "Aucune photo téléchargée."
       }
       ```

3. POST /delete_photos : Cette route permet de supprimer les photos associées à une personne.
   - Paramètre :
     - name : Le nom de la personne dont les photos doivent être supprimées.
   - Réponse JSON :
     - Pour le statut 200 (succès) :
       ```
       {
         "status": 200,
         "message": "Photos supprimées avec succès."
       }
       ```
     - Pour le statut 400 (mauvaise requête) :
       ```
       {
         "status": 400,
         "message": "Paramètre 'name' manquant."
       }
       ```
     - Pour le statut 404 (non trouvé) :
       ```
       {
         "status": 404,
         "message": "Dossier non trouvé."
       }
       ```

## Personnalisation

- Vous pouvez ajuster le seuil de tolérance pour la comparaison des visages en modifiant la valeur de `tolerance` dans la boucle `for face_encoding in encodings`.

- Pour utiliser votre propre API pour récupérer l'image la plus récente, remplacez la valeur de `last_image` par l'URL correspondante.

- Vous pouvez personnaliser la logique de récupération des images et de la reconnaissance faciale selon vos besoins en modifiant le code approprié dans la fonction `detect_faces()`.

## Conclusion

Ce projet vous permet de créer un service de reconnaissance faciale simple en utilisant Flask, OpenCV et face_recognition. Vous pouvez l'étendre pour inclure d'autres fonctionnalités telles que la détection d'objets supplémentaires ou l'intégration à d'autres API pour obtenir des images. N'hésitez pas à expérimenter et à adapter le code en fonction de vos besoins.
