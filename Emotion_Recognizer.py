import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import eel
import time

@eel.expose
def detect_emotion(timeSelect):
    # Initialize necessary variables
    cap = cv2.VideoCapture(0)  # or the appropriate source
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    classifier = load_model('model.h5')  # Load your trained model
    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    emotion_durations = {emotion: 0 for emotion in emotion_labels}

    # Variables to track time
    start_time = int(time.time())
    end_time = start_time + int(timeSelect) * 10  # Convert minutes to seconds

    # Variables to track emotion stability
    previous_label = None
    stability_start_time = None
    stability_duration = 1  # seconds

    while int(time.time()) < end_time:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Check if the emotion is stable
                if label == previous_label:
                    if stability_start_time is None:
                        stability_start_time = time.time()
                    elif time.time() - stability_start_time >= stability_duration:
                        emotion_durations[label] += stability_duration
                        stability_start_time = time.time()
                else:
                    previous_label = label
                    stability_start_time = time.time()
            else:
                cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    timeInv = sum(emotion_durations.values())

    # Normalize each duration to percentage
    for key in emotion_durations:
        emotion_durations[key] = int((emotion_durations[key] / timeInv) * 100)

    print(emotion_durations)
    return emotion_durations

    

# print(detect_emotion())
