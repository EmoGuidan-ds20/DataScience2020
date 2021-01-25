from pretreatment import Standard
from LDA import KeyAnalysis
import json
from tqdm import tqdm
file1=['origin-data/cm1.json','origin-data/bili1.json','origin-data/ysxw12.9-1.22.json','origin-data/ttxw1.json']
file2=['origin-data/cm2.json','origin-data/bili2.json','origin-data/ysxw1.23-2.7.json','origin-data/ttxw1.23-2.7.json']
file3=['origin-data/cm3.json','origin-data/bili3.json','origin-data/ysxw2.10-2.13.json','origin-data/ttxw2.10-2.13.json']
file4=['origin-data/cm4.json','origin-data/bili4.json','origin-data/ysxw4.json','origin-data/ttxw3.10-6.json']
standard=Standard()
lda = KeyAnalysis()
flags = ('n', 'nr', 'ns', 'eng', 'v', 'd', 'a')  # 词性
with open('stopwords/stopwords.json', encoding='utf8') as fp: #停用词表
    stopwords= json.load(fp)
index=0
for per in tqdm(file4):#共4个时间段：每次修改file编号及LDA.py中打开和写入的dictionary编号
    #标准化后进入LDA模型，得到关键词
    if index==0:
        list = standard.dealRenmin(per)
    elif index==1:
       list=standard.dealBili(per)
    else:
        list=standard.dealOther(per)
    num = int(len(list) * 0.2)
    if num==0:
        num=1
    for i in tqdm(range(0,num),'采集关键词'):
        lda.LDA(list[i]['text'], stopwords, flags)
    index+=1