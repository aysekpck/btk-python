import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data,index=["a","c","e","f","h"], columns= [ "column1","column2","column3"])
df = df.reindex(["a","b","c","d","e","f","g","h"])

#NP.NAN İLE YENİ KOLON EKLENDİ
newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10] 
df["Column4"]= newColumn

result=df
result=df.drop("column1",axis=1) #colum1 i siler
result=df.drop(["column1","column2"],axis=1)
result=df.drop("a",axis=0) #a indeksini siler axis satıra karşılık gelmesi içim 0 yapılmalı
result=df.drop("b",axis=0) #b yi siler axis yine 0

#Nan olanları tespit etme
result=df.isnull() #Nan olanları True şeklinde verir 
result=df.notnull() #isnull un tam tersi
result = df.isnull().sum() #nerede kaç Nan olduğunu verir
result= df["column1"].isnull().sum() #volumn1 de kaç tane oldyğyny verir
result= df[df["column1"].isnull()]["column1"] #column1de Nan olan satırları verir

result=df.dropna() #axis=0 satıra göre silme yapar (bir NaN olsa bile siler)
result=df.dropna(how="all") #hepsini silmez
result=df.dropna(subset= ["column1","column2"]) #1 ve 2 de hiç NaN KALMAZ
result=df.dropna(thresh=2) #en az 2 mormal veri bulunsun demek
result=df.fillna(value="ayşe") #Nan olan alanları value ile doldurur

result=df.sum()
result=df.size #eleman sayısı
result=df.sum().sum()

def ortalama(df):
    toplam=df.sum().sum()
    adet=df.size-df["column1"].isnull().sum().sum()
    return toplam / adet
result=df.fillna(value=ortalama(df))

print(result)
