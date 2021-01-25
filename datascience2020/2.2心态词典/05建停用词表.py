import json
files=['stopwords/scu_stopwords.txt','stopwords/hit_stopwords.txt','stopwords/cn_stopwords.txt']
words=['up','图片','星座','龙某','觉得','男女','已经', "z7777nnnn","远必","sofronio","另一边","一边", "应该","周某","汪某孝","王某宇","",]
for file in files:
    f = open("stopwords/scu_stopwords.txt", "r", encoding='utf8')  # 设置文件对象
    words0 = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()
    for i in range(0, len(words0)):
        words0[i] = words0[i][:-1]
    words=words+words0
s=set(words)
l=list(s)
with open('stopwords/stopwords.json', 'w', encoding='utf8') as fp:
    json.dump(l, fp, ensure_ascii=False)
print(len(words))