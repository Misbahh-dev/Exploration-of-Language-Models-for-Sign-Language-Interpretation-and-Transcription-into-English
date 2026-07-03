import cv2

img = cv2.imread('C:/Users/MISBAH/Desktop/photo.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (15, 15), 0)
resized = cv2.resize(img, (400, 400))

cv2.imshow('Original', img)
cv2.imshow('Gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()