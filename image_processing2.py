#image enhancement technique
import cv2 

img = cv2.imread('crime.png')

#preparation for CLAHE
clahe = cv2.createCLAHE()

#CONVERT TO GRAY SCALE IMAGE
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#APPLY ENHANCEMENT
enh_img = clahe.apply(gray_img)

cv2.imwrite('enhanced.png',enh_img)

print('done enhancing')