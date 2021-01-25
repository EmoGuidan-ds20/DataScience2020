import requests
from bs4 import  BeautifulSoup
import json
import random
from tqdm import tqdm
import time
user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
#获得所有视频弹幕
class BiliDanmuSpider(object):
    def get_every_Danmu(self,list):
        headers = {
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "origin": "https://www.bilibili.com",
            "referer": "https://www.bilibili.com/video/BV1Z5411Y7or?from=search&seid=8575656932289970537",
            "cookie": "_uuid=0EBFC9C8-19C3-66CC-4C2B-6A5D8003261093748infoc; buvid3=4169BA78-DEBD-44E2-9780-B790212CCE76155837infoc; sid=ae7q4ujj; DedeUserID=501048197; DedeUserID__ckMd5=1d04317f8f8f1021; SESSDATA=e05321c1%2C1607514515%2C52633*61; bili_jct=98edef7bf9e5f2af6fb39b7f5140474a; CURRENT_FNVAL=16; rpdid=|(JJmlY|YukR0J'ulmumY~u~m; LIVE_BUVID=AUTO4315952457375679; CURRENT_QUALITY=80; bp_video_offset_501048197=417696779406748720; bp_t_offset_501048197=417696779406748720; PVID=2",
            "user-agent": random.choice(user_agent),
        }
        url='https://api.bilibili.com/x/v1/dm/list.so?oid='+str(list[0])
        Danmu_of_one_video=[]
        response = requests.get(url, headers=headers)
        home_page = response.content.decode()
        print(home_page)
        soup = BeautifulSoup(home_page, 'lxml')
        danmu_1 = soup.find_all('d')
        for per in danmu_1:
            Danmu_of_one_video.append(per.text)
        print(Danmu_of_one_video)
        return Danmu_of_one_video
    def run(self):
        with open('data/video_1.json', encoding='utf8') as fp:
            video_list = json.load(fp)
        Danmu_list=[]
        for per in tqdm(video_list,'采集弹幕'):
            Danmu_list.append((self.get_every_Danmu(per),per[0],per[2],per[3],per[4]))
            #[弹幕，cid，时间，url,标题]
            time.sleep(random.randint(1, 3))
        with open('data/Danmu.json','w',encoding='utf8') as fp:
            json.dump(Danmu_list,fp,ensure_ascii=False)


if __name__ == '__main__':
    spider = BiliDanmuSpider()
    spider.run()