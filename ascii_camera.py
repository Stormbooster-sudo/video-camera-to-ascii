import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os
import sys

# --------- for camera input --------- 
cap = cv2.VideoCapture(0)

# --------- for video file input --------- 
# cap = cv2.VideoCapture("file-name.mp4")

def display(value):
    pass
cv2.namedWindow("Original")
cv2.createTrackbar("Font Scale","Original",22,50,display)
cv2.createTrackbar("x","Original",0,1500,display)
cv2.createTrackbar("y","Original",0,1000,display)
cv2.createTrackbar("w","Original",70,120,display)
cv2.createTrackbar("h","Original",30,120,display)
path = os.path.join(sys.path[0], "COURIER.ttf")

while True:
    os.system('cls')
    ret,frame = cap.read()
    canvas = np.zeros([800,960,3], dtype=np.uint8)
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2GRAY)
    w = cv2.getTrackbarPos("w","Original")
    h = cv2.getTrackbarPos("h","Original")
    x = cv2.getTrackbarPos("x","Original")
    y = cv2.getTrackbarPos("y","Original")

    re_frame = cv2.resize(frame, (w,h))
    frame = cv2.resize(frame, (550,400))

    #create canvas for showing the result on a window
    pil_im = Image.fromarray(canvas)
    draw = ImageDraw.Draw(pil_im)
    font_scale = cv2.getTrackbarPos("Font Scale","Original")
    font = ImageFont.truetype(path, font_scale)

    #mask the value in re_frame array from gray format (0-255) to 0-9, which match with string shade (offset -> 25.5)
    val = 0
    str_shade = " .;-=+*#%@"
    for i in range(len(str_shade)):
        re_frame[(re_frame > val) & (re_frame <= (val + 25.5))] = 9 - i
        val += 25.5
    
    #substitute the value with charactor in re_frame array to making plain texts frame
    str_frame = np.chararray((h, w))
    text = ""
    for row in range(h):
        for col in range(w):
            str_frame[row][col] = str(str_shade[re_frame[row][col]])
        text += str(str_frame[row].tostring()).replace("b","") + "\n"

    #===== ASCII output =====
    #------ display on terminal ------
    print(re_frame)

    #------ display in new window ------
    # draw.text((-x, -y), text, font=font)
    # canvas = np.array(pil_im)
    # cv2.imshow("Ascii", canvas)

    cv2.imshow("Original", frame)

    #closing by pressing 'q' or window's close button
    if (cv2.waitKey(2) & 0xFF == ord('q')):
        break
    while cv2.getWindowProperty('window-name', 0) >= 0:
        keyCode = cv2.waitKey(50)
cap.release()
cv2.destroyAllWindows()
