# 阈值算法：二值算法。将图像分为黑与白
import cv2

gray=cv2.imread("../img/night.jpeg",cv2.IMREAD_GRAYSCALE)
# 1.阈值为10，最大灰度255
ret,binary=cv2.threshold(gray,10,255,cv2.THRESH_BINARY)

# 2.自适应阈值算法，每个区独立计算阈值
# 因为图片明暗不均，很难确定固定阈值
# 所以将图片分成好多个区。光照弱的地方阈值小，光照强的地方阈值大
binary_adaptive=cv2.adaptiveThreshold(
    gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1) # 区域大小115个像素

#3.大津算法OTSU：自动计算阈值，使得计算出的 灰度差异 最大化，不需要人为确定阈值。本质是聚类分析算法
ret1,binary_otsu=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print(ret)     # 10
cv2.imshow("gray",gray)
cv2.imshow("binary",binary)
cv2.imshow("binary_adaptive",binary_adaptive)
cv2.imshow("binary_otsu",binary_otsu)
cv2.waitKey()
