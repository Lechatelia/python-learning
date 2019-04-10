import numpy as np
week1 = [[22, 22, 20], [25, 23, 23.3], [25.3, 24, 26.7]]
week2 = [[32.8, 27.7, 31.5], [29.4, 30.4, 31.5], [32.8,30.2, 28.4]]
week3 = [[35, 32.7, 31.2], [39.3, 36.7, 34.8], [31.1, 40.6, 27]]
week4 = [[38.2, 35.1, 34.6], [42.8, 37.8, 48.3], [37, 39.2, 30.2]]
week5 = [[41.3, 40.9, 38.7], [53, 47.5, 50], [31.9, 44, 42.8]]
week6 = [[43.5, 42.7, 40.6], [54.2, 49.6, 52.3], [33.4, 46.9, 45.3]]
week7 = [[44.7, 43, 43.3], [55, 50.9, 54.1], [33.9, 47.5, 46.7]]

def Dataprocessing(week):
    ave = np.mean(week, axis=1,)  #计算均值
    var = np.var(week, axis=1, ddof=1) # 计算组内方差
    std = np.std(week, axis=1, ddof=1) # 计算组内标准差
    conv_matrix = np.cov(week, ddof=1) # 计算协方差矩阵
    conv = np.array([conv_matrix[0,1], conv_matrix[0,2], conv_matrix[1, 2]]) # 组间协方差
    p = [conv[0]/(std[0]*std[1]), conv[1]/(std[0]*std[2]), conv[2]/(std[1]*std[2])] #组间相关系数
    print(ave)
    print(std)
    print(conv)
    print(p)


if __name__ == "__main__":
    # 分时间计算
    print("------week1-------")
    Dataprocessing(week1)
    print("------week2-------")
    Dataprocessing(week2)
    print("------week3-------")
    Dataprocessing(week3)
    print("------week4-------")
    Dataprocessing(week4)
    print("------week5-------")
    Dataprocessing(week5)
    print("------week6-------")
    Dataprocessing(week6)
    print("------week7-------")
    Dataprocessing(week7)

