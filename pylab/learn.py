import numpy as np
import matplotlib.pyplot as pt
from skimage import io
x = np.arange(0 , 360)
y = np.sin( x * np.pi / 180.0)
pt.plot(x,y)
pt.xlim(0,360)
pt.ylim(-1.2,1.2)
pt.title("SIN function")
pt.show()

img=io.imread('123.jpg')
pt.subplot(2,2,1)
pt.subplot(2, 2, 1)  # 将窗口分为两行两列四个子图，则可显示四幅图片
pt.title('origin image')  # 第一幅图片标题
pt.imshow(img)  # 绘制第一幅图片

print(img.shape)
print(img[:, :, 0].shape)



pt.subplot(2, 2, 2)  # 第二个子图
pt.title('R channel')  # 第二幅图片标题
pt.imshow(img[:, :, 0], pt.cm.gray)  # 绘制第二幅图片,且为灰度图
pt.axis('off')  # 不显示坐标尺寸

pt.subplot(2, 2, 3)  # 第三个子图
pt.title('G channel')  # 第三幅图片标题
pt.imshow(img[:, :, 1], pt.cm.gray)  # 绘制第三幅图片,且为灰度图
pt.axis('off')  # 不显示坐标尺寸

pt.subplot(2, 2, 4)  # 第四个子图
pt.title('B channel')  # 第四幅图片标题
pt.imshow(img[:, :, 2], pt.cm.gray)  # 绘制第四幅图片,且为灰度图
pt.axis('off')  # 不显示坐标尺寸


pt.savefig('hah.png')
pt.show()