import cv2
import mediapipe as mp
cap=cv2.VideoCapture("PoseVideos/5.mp4")
import time
mpPose=mp.solutions.pose
# Creating an Object
pose=mpPose.Pose()
previousTime=0
while True:
    success,img=cap.read()
    if not success:
        break   
    # img = cv2.resize(img, (640, 480))
    currentTime=time.time()
    fps=1/(currentTime-previousTime)
    previousTime=currentTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
