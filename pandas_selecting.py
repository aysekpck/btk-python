import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index =["A","B","C"], columns= ["COLUMNS1","COLUMNS2","COLUMNS3"])

result=df
result=df["COLUMNS1"]
result=type(df["COLUMNS1"])
result=df[["COLUMNS1","COLUMNS2"]]


result=df.loc["A"] #A yi gösterir 
result=df.loc[:,"COLUMNS1"] #kolon1 i alır
result=df.loc[:,["COLUMNS1","COLUMNS2"]]
result=df.loc[:,"COLUMNS1":"COLUMNS2"] #KOLON 1 VE 2 ARASI ALINIR
result=df.loc[:,:"COLUMNS3"] #BAŞLANGIÇTAN KOLON3 E KADAR
result=df.loc["A":"B",:"COLUMNS3"] 
result=df.iloc[2] 

df["COLUMNS4"] = pd.Series(randn(3), ["A","B","C"]) #4 KOLON OLUT YOPLAM
df["COLUMNS5"] = df["COLUMNS1"] + df["COLUMNS3"] 

print(df.drop("COLUMNS5",axis=1))
#print(result)
print(df)

