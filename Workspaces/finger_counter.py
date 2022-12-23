import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mpHand.Hands()

mpDraw = mp.solutions.drawing_utils
mpDrawStyle = mp.solutions.drawing_styles

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if not success:
        break

    fingerCount = 0

    rightCount = 0
    leftCount = 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            
            mpDraw.draw_landmarks(img, 
            handLms, 
            mpHand.HAND_CONNECTIONS,
            mpDrawStyle.get_default_hand_landmarks_style(),
            mpDrawStyle.get_default_hand_connections_style())
            
            handIndex = results.multi_hand_landmarks.index(handLms)
            handLabel = results.multi_handedness[handIndex].classification[0].label

            handLandmarks = []

            for landmarks in handLms.landmark:
                handLandmarks.append([landmarks.x, landmarks.y])

            if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                fingerCount = fingerCount+1
                if handLabel == "Left":
                    leftCount += 1

            elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                fingerCount = fingerCount+1
                if handLabel == "Right":
                    rightCount += 1
                if handLabel == "Left":
                    leftCount += 1

            if handLandmarks[8][1] < handLandmarks[6][1]:       #INDEX FINGER
                fingerCount = fingerCount+1
                if handLabel == "Right":
                    rightCount += 1
                if handLabel == "Left":
                    leftCount += 1

            if handLandmarks[12][1] < handLandmarks[10][1]:     #MIDDLE FINGER
                fingerCount = fingerCount+1
                if handLabel == "Right":
                    rightCount += 1
                if handLabel == "Left":
                    leftCount += 1

            if handLandmarks[16][1] < handLandmarks[14][1]:     #RING FINGER
                fingerCount = fingerCount+1
                if handLabel == "Right":
                    rightCount += 1
                if handLabel == "Left":
                    leftCount += 1

            if handLandmarks[20][1] < handLandmarks[18][1]:     #PINKY
                fingerCount = fingerCount+1
                if handLabel == "Right":
                    rightCount += 1
                if handLabel == "Left":
                    leftCount += 1
    #FPS
    cTime = time.time()
    fps = 1 / (cTime- pTime)
    pTime = cTime
    
    cv2.putText(img, "FPS: "+str(int(fps)), (10,75), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 3)
    cv2.putText(img, str(fingerCount), (250,450), cv2.FONT_HERSHEY_PLAIN, 8, (255,0,0), 7)

    cv2.putText(img, str(leftCount), (50,450), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 3) #LEFT
    cv2.putText(img, str(rightCount), (500,450), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 3) #RIGHT

    cv2.imshow("img", img)

    cv2.waitKey(1)

    if cv2.getWindowProperty("img", cv2.WND_PROP_VISIBLE) <1:
        break
    
    
cv2.destroyAllWindows()