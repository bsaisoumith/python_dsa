# Importing necessary libraries
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras_vggface.vggface import VGGFace
from keras_vggface import utils

# Set the path to your dataset folder
dataset_path = 'path_to_your_dataset_folder'

# Function to load dataset
def load_dataset(dataset_path):
    images = []
    labels = []
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith(".jpg"):
                img_path = os.path.join(root, file)
                label = os.path.basename(root)
                images.append(cv2.imread(img_path))
                labels.append(label)
    return images, labels

# Function to detect faces in images
def detect_faces(images):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    detected_faces = []
    for img in images:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            detected_faces.append(img[y:y+h, x:x+w])
    return detected_faces

# Function to label detected faces
def label_faces(faces, labels):
    labeled_faces = []
    for face, label in zip(faces, labels):
        labeled_faces.append((face, label))
    return labeled_faces

# Function to preprocess images for VGG-Face model
def preprocess_images(images):
    processed_images = []
    for img in images:
        img = cv2.resize(img, (224, 224))
        processed_images.append(img)
    return np.array(processed_images)

# Function to train VGG-Face model
def train_model(images, labels):
    # Load VGG-Face model
    model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
    # Preprocess images
    processed_images = preprocess_images(images)
    # Extract features using VGG-Face model
    features = model.predict(utils.preprocess_input(processed_images.copy().astype(float)))
    return features, labels

# Function to evaluate model accuracy
def evaluate_model(features, labels, test_images, test_labels):
    # Split dataset into training and testing sets
    train_features, test_features, train_labels, _ = train_test_split(features, labels, test_size=0.2, random_state=42)
    # Train a simple classifier (e.g., KNN) using extracted features
    # Here, we are using KNN as an example. You can replace this with any classifier of your choice.
    from sklearn.neighbors import KNeighborsClassifier
    knn_classifier = KNeighborsClassifier(n_neighbors=5)
    knn_classifier.fit(train_features, train_labels)
    # Predict labels for test features
    predicted_labels = knn_classifier.predict(test_features)
    # Calculate accuracy
    accuracy = accuracy_score(test_labels, predicted_labels)
    return accuracy

# Main function
def main():
    # Load dataset
    images, labels = load_dataset(dataset_path)
    
    # Detect faces in images
    detected_faces = detect_faces(images)
    
    # Label detected faces
    labeled_faces = label_faces(detected_faces, labels)
    
    # Train VGG-Face model
    features, labels = train_model(detected_faces, labels)
    
    # Evaluate model accuracy
    accuracy = evaluate_model(features, labels, detected_faces, labels)
    print("Model accuracy:", accuracy)

if _name_ == "_main_":
    main()