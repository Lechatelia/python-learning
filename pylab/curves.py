import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import  scipy.interpolate as si

import numpy


def smooth(x, window_len=11, window='flat',mode='valid'):
    """smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    input:
        x: the input signal
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.
        mode : {'full', 'valid', 'same'}, optional

    output:
        the smoothed signal

    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)

    see also:

    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter

    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise ValueError( "smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")

    if window_len < 3:
        return x

    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError ("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s = numpy.r_[x[window_len - 1:0:-1], x, x[-2:-window_len - 1:-1]]
    # print(len(s))
    if window == 'flat':  # moving average
        w = numpy.ones(window_len, 'd')
    else:
        w = eval('numpy.' + window + '(window_len)')

    y = numpy.convolve(w / w.sum(), s, mode=mode)
    # return y
    return y[(window_len //2 ):-(window_len // 2)]

def zc_read_csv(filename):
    zc_dataframe = pd.read_csv(filename, sep=",")
    x = []
    y = []
    for zc_index in zc_dataframe.index:
        zc_row = zc_dataframe.loc[zc_index]
        x.append(zc_row["step"])
        y.append(zc_row["validation_error"])
    return x,y

def draw_curves(filenames, labels,savefile,window_length=151,mode=0,xmin=0,xmax=1000):
    fig = plt.figure()
    fig.set_size_inches(3.5, 3)  # 整个绘图区域的宽度10和高度4
    ax = fig.add_subplot(1, 1, 1)  # 整个绘图区分成一行两列，当前图是第一个。
    # ax.set_title("L1")
    # ax.set_xlabel("Step")
    ax.set_xticks(np.arange(0,25000,5000))
    # ax.set_ylabel("Error")
    ax.set_ylim(0,0.7)
    ax.set_xticklabels(['0K','5K','10k','15k','20k'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)

    colors = ['r-','orange','g-','aqua','navy','coral']
    for i, file in enumerate(filenames):
        x, y = zc_read_csv(file)
        # 获得画图对象。
        if mode == 0:
            x = np.array(x[xmin:xmax])
            y = np.array(y[xmin:xmax])
        elif mode ==1 :
            if i < 3:
                x = np.array(x[xmin:xmax*2:2])
                y = np.array(y[xmin:xmax*2:2])
            else:
                x = np.array(x[xmin:xmax])
                y = np.array(y[xmin:xmax])
        elif mode == 2:
            if i < 1:
                x = np.array(x[xmin:xmax*2:2])
                y = np.array(y[xmin:xmax*2:2])
            else:
                x = np.array(x[xmin:xmax])
                y = np.array(y[xmin:xmax])


        # x_new = np.linspace(xmin,xmax,(xmax-xmin))
        # y_new = si.spline(x,y,x_new)
        y = smooth(y,window_length)
        # 画出原始数据的散点图。
        # ax.set_label(labels[i])
        # ax.scatter(x, y)
        if mode==2:
            ax.plot(x[0:1150], y[0:1150], colors[i], label=labels[i],linewidth=2)
        else:
            ax.plot(x, y, colors[i], label=labels[i],linewidth=2)

    plt.legend(loc='upper right', shadow=True, fontsize='medium')
    # plt.grid(True)
    plt.savefig(savefile,format='pdf',bbox_inches='tight')
    plt.show()

def draw_loss():
    filenames=['csv1/20181107_0951.csv',
               'csv1/20181108_0029.csv',
               'csv1/20181108_0941.csv',
               'csv1/20181108_1541.csv',
               'csv1/20181108_2207.csv']
    labels = [r'$\alpha$1',
              r'$\alpha$2',
              r'$\alpha$3',
              r'$\alpha$4',
              r'$L2$ '
              ]
    draw_curves(filenames,labels,"loss_compare.pdf",window_length=151,mode=1)

def draw_structrue_compare():
    filenames=['csv2/20181107_0951.csv',
               'csv2/20181113_0927.csv',
               'csv2/20181112_1745.csv',
               'csv2/20181110_1752.csv']
    labels = [r'RAN  & REG-$\alpha$1',
              r'Plain & REG-$\alpha$1',
              r'RAN  & CLASS-6',
              r'Plain & CLASS-6'
              ]
    draw_curves(filenames, labels,"structure_compare.pdf",window_length=151, mode=2,xmin=0,xmax=1300)


def draw_loss_function(savefile,x_max):

    fig = plt.figure()
    fig.set_size_inches(3.5, 3)  # 整个绘图区域的宽度10和高度4
    ax = fig.add_subplot(1, 1, 1)  # 整个绘图区分成一行两列，当前图是第一个。
    # ax.set_title("L1")
    ax.set_xticks(np.arange(-20, 25, 10))
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    # plt.title("一元一次函数")
    x = np.arange(-x_max, x_max + 1, 1)
    for i in range(1,5,1):
        y = pow(abs(0.1 * x), i)*(abs(x )< 10)+(abs(0.1 * x) * i - i+1)*(abs(x )>= 10)
        ax.plot(x, y, label=r'$\alpha${num}'.format(num=i),linewidth=2)
    y = pow(abs(0.1 * x), 2)
    ax.plot(x, y, '--',label='L2',linewidth=2)
    plt.legend(loc='upper center', shadow=True, fontsize='medium')
    plt.savefig(savefile, format='pdf', bbox_inches='tight')
    plt.show()

def draw_loss_function2(savefile,x_max):

    fig = plt.figure()
    fig.set_size_inches(3.5, 3)  # 整个绘图区域的宽度10和高度4
    ax = fig.add_subplot(1, 1, 1)  # 整个绘图区分成一行两列，当前图是第一个。
    # ax.set_title("L1")
    ax.set_xticks(np.arange(-30, 35, 10))
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    # plt.title("一元一次函数")
    x = np.arange(-x_max, x_max + 1, 1)
    for i in range(2,3,1):
        y = pow(abs(0.1 * x), i)*(abs(x )< 10)+(abs(0.1 * x) * i - i+1)*(abs(x )>= 10)
        ax.plot(x, y, label=r'$\alpha${num}'.format(num=i),linewidth=2)
    y = pow(abs(0.1 * x), 2)
    ax.plot(x, y, '--',label='L2',linewidth=2)

    y = 0.75 * abs(0.1 * x) * (x < 0) + (0.25 * abs(0.1 * x)) * (x>0)
    ax.plot(x, y, label=r'quantile-0.25', linewidth=2)

    y = 0.25 * abs(0.1 * x) * (x < 0) + (0.75 * abs(0.1 * x)) * (x > 0)
    ax.plot(x, y, label=r'quantile-0.75', linewidth=2)

    y =np.log(np.cosh(0.1*x))
    ax.plot(x, y, label=r'log-cosh', linewidth=2)

    plt.legend(loc='upper center', shadow=True, fontsize='medium')
    plt.savefig(savefile, format='pdf', bbox_inches='tight')
    plt.show()

if __name__=='__main__':
    # draw_loss()
    # draw_structrue_compare()
    # draw_loss_function('loss_function.pdf',22)
    draw_loss_function2('robust_loss_function.pdf',22)

