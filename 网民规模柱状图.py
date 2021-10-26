# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def draw_bar(labels, quants):
    width = 0.8
    ind = np.linspace(0.5, 9, 9)
    # make a square figure
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind - width / 2 + 0.4, quants, width, align='center', color='green')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel('年份')
    ax.set_ylabel('网民规模 (亿人)')
    # title
    # ax.set_title('我国网民规则趋势图', bbox={'facecolor': '0.8', 'pad': 5})
    # plt.grid(True)
    plt.show()
    plt.savefig("./img/网民规模趋势图.jpg")
    plt.close()


labels = ["2013.12", "2014.12", "2015.12", "2016.12", "2017.12", "2018.12", "2019.6", "2020.3", "2021.6"]

quants = [6.17, 6.48, 6.88, 7.31, 7.71, 8.28, 8.54, 9.03, 10.11]

draw_bar(labels, quants)
