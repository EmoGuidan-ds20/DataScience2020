import requests
from bs4 import  BeautifulSoup
import  re
import json
from tqdm import tqdm
import time
import random
#获得视频评论，整理视频信息
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
class BiliSpider(object):
    def get_every_comment(self,aid):
        headers = {
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "origin": "https://www.bilibili.com",
            "referer": "https://www.bilibili.com/video/BV1Z5411Y7or?from=search&seid=8575656932289970537",
            "cookie": "_uuid=0EBFC9C8-19C3-66CC-4C2B-6A5D8003261093748infoc; buvid3=4169BA78-DEBD-44E2-9780-B790212CCE76155837infoc; sid=ae7q4ujj; DedeUserID=501048197; DedeUserID__ckMd5=1d04317f8f8f1021; SESSDATA=e05321c1%2C1607514515%2C52633*61; bili_jct=98edef7bf9e5f2af6fb39b7f5140474a; CURRENT_FNVAL=16; rpdid=|(JJmlY|YukR0J'ulmumY~u~m; LIVE_BUVID=AUTO4315952457375679; CURRENT_QUALITY=80; bp_video_offset_501048197=417696779406748720; bp_t_offset_501048197=417696779406748720; PVID=2",
            "user-agent": random.choice(user_agent),
        }
        #pn:评论页号，oid:AV号,sort=2:按热度排序,sort=1按时间排序
        url='https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid='+aid+'&sort=2'
        Comment_of_one_video = []
        response = requests.get(url, headers=headers)
        data = response.json()
        if(data.get('data')==None):
            return "error"
        if data['data']['replies']:
            for i in data['data']['replies']:
                Comment_of_one_video.append(i['content']['message'])
        return Comment_of_one_video

    def get_information_of_one_video(self,url):
        headers = {
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "origin": "https://www.bilibili.com",
            "referer": "https://www.bilibili.com/video/BV1Z5411Y7or?from=search&seid=8575656932289970537",
            "cookie": "_uuid=0EBFC9C8-19C3-66CC-4C2B-6A5D8003261093748infoc; buvid3=4169BA78-DEBD-44E2-9780-B790212CCE76155837infoc; sid=ae7q4ujj; DedeUserID=501048197; DedeUserID__ckMd5=1d04317f8f8f1021; SESSDATA=e05321c1%2C1607514515%2C52633*61; bili_jct=98edef7bf9e5f2af6fb39b7f5140474a; CURRENT_FNVAL=16; rpdid=|(JJmlY|YukR0J'ulmumY~u~m; LIVE_BUVID=AUTO4315952457375679; CURRENT_QUALITY=80; bp_video_offset_501048197=417696779406748720; bp_t_offset_501048197=417696779406748720; PVID=2",
            "user-agent": random.choice(user_agent),
        }
        print(url)
        #从视频的url获得视频的信息：播放量，弹幕量，点赞数，投币数，收藏数，分享量，返回信息字典
        response = requests.get(url, headers=headers)
        home_page = response.content.decode()
        soup = BeautifulSoup(home_page, 'lxml')
        a = str(soup.find(attrs={'class':'video-data'}))
        if(a=="None"):
            return "error"
        b=str(soup.find(attrs={'class':'ops'}))
        view=re.findall('总播放数(\d+)">',a)[0]
        dm=re.findall('历史累计弹幕数(\d+)">',a)[0]
        like=re.findall('点赞数(\d+)">',b)[0]
        coin=re.findall('投硬币枚数(\d+)">',b)
        if(len(coin)==0):
            coin=re.findall('van-icon-videodetails_throw" style="color:;"></i>\s+(\d+\.?\d+万?)',b)
            if(len(coin)==0):
                coin=0
            else:
                coin=coin[0]
        else:
            coin=coin[0]
        collect=re.findall('收藏人数(\d+)">',b)
        if(len(collect)==0):
            collect=re.findall('van-icon-videodetails_collec" style="color:;"></i>(\d+\.?\d+万?)',b)
            if(len(collect)==0):
                collect=0
            else:
                collect=collect[0]
        else:
            collect=collect[0]
        share=re.findall('"van-icon-videodetails_share"></i>(\d+\.?\d+万?)',b)
        if(len(share)==0):
            share=re.findall('"van-icon-videodetails_share"></i>(\d+)',b)
            if(len(share)==0):
                share=0
            else:
                share=share[0]
        else:
            share=share[0]
        dic = {"view": view, "dm": dm,"like":like,"coin":coin,"collect":collect,"share":share}
        return dic
    def run(self):
        with open('data/video_1.json', encoding='utf8') as fp:
            video_list = json.load(fp)
        with open('data/Danmu.json',encoding='utf8') as fp:
            danmu_list=json.load(fp)
        all_list = []
        index=0
        for per in tqdm(video_list,'采集评论及视频信息'):
            information=self.get_information_of_one_video(per[3])
            if information=="error":
                continue
            comment=self.get_every_comment(per[1])
            if comment=="error":
                continue
            dic={"date":per[2],"information":information,"url":per[3],"aid":per[1],"cid":per[0],"title":per[4],"comment":comment,"danmu":danmu_list[index][0]}
            index+=1
            all_list.append(dic)
            time.sleep(random.randint(1, 3))
            with open('data/All_Bili.json','w',encoding='utf8') as fp:
                json.dump(all_list,fp,ensure_ascii=False)
        





if __name__ == '__main__':
    spider = BiliSpider()
    spider.run()











