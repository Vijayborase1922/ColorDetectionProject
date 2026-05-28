# pip install opencv-python numpy

import cv2
import numpy as np

# Reading image
img = cv2.imread("sample.jpg")

# Resize image
img = cv2.resize(img, (800, 600))

clicked = False
r = g = b = xpos = ypos = 0


# Mouse click function
def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y

        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# Set mouse callback
cv2.namedWindow("Color Detection Project")
cv2.setMouseCallback("Color Detection Project", draw_function)

while True:
    temp = img.copy()

    if clicked:
        cv2.rectangle(temp, (20, 20), (750, 80), (b, g, r), -1)

        text = f"R={r} G={g} B={b}"

        cv2.putText(temp, text, (50, 60), 2, 0.8, (255, 255, 255), 2)

    cv2.imshow("Color Detection Project", temp)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()