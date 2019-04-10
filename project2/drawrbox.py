import cv2
import numpy as np

# 根据四点画原矩形


def drawRect(img, pt1, pt2, pt3, pt4, color, lineWidth):
    cv2.line(img, pt1, pt2, color, lineWidth)
    cv2.line(img, pt2, pt3, color, lineWidth)
    cv2.line(img, pt3, pt4, color, lineWidth)
    cv2.line(img, pt1, pt4, color, lineWidth)


def rRect_draw(img, rRect, color, lineWidth):
    # rRect = [xc, yc, W, H, angle] 注意为角度值

    rotatemat = cv2.getRotationMatrix2D((rRect[0], rRect[1]), rRect[4], 1)
    pt1 = tuple(np.dot(rotatemat, [rRect[0] - rRect[2] / 2, rRect[1] - rRect[3] / 2, 1]).astype(int))
    pt2 = tuple(np.dot(rotatemat, [rRect[0] - rRect[2] / 2, rRect[1] + rRect[3] / 2, 1]).astype(int))
    pt4 = tuple(np.dot(rotatemat, [rRect[0] + rRect[2] / 2, rRect[1] - rRect[3] / 2, 1]).astype(int))
    pt3 = tuple(np.dot(rotatemat, [rRect[0] + rRect[2] / 2, rRect[1] + rRect[3] / 2, 1]).astype(int))
    cv2.line(img, pt1, pt2, color, lineWidth)
    cv2.line(img, pt2, pt3, color, lineWidth)
    cv2.line(img, pt3, pt4, color, lineWidth)
    cv2.line(img, pt1, pt4, color, lineWidth)
    return img


width = 320
height = 240
angle = 30
image = np.zeros((height, width))

cv2.rectangle(image, (50, 70), (150, 130), (255, 255, 255))  # 12
rRect_draw(image, [100, 100, 100, 60, 30], (255, 255, 255), 2)
rRect_draw(image, [100, 100, 100, 60, 45], (255, 255, 255), 2)
rRect_draw(image, [100, 100, 100, 60, 60], (255, 255, 255), 2)
rRect_draw(image, [100, 100, 100, 60, 90], (255, 255, 255), 2)
cv2.imshow("Canvas", image)  # 13
cv2.waitKey(0)  # 14
