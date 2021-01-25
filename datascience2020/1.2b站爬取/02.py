import requests
from bs4 import  BeautifulSoup
import  re
import json
from tqdm import tqdm
#通过BV号从接口获取所有视频cid，以获得弹幕
class BiliDanmuSpider(object):
    def get_oid(self,list):
        i=0;
        for per in tqdm(list,'采集视频cid'):
            print(per)
            url='https://api.bilibili.com/x/player/pagelist?bvid='+str(per[3])[31:43]+'&jsonp=jsonp'
            #url='https://www.bilibili.com/widget/getPageList?aid='+str(per[1])→易崩坏接口
            #print(url)
            response = requests.get(url)
            home_page = response.content.decode() #string
            #print(home_page)
            cid=re.findall('cid":(\d+),',home_page)
            print(cid)
            list[i][0]=cid[0]
            i+=1
            #print(list[i])
        return list
    def run(self):
        with open('data/video.json', encoding='utf8') as fp:
            video_list = json.load(fp)
        full_list=self.get_oid(video_list)
        with open('data/video_1.json','w',encoding='utf8') as fp:
            json.dump(full_list,fp,ensure_ascii=False) #0:cid,1:aid

if __name__ == '__main__':
    spider = BiliDanmuSpider()
    spider.run()