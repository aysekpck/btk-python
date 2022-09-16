import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

data={
        "Column1":[1,2,3,4,5],
        "Column2":[10,20,13,45,25],
        "Column3":["abc","bcaa","ade","cb","dea"]
}

df=pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2= lambda x: x*x


result=df

result=df["Column2"].unique() #tekrarlamayan verileri verir
result=df["Column2"].value_counts() #hangi veriden kaç adet old verir
result=df["Column1"]*2
result=df["Column1"].apply(kareal)
result=df["Column1"].apply(kareal2)
result=df["Column3"].apply(len) #elemanların karakter sayısını verir
result=df.sort_values("Column2") #artan şekilde sıralar
result=df.sort_values("Column3") #alfabetik olarak sıralar
result=df.sort_values("Column3",ascending=False) #tersi yönde sıralar


print(result)


data={
    "Ay":["mayıs","haziran","nisan","mayıs","haziran","nisan","mayıs","haziran","nisan"],
    "Kategori":["elektrnik","elektrnik","elektrnik","kitap","kitap","kitap","giyim","giyim","giyim"],
    "Gelir":[20,30,15,14,32,42,12,36,52]
}

df=DataFrame(data)

print(df.pivot_table(index="Ay",columns="Kategori",values="Gelir"))



















