# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:00:03 2020

@author: 涅

plot()颜色设置：
‘b’是蓝色，‘g’是绿色，‘r’是红色，‘c’是青绿色，‘m’是洋红色，‘y’是黄色，‘k’是黑色，‘w’是白色



"""
import xlrd
import numpy as np
import matplotlib.pyplot as plt

x_data=[]
y_data=[]

data = xlrd.open_workbook(r'change.xls')
table = data.sheets()[0]

day= int(input("请输入减肥的天数："))

#取出第1列的出来放入cap
cap1 = table.col_values(1)

#再依次输入进入x_data中
for i in range(2,day+1): #2020_12_3 改为10
    x_data.append(cap1[i])

#取出第2列的出来放入cap
cap2 = table.col_values(2)
#再依次输入进入x_data中
for i in range(2,day+1): #2020_12_3 改为10
    y_data.append(cap2[i])

#设置坐标轴范围
plt.xlim((0, 62))
plt.ylim((100, 200))

#测试部分：

plt.scatter([145],[149.8],s=25,c='r') # 标注最小值
# 点的标签（座标中加减的 `0.15` 是显示位置的偏移，避免挡住点）
#ha用来设置 字体部分所在的水平位置，va用来设置上下部分
plt.text(145, 149.8, 'minima', ha='left', va='bottom', fontsize=10.5)  # horizontal alignment


# 画两条虚线
#设置水平虚线
plt.plot([0, 146], [149.8, 149.8],  c='r', linestyle='--')
#设置垂直虚线
plt.plot([146, 146], [149.8, 0],  c='r', linestyle='--')

#---------------------------------------------

#设置坐标轴刻度
my_x_ticks = np.arange(0, 205, 10)
my_y_ticks = np.arange(100, 205, 5)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)

plt.plot(x_data, y_data, 'bo-', linewidth = 1.5,markersize=0)
plt.title('Feedback Figure')
plt.legend()

#设置坐标轴名称
plt.xlabel('Number of Days to Lose Weight  (time)')
plt.ylabel('My Weight Change (g)')
plt.show()
