import pandas as pd

df1 = pd.read_csv('양파 2009년.csv', encoding='cp949')
df1 = df1.add_prefix('2009/')
df1 = df1.rename({'2009/구분':'구분'}, axis='columns')
df1 = df1.transpose()
print(df1)

df2 = pd.read_csv('양파 2010년.csv', encoding='cp949')
df2 = df2.add_prefix('2010/')
df2 = df2.transpose()
df2 = df2.drop(['2010/구분'], axis=0)
print(df2)

df3 = pd.read_csv('양파 2011년.csv', encoding='cp949')
df3 = df3.add_prefix('2011/')
df3 = df3.transpose()
df3 = df3.drop(['2011/구분'], axis=0)
print(df3)

df4 = pd.read_csv('양파 2012년.csv', encoding='cp949')
df4 = df4.add_prefix('2012/')
df4 = df4.transpose()
df4 = df4.drop(['2012/구분'], axis=0)
print(df4)

df5 = pd.read_csv('양파 2013년.csv', encoding='cp949')
df5 = df5.add_prefix('2013/')
df5 = df5.transpose()
df5 = df5.drop(['2013/구분'], axis=0)
print(df5)

df6 = pd.read_csv('양파 2014년.csv', encoding='cp949')
df6 = df6.add_prefix('2014/')
df6 = df6.transpose()
df6 = df6.drop(['2014/구분'], axis=0)
print(df6)

df7 = pd.read_csv('양파 2015년.csv', encoding='cp949')
df7 = df7.add_prefix('2015/')
df7 = df7.transpose()
df7 = df7.drop(['2015/구분'], axis=0)
print(df7)

df8 = pd.read_csv('양파 2016년.csv', encoding='cp949')
df8 = df8.add_prefix('2016/')
df8 = df8.transpose()
df8 = df8.drop(['2016/구분'], axis=0)
print(df8)

df9 = pd.read_csv('양파 2017년.csv', encoding='cp949')
df9 = df9.add_prefix('2017/')
df9 = df9.transpose()
df9 = df9.drop(['2017/구분'], axis=0)
print(df9)

df10 = pd.read_csv('양파 2018년.csv', encoding='cp949')
df10 = df10.add_prefix('2018/')
df10 = df10.transpose()
df10 = df10.drop(['2018/구분'], axis=0)
print(df10)

df11 = pd.read_csv('양파 2019년.csv', encoding='cp949')
df11 = df11.add_prefix('2019/')
df11 = df11.transpose()
df11 = df11.drop(['2019/구분'], axis=0)
print(df11)

total = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11])
total = total.rename(columns=total.iloc[0])
total = total.drop(total.index[0])
print(total)
total.to_csv('양파_09~19년.csv')