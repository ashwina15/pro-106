import cv2


# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')
body_classifier=cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Loop once video is successfully loaded

    
    # Read first frame
ret, frame = cap.read()

    while(True):
      cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      bodies=body_classifier.detectMultiScale(gray,1.2,3)

      for(x,y,w,h)in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

      cv2.imshow()
    #Convert Each Frame into Grayscale
    
    # Pass frame to our body classifier
    
    
    # Extract bounding boxes for any bodies identified
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()

