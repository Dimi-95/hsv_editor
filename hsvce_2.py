from tkinter import filedialog
import cv2 as cv
import numpy as np
from tkinter import *
import os
import sys

window_name = "HSV Editor"
hsv_track = {'h_min': 0, 's_min': 0, 'v_min': 0, 'h_max': 179, 's_max': 255, 'v_max': 255,
            's_add' : 0, 's_sub' : 0, 'v_add' : 0, "v_sub" : 0}


font = cv.FONT_HERSHEY_SIMPLEX
current_action = None


img = np.zeros((200,700), np.uint8)
cv.namedWindow(window_name)

img = cv.putText(img, "Press 's' to take a picture and print the values into a text file ", (10, 30), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "Press 'q' to quit ", (10, 60), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "Press 'r' to choose a new image to edit. Don't forget to save. ", (10, 90), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "Output: ", (10, 120), font, 0.5, (255,255,255), 1)
img = cv.putText(img, " ", (90, 120), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "Note: Image(PNG) and text file gets saved to the same folder of the original image ", (10, 150), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "Made by d3x", (550, 180), font, 0.4, (255,255,255), 1)

def update_H_min_value(x):
    global font, img, current_action
    img = cv.putText(img,f"{current_action}", (90, 120), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (90, 120), font, 0.5, (255,255,255), 1)


def nothing(x):
    pass

#Function to apply adjustments to an HSV channel
def shift_channel(c, amount):
    if amount > 0:
        lim = 255 - amount
        c[c >= lim] = 255
        c[c < lim] += amount
    elif amount < 0:
        amount = -amount
        lim = amount
        c[c >= lim] = 0
        c[c > lim] -= amount
    return c


#Setting up the trackers

cv.createTrackbar("h_min", window_name, 0, 179, nothing)
cv.createTrackbar("s_min", window_name, 0, 255, nothing)
cv.createTrackbar("v_min", window_name, 0, 255, nothing)

cv.createTrackbar("h_max", window_name, 0, 179, nothing)
cv.createTrackbar("s_max", window_name, 0, 255, nothing)
cv.createTrackbar("v_max", window_name, 0, 255, nothing)

cv.setTrackbarPos('h_max', window_name, 179)
cv.setTrackbarPos('s_max', window_name, 255)
cv.setTrackbarPos('v_max', window_name, 255)

cv.createTrackbar("s_add", window_name, 0, 255, nothing)
cv.createTrackbar("s_sub", window_name, 0, 255, nothing)
cv.createTrackbar("v_add", window_name, 0, 255, nothing)
cv.createTrackbar("v_sub", window_name, 0, 255, nothing)

path = filedialog.askopenfilename(title="Choose your image to edit !")

while(1):
    

    image = cv.imread(path)

    image_2 = cv.imread(path)

    cv.imshow(window_name, img)
    key = cv.waitKey(1) & 0xff
    if key==ord('q'):
        break

    h_min = cv.getTrackbarPos("h_min", window_name)
    s_min = cv.getTrackbarPos("s_min", window_name)
    v_min = cv.getTrackbarPos("v_min", window_name)

    h_max = cv.getTrackbarPos("h_max", window_name)
    s_max = cv.getTrackbarPos("s_max", window_name)
    v_max = cv.getTrackbarPos("v_max", window_name)

    s_add = cv.getTrackbarPos("s_add", window_name)
    s_sub = cv.getTrackbarPos("s_sub", window_name)
    v_add = cv.getTrackbarPos("v_add", window_name)
    v_sub = cv.getTrackbarPos("v_sub", window_name)

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    oiriginal_hsv_image = cv.cvtColor(image_2, cv.COLOR_BGR2HSV)

    #Original Image
    og_h, og_s, og_v = cv.split(oiriginal_hsv_image)
    og_s = shift_channel(og_s, s_add)
    og_s = shift_channel(og_s, -s_sub)
    og_v = shift_channel(og_v, v_add)
    og_v = shift_channel(og_v, -v_sub)
    oiriginal_hsv_image = cv.merge([og_h, og_s, og_v])


    #Normal Image
    h, s, v = cv.split(hsv)
    s = shift_channel(s, s_add)
    s = shift_channel(s, -s_sub)
    v = shift_channel(v, v_add)
    v = shift_channel(v, -v_sub)
    hsv = cv. merge([h, s, v])


    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    #Use original values to be able to use the Trackbar to revert the changes
    hsv = oiriginal_hsv_image

    mask = cv.inRange(hsv, lower, upper)
    result = cv.bitwise_and(hsv, hsv, mask=mask)

    image = cv.cvtColor(result, cv.COLOR_HSV2BGR)
    cv.imshow("Editor_View", image)
    if key==ord('s'):
        name_of_path = path
        head_tail = os.path.split(name_of_path)
        f = open(f"{head_tail[1]}_HSV_values.txt", "w")
        f.write(f"h_min = {h_min}, v_min = {v_min},s_min = {s_min}, h_max = {h_max}, v_max = {v_max}, s_max = {s_max}, s_add = {s_add}, s_sub = {s_sub}, v_add {v_add}, v_sub {v_sub}")
        f.close()
        cv.imwrite(f"{head_tail[1]}_HSV.png", image )
        current_action = "Picture has been saved and text file created !"
        update_H_min_value(current_action)
    if key==ord('r'):
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)





cv.destroyAllWindows()