import json
import datetime
from tqdm import tqdm
#按时间分类可用视频
class BiliSort(object):
    def CutIntoFour(self):
        with open('data/All_Bili.json', encoding='utf8') as fp:
            list = json.load(fp)
        #print(len(list)) #968
        list_1=[]#2019——2020-01-22
        list_2=[]#2020-01-23——2020-02-09
        list_3=[]#2020-02-10——2020-03-09
        list_4=[]#2020-03-10——2020
        for per in tqdm(list,'初步分段'):
            date=per["date"]
            if date[0:4]=="2019":
                list_1.append(per)
            else:
                if date[5:6]=="0":
                    if date[6:7]=="1":
                        if int(date[8:10])<=22:list_1.append(per)
                        else:list_2.append(per)
                    elif date[6:7]=='2':
                        if int(date[8:10])<=9:list_2.append(per)
                        else:list_3.append(per)
                    elif date[6:7]=='3':
                        if int(date[8:10])<10:list_3.append(per)
                        else:list_4.append(per)
                    else:list_4.append(per)
                else:list_4.append(per)
        with open('data/Bili_1.json', 'w', encoding='utf8') as fp:
            json.dump(list_1, fp, ensure_ascii=False)#22
        with open('data/Bili_2.json', 'w', encoding='utf8') as fp:
            json.dump(list_2, fp, ensure_ascii=False)#68
        with open('data/Bili_3.json', 'w', encoding='utf8') as fp:
            json.dump(list_3, fp, ensure_ascii=False)#142
        with open('data/Bili_4.json', 'w', encoding='utf8') as fp:
            json.dump(list_4, fp, ensure_ascii=False)#736
    def run(self):
        self.CutIntoFour()


if __name__ == '__main__':
    sort=BiliSort()
    sort.run()