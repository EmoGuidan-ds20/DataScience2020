import csv
import json
import matplotlib.pyplot as plt
from scipy import optimize as op
import numpy as np
from scipy.optimize import curve_fit
import math
from scipy.stats import norm
import matplotlib.mlab as mlab

f = csv.reader(open('央视新闻.csv', 'r',encoding='utf-8'))
cm = list()
for i in f:
    if len(i) != 0 and i[10] != '评论数':
        # print(int(i[2][2:len(i[2])-1]))
        cm.append(int(i[10]))
viewres = list()
temp = 0
i = 0
x = list()
y = list()
cm.sort()
print(cm)
delt = 50
for vi in cm:
    if delt * i <= vi < delt * (i + 1):
        temp += 1
    else:
        if temp != 0:
            x.append(delt * (i + 0.5))
            y.append(temp)
            temp = 0
        while vi > delt * (i + 1):
            i += 1
        temp += 1
x.append(delt * (i + 0.5))
y.append(temp)
xdata = np.array(x)
ydata = np.array(y)


def func(x, a, u, sig, offset):
    return a * (np.exp(-(x - u) ** 2 / (2 * sig ** 2))) + offset


popt, pcov = curve_fit(func, xdata, ydata, p0=(max(y), 0, np.std(cm), 0))  # popt数组中，三个值分别是待求参数a,b,c
y_pred3 = [func(i, popt[0], popt[1], popt[2], popt[3]) for i in xdata]
plt.scatter(xdata, ydata, marker='o', label='real')
plt.plot(xdata, y_pred3, 'y-')
plt.show()
mu = popt[1]
sig = popt[2]
judge = mu + 2 * sig
print(judge)
f2 = csv.reader(open('央视新闻.csv', 'r',encoding='utf-8'))
for j in f2:
    if len(j) != 0 and j[10] != '评论数':
        if int(j[10]) > judge:
            viewres.append(j)
print(viewres)
print(len(cm))
print(len(viewres))

with open('ysxw.json', 'w', encoding='utf-8') as f:
    json.dump(viewres, f, ensure_ascii=False)
