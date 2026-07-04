import dlib
import numpy as np 
import face_recognition_models
from sklearn.svm import SVC 
import streamlit as st 

from src.database.db import get_all_students

# --------------------------------------------------------------------------------------------------
# Load and cache all required Dlib models.
#
# Models:
# - Face Detector      : Detects face locations (bounding boxes - track only round boundry of face).
# - Shape Predictor    : Predicts facial landmarks for each detected face.
#                        total 68 landmarks detect such as eye, nose, mouth texture etc
# - Face Recognition   : Generates a 128-dimensional face embedding.
#                        Base on Shape Predictor convet image face to the 128dim vector
#
# @st.cache_resource ensures these models are loaded only once, avoiding
# repeated initialization on every Streamlit rerun.
#
# 128dim embedding means => [e1, e2, e3, ..., e128]
# --------------------------------------------------------------------------------------------------

@st.cache_resource
def load_dlib_models():

    # Face Detector - Detects face bounding boxes. 
    detector = dlib.get_frontal_face_detector()

    # Facial Landmark detector model 
    sp = dlib.shape_predictor(

        # Note : Loads the pre-trained facial landmark model used by the shape predictor for better performance.
        face_recognition_models.pose_predictor_model_location()
    )

    # Generates 128-dimensional face embeddings.
    facerec = dlib.face_recognition_model_v1(
        # Loads the pre-trained facial landmark model used by the shape predictor for better performance.
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


# Detect all faces in an image and generate embeddings for each face. 
def get_face_embeddings(image_np):

    # load all face recognition models 
    detector, sp, facerec = load_dlib_models()

    # Step 1 : Detect all face bounding boxes
    # Detector return all detected face location in given image as form of list 
    # here inside detector(, 1) 1 means zoom image by x2 for more better faces analysis 
    # detector(, 0) means use as it is given image witout zooming 
    faces = detector(image_np, 1)

    encodings = []

    for face in faces:

        # Stpe 2 : Detect individual Face 68landmarks with the help of individaul face positions detected by detector 
        shape = sp(image_np, face)
        
        # Step 3: Generate a unique 128-dimensional embedding from the detected face.
        # compute_face_descriptor(, , 1) here 1 means use given 68landmark image not apply any oter additional rotational version of image for better embeddings
        # if we use 2, 3, .. etc so it means it internally rotates images and then as detect all images embeddings and finally predict average embeddings as final
        face_descriptor = facerec.compute_face_descriptor(
            image_np, 
            shape,
            1
        )

        encodings.append(np.array(face_descriptor))

    return encodings
    
@st.cache_resource
def get_trained_model():

    X = []
    y = []

    # get all students from database
    student_db = get_all_students()

    if not student_db:
        return None
    
    for student in student_db:
        embedding = student.get('face_embedding')

        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))
        
    # Students exist, but none have registered face embeddings. 
    if len(X) == 0:
        return None 
        
    # Initialise the Machine Learning Model 
    clf = SVC(
        kernel = "linear",
        probability = True, # Enables probability estimation using predict_proba(). 
        class_weight = 'balanced' # balance all class for stable training 
    )

    try:
        # Train the model 
        clf.fit(X, y)

    # if onle one student we fetch from database so that case SVC can't train because its classification model 
    # that case it returns ValueError and this case handeling done in futher functions in this file 
    except ValueError:
        pass 

    return {'clf': clf, 'X': X, 'y': y}


# Retrain the classifier after registering a new student. 
def train_classifier():
    get_trained_model.clear() # only remove ML model inside the cache 
    model_data = get_trained_model()
    return bool(model_data)


# Main attendance prediction pipeline
def predict_attendance(class_image_np):

    # get all face embeddings inside the teacher uploaded class_image_np
    encodings = get_face_embeddings(class_image_np)

    detected_students = {}
    
    # Load the trained classifier.
    model_data = get_trained_model()
    
    # if no student exist inside database or student have no face information
    if not model_data:
        return detected_students, [], len(encodings)
    
    # Extract the trained model and training data
    clf = model_data['clf']
    X_train = model_data['X']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:

        # if we have 2 or more student then we can predict by ML model 
        if len(all_students) >= 2:
            predicted_id = int(clf.predict([encoding])[0])
        else:
            # Handle single-student case without calling the unfitted SVC model. 
            predicted_id = int(all_students[0])

        # Retrieve the stored embedding of the predicted student.
        student_embedding = X_train[y_train.index(predicted_id)]

        # find best_match_score = student_embedding (real embedding of student) - encoding (fetech embedding of student in teacher group image)
        best_match_score = np.linalg.norm(student_embedding - encoding)

        # Accept the prediction only if the similarity score is below the threshold.
        resemblance_threshold = 0.6
        if best_match_score <= resemblance_threshold:
            detected_students[predicted_id] = True

    return detected_students, all_students, len(encodings)