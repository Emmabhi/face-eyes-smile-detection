import cv2
facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyecascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smilecascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
s = int(input(" press number  ==== 1.face\t2.eye\t3.smile\n"))
while True:
    success,frame = cap.read()

    if s == 1:
        obj = facecascade.detectMultiScale(frame,1.1,4)
    elif s == 2:
        obj = eyecascade.detectMultiScale(frame,1.1,10)

    elif s == 3:
        obj = smilecascade.detectMultiScale(frame,2,50)

    else:
        print("Invalid")
        break
    for (x,y,w,h) in obj:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2)
    cv2.imshow('Camera',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
