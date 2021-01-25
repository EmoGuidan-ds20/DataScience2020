from operator import itemgetter
import json
#预处理,run函数建立4个空字典
#Standard类下函数：将各个类型数据标准化为可进入LDA模型的格式
class Standard(object):
    def dealBili(self,file):
        with open(file, encoding='utf8') as fp:
            origin_list = json.load(fp)
        list=[]
        for per in origin_list:
            newper={'view':int(per['information']['view']),'text':((per['comment'])+(per['danmu']))}
            list.append(newper)
        list1=sorted(list,key=itemgetter('view'),reverse=True)
        return list1
    def dealRenmin(self,file):
        with open(file, encoding='utf8') as fp:
            origin_list = json.load(fp)
        list=[]
        for per in origin_list:
            comment=[]
            for i in range(3,len(per)):
                comment.append(per[i])
            newper={'commentNum':int(per[2][3:]),'text':([per[0]]+comment)}
            list.append(newper)
        list1=sorted(list,key=itemgetter('commentNum'),reverse=True)
        return list1
    def dealOther(self,file):
        with open(file, encoding='utf8') as fp:
            origin_list = json.load(fp)
        list=[]
        for per in origin_list:
            text=[per["微博内容:"]]+per["评论"]
            newper={'commentNum':per["评论数"],'text':text}
            list.append(newper)
        list1=sorted(list,key=itemgetter('commentNum'),reverse=True)
        #print (list1)
        return list1
    def run(self):
        file0 = ['data/dictionary1.json', 'data/dictionary2.json', 'data/dictionary3.json', 'data/dictionary4.json']
        for per in file0:
            with open(per, 'w', encoding='utf8') as fp:
                json.dump([], fp, ensure_ascii=False)
if __name__ == '__main__':
    sta = Standard()
    sta.run()