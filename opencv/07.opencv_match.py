# 匹配poker上的图案
import cv2
import numpy as np

image = cv2.imread("../img/poker.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)     # 转为灰度图
template = gray[810:850,240:280]    # 横行和纵列刚好包含一个菱形

# 1.存入待检测图像gray，模版template，使用标准相关匹配算法
# 标准相关匹配算法：将待检测图像和模版各自标准化，再来计算匹配度，这样可以保证匹配结果不受光照强度的影响
match = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)

# 2.找出匹配系数>0.9的匹配点：np.where(match>=0.9)，返回满足条件的坐标
# np.where(match>=0.9，1，0)，满足条件返回1，不满足条件返回0
locations= np.where(match>=0.9)

# 3.求出模版图案的长宽
# img.shape[ : 2] 表示取彩色图片的长、宽。
# img.shape[ : 3] 则表示取彩色图片的长、宽、通道。
# 在矩阵中，[0]就表示行数，[1]则表示列数。
# 使用切片的具体范围，从索引0到索引2（不包括2），返回一个包含高度和宽度的元组。
# 例如，如果 image.shape 是 (height, width, channels)，则 image.shape[0:2] 返回 (height, width)
w,h=image.shape[0:2]

# 4.作图
# 循环遍历每个匹配点
# list[::-1]返回倒序原序列 startIndex,endIndex,step
# startIndex:最小为0可以为空；endIndex 最大为长度，可以为空；step：默认为1步长，-1位倒序
# *：接收任意数量的参数，并返回元组(元组不可变)
for p in zip(*locations[::-1]):
    x1, y1 = p[0], p[1]
    x2, y2 = x1+w,y1+h
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)

print(gray.shape)
# cv2.imshow("template",template)

cv2.imshow("image",image)
cv2.waitKey()