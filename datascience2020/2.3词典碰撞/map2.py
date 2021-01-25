from pretreatment import Standard
from operator import itemgetter
import json
import jieba.posseg as pseg
from tqdm import tqdm
file1=['origin-data/cm1.json','origin-data/ysxw12.9-1.22.json','origin-data/ttxw1.json']
file2=['origin-data/cm2.json','origin-data/ysxw1.23-2.7.json','origin-data/ttxw1.23-2.7.json']
file3=['origin-data/cm3.json','origin-data/ysxw2.10-2.13.json','origin-data/ttxw2.10-2.13.json']
file4=['origin-data/cm4.json','origin-data/ysxw4.json','origin-data/ttxw3.10-6.json']
standard=Standard()
index=0
all_list=[]
for per in file4:#共4个时间段：每次修改file编号和打开的词典编号，以及最后存入文件的编号
    #标准化文件
    if index==0:
        list = standard.dealRenmin(per,4)#当运行file3时，将第二个系数设为3！！！
        all_list=all_list+list
    else:
        list=standard.dealOther(per)
        all_list=all_list+list
    index+=1
#得到列表项格式为{"date":xxxx-xx-xx,"text":[],"main":xxxxx}
all_list=sorted(all_list,key=itemgetter('date'))
print(all_list)

with open('origin-data/dictionary4.json', encoding='utf8') as fp:#用来碰撞的第x阶段的词典，每次修改打开字典编号
    dic_list= json.load(fp)

w_f=[]
w_f={word:0 for word in dic_list}#词典词：频率
#print(w_f)
#frequency[i]:每个文本中词典词的词频
frequnency=[]
j=0
for per in tqdm(all_list):
    a_w_f=w_f.copy()
    now=[per['date'],a_w_f]
    i = 0
    sentence=per['main']
    b=[w.word for w in pseg.cut(sentence)]
    for word in dic_list:
        count=0
        for compare_word in b:
            if word ==compare_word:
                count+=1
        now[1][word]=count
    frequnency.append(now)
    j+=1
print(len(frequnency))

#每个日期词典词的词频
past_date=frequnency[0][0]
past_f=frequnency[0][1]
result=[[past_date,past_f]]
i=0
for per in frequnency:
    date=per[0]
    if date==past_date:
        for word in dic_list:
            past_f[word]+=per[1][word]
        result[i]=[date,past_f]
    else:
        i+=1
        result.append(per[:])
        past_date=per[0]
        past_f=per[1]
print(result)
print(len(result))
with open('data/正文4.json', 'w', encoding='utf8') as fp:#每次修改存入文件编号
    json.dump(result, fp, ensure_ascii=False)

#第x阶段词典词的词频
first=result[0][1]
for per in result:
    for word in dic_list:
        first[word]=first[word]+per[1][word]
print(first)
with open('data/正文4.1.json', 'w', encoding='utf8') as fp:#每次修改存入文件编号
    json.dump([first], fp, ensure_ascii=False)