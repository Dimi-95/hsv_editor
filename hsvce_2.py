import cv2 as cv
import numpy as np
from windowcapture import WindowCapture
import win32gui, win32ui, win32con


image = cv.imread("C:\\Users\\d3x\\Desktop\\OpenCv_test_ground\\champion_image\\taric.png")
image_2 = cv.imread("C:\\Users\\d3x\\Desktop\\OpenCv_test_ground\\champion_image\\taric.png")

window_name = "HSV Editor"
color_win_position = [(350,30), (700,90)]
hsv_track = {'h_min': 0, 's_min': 0, 'v_min': 0, 'h_max': 179, 's_max': 255, 'v_max': 255,
            's_add' : 0, 's_sub' : 0, 'v_add' : 0, "v_sub" : 0}


font = cv.FONT_HERSHEY_SIMPLEX


img = np.zeros((350,700,3), np.uint8)
cv.namedWindow(window_name)

#HSV MIN-MAX 
img = cv.putText(img, "h_min: ", (10, 30), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "s_min: ", (170, 30), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "v_min: ", (330, 30), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "h_max: ", (10, 60), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "s_max: ", (170, 60), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "v_max: ", (330, 60), font, 0.5, (255,255,255), 1)

#SV ADD/SUB
img = cv.putText(img, "s_add: ", (10, 90), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "v_add: ", (170, 90), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "s_sub: ", (330, 90), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "v_sub: ", (490, 90), font, 0.5, (255,255,255), 1)

#Values
#HSV MIN-MAX
img = cv.putText(img, "0", (80, 30), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "0", (240, 30), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "0", (400, 30), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "179", (80, 60), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "255", (240, 60), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "255", (400, 60), font, 0.5, (255,255,255), 1)
#SV ADD/SUB
img = cv.putText(img, "0", (80, 90), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "0", (240, 90), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "0", (400, 90), font, 0.5, (255,255,255), 1)
img = cv.putText(img, "0", (560, 90), font, 0.5, (255,255,255), 1)

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

#Update functions
#MIN Values
def update_H_min_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['h_min']}", (80, 30), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (80,30), font, 0.5, (255,255,255), 1)
    hsv_track['h_min'] = x

def update_S_min_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['s_min']}", (240, 30), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (240,30), font, 0.5, (255,255,255), 1)
    hsv_track['s_min'] = x

def update_V_min_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['v_min']}", (400, 30), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (400,30), font, 0.5, (255,255,255), 1)
    hsv_track['v_min'] = x
#MAX Values
def update_H_max_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['h_max']}", (80, 60), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (80,60), font, 0.5, (255,255,255), 1)
    hsv_track['h_max'] = x

def update_S_max_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['s_max']}", (240, 60), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (240,60), font, 0.5, (255,255,255), 1)
    hsv_track['s_max'] = x

def update_V_max_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['v_max']}", (400, 60), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (400,60), font, 0.5, (255,255,255), 1)
    hsv_track['v_max'] = x
#ADD and SUB
def update_S_add_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['s_add']}", (80, 90), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (80,90), font, 0.5, (255,255,255), 1)
    hsv_track['s_add'] = x

def update_V_add_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['v_add']}", (240, 90), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (240,90), font, 0.5, (255,255,255), 1)
    hsv_track['v_add'] = x

def update_S_sub_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['s_sub']}", (400, 90), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (400,90), font, 0.5, (255,255,255), 1)
    hsv_track['s_sub'] = x

def update_V_sub_value(x):
    global font, img, hsv_track
    img = cv.putText(img,f"{hsv_track['v_sub']}", (560, 90), font, 0.5, (0,0,0), 1)
    img = cv.putText(img,f"{x}", (560,90), font, 0.5, (255,255,255), 1)
    hsv_track['v_sub'] = x

#Setting up the trackers

cv.createTrackbar("h_min", window_name, 0, 179, update_H_min_value)
cv.createTrackbar("s_min", window_name, 0, 255, update_S_min_value)
cv.createTrackbar("v_min", window_name, 0, 255, update_V_min_value)

cv.createTrackbar("h_max", window_name, 0, 179, update_H_max_value)
cv.createTrackbar("s_max", window_name, 0, 255, update_S_max_value)
cv.createTrackbar("v_max", window_name, 0, 255, update_V_max_value)

cv.setTrackbarPos('h_max', window_name, 179)
cv.setTrackbarPos('s_max', window_name, 255)
cv.setTrackbarPos('v_max', window_name, 255)

cv.createTrackbar("s_add", window_name, 0, 255, update_S_add_value)
cv.createTrackbar("s_sub", window_name, 0, 255, update_S_sub_value)
cv.createTrackbar("v_add", window_name, 0, 255, update_V_add_value)
cv.createTrackbar("v_sub", window_name, 0, 255, update_V_sub_value)

while(1):
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
    if key==ord('z'):
        print("Image has been saved")
        f = open("HSV_Values.txt", "w")
        f.write(f"h_min = {h_min}, v_min = {v_min},s_min = {s_min}, h_max = {h_max}, v_max = {v_max}, s_max = {s_max}, s_add = {s_add}, s_sub = {s_sub}, v_add {v_add}, v_sub {v_sub}")
        f.close()
        cv.imwrite("test.png", image )




cv.destroyAllWindows()