import cv2
import numpy as np

mtx=[[3.38914855e+03 , 0.00000000e+00, 9.82985434e+02],
 [0.00000000e+00 , 3.78414471e+03 , 5.56363307e+02],
 [0.00000000e+00 , 0.00000000e+00, 1.00000000e+00]]
mtx = cv2.UMat(np.array(mtx))

dist= [[-1.83418584e+00 , 1.22930625e+01 , -4.34882103e-03 , 2.26389517e-02 ,
  -8.51805652e+01]]
dist = cv2.UMat(np.array(dist))

def undistort(img):
#   img = img[80:780,0:1920]
  h,  w = img.shape[:2]
  newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
  dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
  dst = cv2.UMat.get(dst)
  x,y,w1,h1 = roi
  dst = dst[y:y+h1, x:x+w1]
  return dst

cap = cv2.VideoCapture("negley/output_negley_1st.mp4")
frame_num = 0
while(True):
    ret, frame = cap.read()
    print(frame.shape)
    if ret:
        cv2.imwrite("negley/negley_1_undistort/{}.png".format(frame_num),frame[200:500,:])
        frame_num += 1
    else:
        break
cap.release()
cv2.destroyAllWindows()

