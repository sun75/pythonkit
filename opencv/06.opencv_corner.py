import cv2

image = cv2.imread("../img/opencv_logo2.png")
# 彩色图像转为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 获取图像中的特征点:图像中的点最多500个点，点的质量优于0.1，特质点之间的距离>10个像素
corners =cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)
# 将每个特征点标记出来
for corner in corners:
    x, y = corner.ravel()
# x y 为float，需要转成int,中心点坐标，半径，颜色，像素粗细
    cv2.circle(image, (int(x), int(y)), 3, (255, 0, 255), -1)

# 提取出来的点都是转角，转角是最明显的特征
cv2.imshow("corners", image)
cv2.waitKey()

