import cv2
import os
import numpy as np

imagedir = 'D:\\GW4'
annotation = os.path.join(imagedir, 'annotation')
list_images = [319, 325, 329,  344, 335, 358]
outputdir = 'output'
if not os.path.exists(outputdir):
    os.mkdir(outputdir)
radius = 7
gauss = 7


def draw_images():
    for imagename in list_images:
        img = cv2.imread(os.path.join(imagedir,str(imagename)+'.jpg')) # 720 1280 3
        with open(os.path.join(annotation,str(imagename)+'.txt' )) as label_file:
            lines = label_file.readlines()
            label_zero = []
            label_one = []
            for line in lines:
                line = line.rstrip().split(' ')
                if line[-4] == '0':
                    label_zero.append((int(line[1]), int(line[2])))
                elif line[-4] == '1':
                    label_one.append((int(line[1]), int(line[2])))

        label_one = np.array(label_one)
        label_zero = np.array(label_zero)
        # img_temp  = np.zeros(img.shape)
        for point in label_zero:
            cv2.circle(img, tuple(point),radius,(0,0,255), -1)
        for point in label_one:
            cv2.circle(img, tuple(point),radius,(0,255,255), -1)
        # 利用刚性物体的特性按照x坐标进行排序

        cv2.imwrite(os.path.join(outputdir,"point"+str(imagename)+'.jpg'),img)
        # img = img_temp + img
        # cv2.GaussianBlur(img_temp,(gauss, gauss),0)
        #分开状态
        if label_one.shape[0] == label_zero.shape[0]:
            label_one = np.array(sorted(label_one, key=lambda x: x[0]))
            label_zero = np.array(sorted(label_zero, key=lambda x: x[0]))
            for i, _ in enumerate(label_zero):
                cv2.line(img, tuple(label_zero[i]), tuple(label_one[i]), (0,200,100), 2)

         # 闭合状态
        if label_one.shape[0] == label_zero.shape[0]/2.0:
            label_one = np.array(sorted(label_one, key=lambda x: x[1]))
            label_zero = np.array(sorted(label_zero, key=lambda x: x[1]))
            for i, _ in enumerate(label_one):
                cv2.line(img, tuple(label_zero[2*i]), tuple(label_one[i]), (0,200,100), 2)
                cv2.line(img, tuple(label_zero[2*i+1]), tuple(label_one[i]), (0,200,100), 2)
        cv2.imwrite(os.path.join(outputdir, "line" + str(imagename) + '.jpg'), img)
        cv2.imshow(str(imagename), img)
        # cv2.imshow(str(imagename)+"hm", img_temp)
        cv2.waitKey(0)


if __name__ == "__main__":
    print("OK")
    draw_images()

