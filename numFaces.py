import cv2
from firebase import firebase
#connecting to the firebase server using its id
firebase = firebase.FirebaseApplication('https://parkpak-c41e3.firebaseio.com/')
# https://github.com/Itseez/opencv/blob/master
# /data/haarcascades/haarcascade_frontalface_default.xml
# XML file trained with data from faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture frames from a camera 
liveFeed = cv2.VideoCapture(0)

# loop runs if capturing has been initialized.
facePresent = 0
while 1:
    ret, img = liveFeed.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        facePresent += 1
    # Display an image in a window
    cv2.imshow('img', img)
    result = firebase.put(
        '',
        '/camera',
        {
            "faceCount":str(facePresent)
        }
    )
    print(result)
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    facePresent = 0

# Close the window 
liveFeed.release()

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
