# 对汽车投诉信息进行分析
import pandas as pd
import numpy as np

result = pd.read_csv('car_complain.csv')
#print(result)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
# print(result.columns)
tags = result.columns[7:]
# print(tags)

df = result.groupby(['brand'])['id'].agg(['count'])
df1 = df.sort_values(by=['count'],ascending=False) #按照brand统计 投诉总数,按照投诉总数进行排序
print(df1)

df2 = result.groupby(['car_model'])['id'].agg(['count'])
df3 = df2.sort_values(by=['count'],ascending=False) #按照car_model统计 投诉总数,按照投诉总数进行排序
print(df3)

df4 = result.groupby(['brand', 'car_model'])['id'].agg(['count'])#按照brand统计 哪个品牌的平均车型投诉最多
df5 = df4.reset_index()
df6 = df5.groupby(["brand"])['count'].agg([np.mean])
print(df6.sort_values('mean', ascending=False))



