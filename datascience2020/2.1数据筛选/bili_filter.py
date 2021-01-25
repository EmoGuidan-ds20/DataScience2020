import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# 读取json文件内容,返回字典格式
with open('头条新闻1.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    #print('这是文件中的json数据：',json_data[0]['information'])
    #print('这是读取到文件数据的数据类型：', type(json_data[0]['information']['view']))
    #print(len(json_data))
    view = list()
    dm = list()
    like = list()
    for i in range(len(json_data)):
        view.append(int(json_data[i]['information']['view']))
        dm.append(float(json_data[i]['information']['dm']))
        like.append(float(json_data[i]['information']['like']))
    '''
    with open('Bili_2.json', 'r', encoding='utf8')as fp2:
        json_data2 = json.load(fp2)
        # print('这是文件中的json数据：',json_data[0]['information'])
        # print('这是读取到文件数据的数据类型：', type(json_data[0]['information']['view']))
        # print(len(json_data))
        for i in range(len(json_data2)):
            view.append(float(json_data2[i]['information']['view']))
            dm.append(float(json_data2[i]['information']['dm']))
            like.append(float(json_data2[i]['information']['like']))
    with open('Bili_3.json', 'r', encoding='utf8')as fp3:
        json_data3 = json.load(fp3)
        # print('这是文件中的json数据：',json_data[0]['information'])
        # print('这是读取到文件数据的数据类型：', type(json_data[0]['information']['view']))
        # print(len(json_data))
        for i in range(len(json_data3)):
            view.append(float(json_data3[i]['information']['view']))
            dm.append(float(json_data3[i]['information']['dm']))
            like.append(float(json_data3[i]['information']['like']))
    with open('Bili_4.json', 'r', encoding='utf8')as fp4:
        json_data4 = json.load(fp4)
        # print('这是文件中的json数据：',json_data[0]['information'])
        # print('这是读取到文件数据的数据类型：', type(json_data[0]['information']['view']))
        # print(len(json_data))
        for i in range(len(json_data4)):
            view.append(float(json_data4[i]['information']['view']))
            dm.append(float(json_data4[i]['information']['dm']))
            like.append(float(json_data4[i]['information']['like']))
    '''
    viewres=list()
    temp=0
    i=0
    x=list()
    y=list()
    view.sort()
    delt=50000
    for vi in view:
        if delt*i<=vi<delt*(i+1):
            temp+=1
        else:
            if temp!=0:
                x.append(delt*(i+0.5))
                y.append(temp)
                temp=0
            while (vi>delt*(i+1)):
                i+=1
            temp+=1
    x.append(delt * (i + 0.5))
    y.append(temp)
    xdata = np.array(x)
    ydata = np.array(y)
    def func(x, a, u, sig,offset):
        return a * (np.exp(-(x - u) ** 2 / (2 * sig ** 2)))+offset
    popt, pcov = curve_fit(func, xdata, ydata,p0=(max(y), 0,np.std(view), 0))  # popt数组中，三个值分别是待求参数a,b,c
    y_pred3 = [func(i, popt[0],popt[1],popt[2],popt[3]) for i in xdata]
    plt.scatter(xdata, ydata, marker='o', label='real')
    plt.plot(xdata, y_pred3, 'y-')
    plt.show()
    mu=popt[1]
    sig=popt[2]
    judge=mu+2*sig
    print(judge)
    for i in range(len(view)):
        if view[i]>judge:
            viewres.append(json_data[i])
    print(viewres)
    print(len(viewres))
    with open('bili4.json', 'w', encoding='utf-8') as f:
        json.dump(viewres, f, ensure_ascii=False)
