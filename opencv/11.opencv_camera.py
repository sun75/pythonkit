# 使用opencv调用电脑中的摄像头
import cv2

# 获取摄像头的指针,参数里面需要传入摄像头的序号。如果只有一个摄像头，参数为0
capture=cv2.VideoCapture(0)

# 因为video是一帧一帧连续读取，所以暂时先设为死循环
# 如果输入任意键 != -1,就跳出循环
# 释放capture指针
while True:
    ret,frame=capture.read()
    cv2.imshow("camera",frame)
    key=cv2.waitKey(1)      #等待1毫秒
    if key!= -1:
        break

capture.release()