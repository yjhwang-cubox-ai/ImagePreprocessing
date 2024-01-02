import numpy as np
import cv2
from time import sleep

# 메인 함수
image = cv2.imread('test/009.jpg') # 파일 읽어들이기
image = cv2.resize(image, dsize=(600,600), interpolation=cv2.INTER_LINEAR)
image2 = cv2.imread('test/dr_00000027.jpg') # 파일 읽어들이기
image2 = cv2.resize(image2, dsize=(600,600), interpolation=cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("image2", image2)

cv2.waitKey()

   