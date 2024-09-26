import cv2

image = cv2.imread("../img/opencv_logo2.png")
cv2.imshow("blue", image[:,:,0])
cv2.imshow("green", image[:,:,1])
cv2.imshow("red", image[:,:,2])

# 1.提供彩色图像的灰度变化算法:将三个彩色通道的图像作平方和做加权平均
# 2.通常将gray成为灰度图，大量的图像算法，基于灰度图来操作
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #彩色图像转为灰度图
cv2.imshow("gray", gray)
cv2.waitKey()