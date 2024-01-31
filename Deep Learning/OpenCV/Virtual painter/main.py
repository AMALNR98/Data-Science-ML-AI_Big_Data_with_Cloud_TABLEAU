import cv2

import HandTrackingModule as htm

detector = htm.handDetector()
cap = cv2.VideoCapture(0)

# while True:
#     x,frame = cap.read()
#     cv2.imshow('Virtual painter', frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#     cap.release


while True:
    x,img = cap.read()
    img = cv2.resize(img,(1280,720))
    # Draw rectangles
    img = cv2.rectangle(img,(10,100),(200,10),(255,0,0),-1)
    img = cv2.rectangle(img,(210,100),(400,10),(0,255,0),-1)
    img = cv2.rectangle(img,(420,100),(600,10),(0,0,255),-1)   
    img = cv2.rectangle(img,(620,100),(800,10),(0,255,255),-1)
    img = cv2.rectangle(img,(820,100),(1000,10),(255,255,255),-1)


    cv2.imshow('Virtual painter', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    cap.release