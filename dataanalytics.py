import pandas as pd
import matplotlib.pyplot as plt
names=['Bob','narendra','john','rajesh','ravi']
births=[962,522,277,652,785]
Babydataset=list(zip(names,births))
print(Babydataset)
df=pd.DataFrame(data=Babydataset,columns=['names','births'])
print(df)
df.to_csv('births.csv',index=False,header=False)
df=pd.read_csv('births.csv')
print(df)
df=pd.read_csv('births.csv',header=None)
print(df)
df=pd.read_csv('births.csv',names=['names','births'])
print(df)
sorted=df.sort_values(['births'],ascending=True)
print(sorted)
print(sorted.head(1))
print(df['births'].max())
print(df['births'].mean())
print(df['births'].std())
plt.plot([1,2,3,4,5],list(sorted['births']))
plt.show()