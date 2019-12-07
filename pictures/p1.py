#微信集赞

import cv2
import numpy as np

groundtruth = cv2.imread('1.jpg')[:, :, 0]
h1, w1 = groundtruth.shape
contours, cnt = cv2.findContours(groundtruth.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if len(contours) != 1:#轮廓总数
    pass
M = cv2.moments(contours[0])  # 计算第一条轮廓的各阶矩,字典形式
center_x = int(M["m10"] / M["m00"])
center_y = int(M["m01"] / M["m00"])
image = np.zeros([h1, w1], dtype=groundtruth.dtype)
cv2.drawContours(image, contours, 0, 255, -1)#绘制轮廓，填充
cv2.circle(image, (center_x, center_y), 7, 128, -1)#绘制中心点
cv2.imwrite("3.png", image)
