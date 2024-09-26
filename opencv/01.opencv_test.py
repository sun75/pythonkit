# ------install packages commands
# pip3 install opencv_python
# pip3 install numpy
# pip3 install matplotlib

import cv2

print(cv2.getVersionString())

# 1.read image
# image=cv2.imread("img/plane.jpg")
image=cv2.imread("../img/opencv_logo2.png")

# 2.print shape 打印维度
# should go with jpg/png, not svg
# 1080* 1920* 3 像素的图片
print(image.shape)   #(1080, 1920, 3)

# 3.show image
cv2.imshow("image",image)

# 4.make image stop and show (runnning)
cv2.waitKey()

# 5.opencv store image with the order BGR (0~255), contrary to normal RGB
# opencv灰度图纬度是0～255存储顺序为BGR，与三原色RGB相反
