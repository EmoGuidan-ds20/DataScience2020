import requests
from bs4 import  BeautifulSoup
import  re
import json
from tqdm import tqdm
video=[]
#获取以“疫”为关键词搜索出的前1000个视频的aid,上传时间，url（含BV号）,标题
class BiliDanmuSpider(object):
    def __init__(self):
        self.home_url='https://search.bilibili.com/all?keyword=%E7%96%AB&from_source=nav_suggest_new&order=totalrank&duration=0&tids_1=0'
    def get_title_of_one_page(self,url):
        global video
        print(url)
        response=requests.get(url)
        home_page=response.content.decode()
        #print(home_page)
        soup = BeautifulSoup(home_page, 'lxml')
        page = soup.find_all(attrs={'class':'img-anchor'})
        time=soup.find_all(attrs={'title':'上传时间'})
        aid=soup.find_all('script')
        #print(page)
        #print(date)
        rs=re.findall('"aid":\d*,',str(aid[7]))
        #print(rs)
        date=[];url_list=[];name_list=[];aid_list=[]
        for i in range(0,len(time)):
            date.append(time[i].text[9:19])
        for i in range(0,len(page)):
            url_list.append('https:'+page[i].attrs.get('href'))
        for i in range(0,len(page)):
            name_list.append(page[i].attrs.get('title'))
        for per in rs:
            if per[6:15].find(',')!=-1:
                aid_list.append(per[6:14])
            else:
                aid_list.append(per[6:15])
        #print(aid_list)
        for i in range(0,len(date)):
            video.append(('oid',aid_list[i],date[i],url_list[i],name_list[i]))
        #print(video)
    def run(self):
        page_url=['https://search.bilibili.com/all?keyword=%E7%96%AB&from_source=nav_suggest_new']
        for i in range(2,51):
            page_url.append('https://search.bilibili.com/all?keyword=%E7%96%AB&from_source=nav_suggest_new&page='+str(i))
        for page in tqdm(page_url,'采集视频aid'):
            self.get_title_of_one_page(page)
        with open('data/video.json','w',encoding='utf8') as fp:
            json.dump(video,fp,ensure_ascii=False)
        '''with open('data/video.json', encoding='utf8') as fp:
           video_list = json.load(fp)
        print(len(video_list)) #1000个视频'''


if __name__ == '__main__':
    spider = BiliDanmuSpider()
    spider.run()