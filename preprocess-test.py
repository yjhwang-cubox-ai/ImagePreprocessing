import cv2

src = cv2.imread('test/00000.jpeg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 30)

cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()