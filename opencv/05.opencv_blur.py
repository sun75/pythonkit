# 均值滤波 blur
import cv2
from matplotlib.pyplot import imshow

image=cv2.imread("../img/blurcat.jpg")

# 1.高斯滤波器
# 高斯内核为5个像素，sigmaX设为0， 表示sigma又内核大小决定
gauss=cv2.GaussianBlur(image,(5,5),0)

# 2.中值滤波器
# 像素为5个像素
median = cv2.medianBlur(image,5)

# 3.将滤波后的图像显示出来
# 噪点：模糊的白色点点
cv2.imshow("image",image)
cv2.imshow("gauss",gauss)    #噪点减少，但是会破坏图像细节
cv2.imshow("median",median)  #噪点变得更少
# 但是实际情况很少遇到，只会遇到干净背景的少数几个噪点，使用均值滤波进行消除，方便后面的图像处理

cv2.waitKey()