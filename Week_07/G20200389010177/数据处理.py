# -*- coding: gbk -*-

import pandas as pd
from snownlp import SnowNLP

# ��������
df = pd.read_csv('F:\python\scrapy\qsbk\qsbk\wenjian.csv',encoding='gbk',delimiter='\t')
df.columns = ['nick','mid','content']

# ��ϴ����
df.drop_duplicates(inplace=True)

# ��з���
def get_sentiment(coment):
    senti_number = SnowNLP(coment).sentiments
    # print(senti_number)
    return senti_number

df['senti'] = df['content'].apply(get_sentiment)