#import 
import cv2

#initializing
vehile = 0
validVehiles = []

#adding background subtractor 
BS_MOG2 = cv2.createBackgroundSubtractorMOG2()

#opening video file
cap = cv2.VideoCapture('night1.mp4')

while cap.isOpened():
    ret,frame = cap.read() #reads next frame
    fgMask = BS_MOG2.apply(frame) #foreground mask
    cv2.line(frame, (0,450), (1200,450), (0,0,255), 2) #red line
    contours,h = cv2.findContours(fgMask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #contour 
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)

        # ignore the small contours in size
        visibleVehile = (w > 50) and (h > 50)
        if not visibleVehile:
            continue
        if x > 200 and x < 800 and y > 100:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) #green rectangle surrounding object
            xMid = int((x + (x+w))/2)
            yMid = int((y + (y+h))/2)
            cv2.circle(frame, (xMid,yMid),5,(0,0,255),5) #red center dot

            # add all valid vehiles into List Array
            validVehiles.append((xMid,yMid))
            
            for (vX, vY) in validVehiles:
                if vY > 450 and vY < 456: #frame change
                    vehile += 1
                    validVehiles.remove((vX,vY))

    cv2.putText(frame, 'Vehicle count : {}'.format(vehile), (450, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2) #blue text
    cv2.imshow('Original Video', frame)
    
    # wait for any key to be pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release video capture
cv2.destroyAllWindows()
vidCap.release()
