import cv2
import numpy as np


img = cv2.imread('bird.jpg', cv2.IMREAD_UNCHANGED)

ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                100, 100, cv2.THRESH_BINARY)


contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



for c in contours:


    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

   
print(len(contours))



cv2.imshow("contours", img)



while True:
    key = cv2.waitKey(1)
    if key == 27: 
        break

cv2.destroyAllWindows()