import json
import jieba.posseg as pseg
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
class KeyAnalysis(object):
    def LDA(self,corpus,stopwords,flags):
        # 对语句进行分词，去除词性停用词和不属于要求词性的词，存储语料
        #list内的每一项为一个文档，文档之间的词之间用空格分隔
        i=0
        for sentence in corpus:
            word=[w.word for w in pseg.cut(sentence) if w.flag in flags and w.word not in stopwords]
            corpus[i]=' '.join(word)
            i=i+1
        print(corpus)

        topic_num = 3#主题数

        # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(corpus)
        weight = X.toarray()
        #print(len(weight))
        #print(weight[:35, :35])

        # LDA算法
        #print('LDA:')
        np.set_printoptions(suppress=True)

        model = LatentDirichletAllocation(n_components=topic_num, max_iter=500, random_state=1)
        model.fit_transform(X)
        topic_word = model.components_
        #print("------")
        #print(model)
        #print("------")

        n_top_words = 2 #主题输出前2个关键词
        list=[]
        feature_names =vectorizer.get_feature_names()
        for topic_idx, topic in enumerate(model.components_):
            a_list=[]
            print('\nTopic Nr.%d:' % int(topic_idx + 1))
            print(''.join([feature_names[i] + ' ' + str(round(topic[i], 2)) + ' | ' for i in topic.argsort()[:-n_top_words - 1:-1]]))
            a_list.append(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
            a_list=a_list[0].split(" ")
            list=list+a_list
            #print(a_list)


        #将提取到的关键词加入词典
        with open('data/dictionary4.json', encoding='utf8') as fp:
            origin_list = json.load(fp)
        new_list=origin_list+list
        with open('data/dictionary4.json', 'w', encoding='utf8') as fp:
            json.dump(new_list, fp, ensure_ascii=False)

'''调试LDA
    def run(self):
        with open('origin-data/bili1.json',encoding='utf8') as fp:
            origin_list=json.load(fp)
        print(origin_list[0]['comment'])
        flags = ('n', 'nr', 'ns', 'eng', 'v', 'd', 'a')  # 词性
        stopwords = ['喔']#停用词表
        self.DLA(origin_list[0]['comment'],stopwords,flags)
if __name__ == '__main__':
    ana = KeyAnalysis()
    ana.run()'''
