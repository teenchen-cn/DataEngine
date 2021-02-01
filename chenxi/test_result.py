import pandas

data = {'Chinese': [68, 95, 98, 90,80], 'Math': [65, 76, 86, 88, 90], 'English': [30, 98, 88, 77, 90]}
df = pandas.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['Chinese', 'Math', 'English'])
# print(df1)
print(df)

#计算平均值，大小等
print(df.describe())

df['总分']=df.apply(lambda x: x.sum(), axis=1)
df.sort_values(by='总分',inplace=True)
print(df)