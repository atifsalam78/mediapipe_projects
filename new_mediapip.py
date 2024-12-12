import cv2 as cv
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

def mediapipe_detection(image, model):
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB) # Color conversion from BGR to RGB
    image.flags.writeable = False                  # Image is no longe writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR) # Color converson from RGB to BGR
    return image, results



# For webcam input:
cap = cv.VideoCapture(0)
cap.set(3, 1280)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
   
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())

    
            
    # Flip the image horizontally for a selfie-view display.
    cv.imshow('MediaPipe Hands', cv.flip(image, 1))
    
    
    
    
    if cv.waitKey(1) & 0xFF == 27:
      break
cap.release()