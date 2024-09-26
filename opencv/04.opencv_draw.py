import cv2
import numpy as np

cv2.imread("../img/opencv_logo2.png")

# 1.创建画布，维度 300*300*3, 灰度数值类型是无符号8位整数
# 是否加 dtype= 都可以
image = np.zeros((300, 300, 3), np.uint8)
# image = np.zeros((300, 300, 3), dtype=np.uint8)

# 2.画线
# 参数：起点 终点 颜色(蓝色B) 像素
cv2.line(image, (100, 200), (250, 250), (255, 0, 0), 2)

# 3.画rectangle
# 参数：顶点坐标 对角坐标 颜色(绿色G) 像素
cv2.rectangle(image, (30, 100), (60, 150), (0,255, 0), 2)

# 4.画circle
# 参数：圆心坐标 半径 颜色(红色R) 像素
cv2.circle(image, (150, 100), 20, (0,0,255), 3)

# 5.100,50 坐标，字体缩放序号 0 默认字体， 缩放序数 1， 颜色 255，255，255 白色, 粗细2个像素，线条类型1 为实线
cv2.putText(image,"hello",(100,50),0,2,(255,255,255),2,1)
cv2.imshow("image", image)
cv2.waitKey()