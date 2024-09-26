# crop image / trim image  裁剪
import cv2

image = cv2.imread("../img/opencv_logo2.png")

#(695, 1600, 3)   row  ,  column
# 先横行，再纵行 [300:470, 400:1200] 300～470行，400～1200列
crop = image[300:470, 400:1200]

cv2.imshow("crop", crop)
cv2.waitKey()