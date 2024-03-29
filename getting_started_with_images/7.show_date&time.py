import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,3000)
cap.set(4,2000)
print(cap.get(3))
print(cap.get(4))
while(True):                            # True / cap.isOpened()  both are same we can either one
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        datet=str(datetime.datetime.now())
        text = 'width: '+ str(cap.get(3))+' , '+'height: '+ str(cap.get(4))+' , '+'date: '+ datet
        cv2.putText(frame,text, (10,50),font,1,(0,0,255),2,cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()