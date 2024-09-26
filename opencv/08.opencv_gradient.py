# 图像梯度：就是明暗变化。梯度算法接收灰度图
import cv2

gray=cv2.imread("../img/opencv_logo2.png", cv2.IMREAD_GRAYSCALE)  # 直接读取灰度图

# 1.拉普拉斯算子 Laplace Operator：大致对应图像的二阶导数
# 拉普拉斯算子能给出图像明暗变化的趋势：背景区域变黑色，有明暗变化的区域变成白色(几何图形的边缘有剧烈的明暗变化)
# 所以梯度算法常常用来检测边缘
laplacian=cv2.Laplacian(gray, cv2.CV_64F)

# 2.Canny算法: 使用梯度区间来定义边缘
# 如果某个梯度区间>200 ，就可以确定是一个边缘，因为周围的明暗变化过于强烈
# 如果梯度<100，就可以确定不是边缘，因为周围没有明暗变化
# 如果梯度在100～200，就要看像素是否和已知的边缘像素相连。
# ---如果和某个已知的边缘像素连在一起，那么判断它是边缘；否则不是
canny = cv2.Canny(gray,100,200)

# 显示一下原图和计算结果
cv2.imshow("gray",gray)
cv2.imshow("laplacian",laplacian)# 拉普拉斯算子能给出图像明暗变化的趋势：
cv2.imshow("canny",canny)        # canny能检测出清晰完美的边缘
cv2.waitKey()
