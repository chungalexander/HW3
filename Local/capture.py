# Import libraries

import numpy as np
import cv2
import paho.mqtt.client as mqtt

# Set up the mqtt client 

client = mqtt.Client()
client.connect("ip address of docker network hw03", 1883, 60)

# Define video input and haarcascade 

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1) # Video capture from cam 

while True:
    ret, img = cap.read()  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find the faces    
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    # For every face, add rectangle and convert image  
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face = frame[y:y+h, x:x+w] # Crop
        tmp,face = cv2.imencode('.png', face) # Convert to png
        face = face.tobytes() # Convert to bytes
        client.publish(topic, payload=face, qos=0, retain=False) # Publish

cap.release()
cv2.destroyAllWindows()