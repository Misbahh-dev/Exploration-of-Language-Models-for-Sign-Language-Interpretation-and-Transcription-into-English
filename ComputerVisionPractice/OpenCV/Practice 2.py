import cv2
# Load two images
img1 = cv2.imread('C:/Users/MISBAH/Desktop/photo.jpg')
img2 = cv2.imread('C:/Users/MISBAH/Desktop/photo2.jpg')

# Resize images to same size
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.resize(img2, (400, 400))

# Blend images with transparency (alpha blending)
alpha = 0.5  # 0 = img1, 1 = img2
blended = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Blended Image', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()