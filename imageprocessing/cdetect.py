
import cv2

video = cv2.VideoCapture("video.avi")

car_cascade = cv2.CascadeClassifier("cars.xml")
check = True
while check==True :
    check,frame = video.read()
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=1)
    for x,y,w,h in cars:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(50,321,65),3)

    cv2.imshow("frames",frame)
    key = cv2.waitKey(60)
    if(key==ord('q')):
        break


cv2.destroyAllWindows()

video.release()
print(frame.shape)
'''
import cv2 
  
# capture frames from a video 
cap = cv2.VideoCapture('video.avi') 
  
# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('cars.xml') 
  
# loop runs if capturing has been initialized. 
while True: 
    # reads frames from a video 
    ret, frames = cap.read() 
      
    # convert to gray scale of each frames 
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
      
  
    # Detects cars of different sizes in the input image 
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
      
    # To draw a rectangle in each cars 
    for (x,y,w,h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2) 
  
   # Display frames in a window  
    cv2.imshow('video2', frames) 
      
    # Wait for Esc key to stop 
    if cv2.waitKey(33) == 27: 
        break
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
'''