# 图像的形态学算法
import cv2
import numpy as np

gray=cv2.imread("../img/opencv_logo2.png",cv2.IMREAD_GRAYSCALE)

# 1.基于二值化图像，使用反向阈值：变成了背景为黑，图像为白
# _ 表示它只是一个临时值
_, binary = cv2.threshold(gray,250,255,cv2.THRESH_BINARY_INV)

# 2.定义一个kernel为5*5的正方形。
# 腐蚀和膨胀对于清理边缘细节有作用
# Return a new array of given shape and type, filled with ones.
kernel=np.ones((5,5),np.uint8)

# 2.1腐蚀erosion内核: 会看到图标小了一圈
# 用kernel来腐蚀binary图像
erosion=cv2.erode(binary,kernel)

# 2.2膨胀 dilation：会看到图标大了一圈
dilation=cv2.dilate(binary,kernel)

cv2.imshow("binary",binary)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.waitKey()