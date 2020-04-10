""" Experiment with face detection and image filtering using OpenCV """

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('filename') # Leaving this here just for fun! Input a video if you'd like!

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
kernel = np.ones((21, 21), 'uint8')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
    if type(faces) is tuple:
        cv2.imshow('frame',frame)
    for (x, y, w, h) in faces:
        # To blur the face
        #frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)

        # My funny face drawing
        cv2.ellipse(frame, (int(x+w/2), int(y+h/2)), (int(w/2-13),int(h/2+20)), 0, 0, 360, (186,208,161), 5)
        size = cv2.getTextSize("You're an egg!", cv2.FONT_HERSHEY_SIMPLEX, w/150, 3)[0][0]
        text = cv2.putText(frame, "You're an egg!", (int(x+w/2-size/2),int(y+h+65)), cv2.FONT_HERSHEY_SIMPLEX, w/150, (186,208,161), 3)

        # Display the resulting frame
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
