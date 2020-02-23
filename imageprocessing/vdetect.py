import cv2 

video = cv2.VideoCapture("faceDetection.mp4")
# print(type(video))
# check , frame = video.read()
# print(type(frame))
# print(type(check))
# print(frame)
# cv2.imshow("1st frame",frame)
# cv2.waitKey(3000)
# cv2.destroyAllWindows
'''
check = True
while check :
    check,frame = video.read()
    cv2.imshow("frames",frame)
    key = cv2.waitKey(6)
    if(key==ord('q')):
        break


cv2.destroyAllWindows

video.release()

'''
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
check = True
while check :
    check,frame = video.read()
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.30,minNeighbors=12)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(50,321,65),3)

    cv2.imshow("frames",frame)
    key = cv2.waitKey(1)
    if(key==ord('q')):
        break


cv2.destroyAllWindows()

video.release()
print(frame_count)
