import json
#去除词典中的重复词
file0 = ['data/dictionary1.json', 'data/dictionary2.json', 'data/dictionary3.json', 'data/dictionary4.json']
for file in file0:
    with open(file, encoding='utf8') as fp:
        origin_dic = json.load(fp)
    s=set(origin_dic)
    l=list(s)
    with open(file, 'w', encoding='utf8') as fp:
        json.dump(l, fp, ensure_ascii=False)
    print(l)