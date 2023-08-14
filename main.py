import cv2
import numpy as np
from PIL import ImageGrab


def grab_screen(bbox=None):
    img = ImageGrab.grab(bbox=bbox)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


while True:
    img = grab_screen(bbox=(360, 85, 575, 210))

    cv2.imshow("Screen", img)
    cv2.waitKey(1)

# Currently, these codes can perform live screen tracking at the given location. The remaining codes will be added.
