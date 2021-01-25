from operator import itemgetter
import json
from datetime import datetime
class Standard(object):
    #标准化，dealBili()得到列表项格式为{"date":xxxx-xx-xx,"text":[]},
    #dealRenmin()和dealOther()得到列表项格式为{"date":xxxx-xx-xx,"text":[],"main":xxxxxxx}(main内即正文)
    def dealBili(self,file):
        with open(file, encoding='utf8') as fp:
            origin_list = json.load(fp)
        list=[]
        for per in origin_list:
            newper={'date':per['date'],'text':((per['comment'])+(per['danmu']))}
            list.append(newper)
        list1=sorted(list,key=itemgetter('date'))
        print(list1)
        return list1
    def dealRenmin(self,file,index):
        with open(file, encoding='utf8') as fp:
            origin_list = json.load(fp)
        list=[]
        for per in origin_list:
            comment=[]
            for i in range(3,len(per)):
                comment.append(per[i])
            if index!=3:
                newper={'date':"2020-"+per[1][0:4],'text':comment,'main':per[0]}
                d = "2020-" + per[1][0:4]
                if '-' in d[5:7]:
                    d = d[0:5] + '0' + d[5:]
                newper = {'date': d, 'text':comment,'main':per[0]}
            else:
                newper={'date':datetime.strptime(per[1], '%Y/%m/%d %H:%M').strftime('%Y-%m-%d'),'text':comment,'main':per[0]}
            list.append(newper)
        list1=sorted(list,key=itemgetter('date'))
        print(list1)
        return list1
    def dealOther(self,file):
        with open(file, encoding='utf8') as fp:
            origin_list = json.load(fp)
        list=[]
        for per in origin_list:
            main=per["微博内容:"]
            text=per["评论"]
            date=per["发布时间:"][4:10]+" "+per["发布时间:"][26:]
            date=datetime.strptime(date, '%b %d %Y').strftime('%Y-%m-%d')
            newper={'date':date,'text':text,'main':main}
            list.append(newper)
        list1=sorted(list,key=itemgetter('date'))
        print (list1)
        return list1

''''#调试pretreatment
    def run(self):
        self.dealRenmin('origin-data/cm1.json',1)
if __name__ == '__main__':
    sta = Standard()
    sta.run()'''