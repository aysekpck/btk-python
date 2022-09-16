import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df= pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])

result= df
result = df.columns #dataframede kaç tane kolon olduğunu vrir
result=df.head() #ilk beş kolonu verir(kayıdı)
result=df.head(10) #ilk on kayıt
result=df.tail() #son beşi verir
result=df.tail(10) #son 10 kaydı verir
result= df["Column1"].head() #kolon1 de ilk beşi verir
result=df.Column1.head()  #kolon1 de ilk beşi verir
result=df[5:15][["Column1","Column2"]].head() #5den 9a kadar
result=df[5:15][["Column1","Column2"]] #5den 74e kadar verir

#FİLTRELEME
result=df>50 #50den büyükler için true olmayanlar için false verir
result=df[df>50] #50den büyük verileri gösterir diğerleri için Nan yazar
result=df["Column1" ] >50 #kolon1 de 50den büyük olanlara true verir
result=df[df["Column1" ] >50] #kolon1 de 50den büyük olan verileri gösterir
result=df[(df["Column1" ] >50) & (df["Column1"] <=70)]  #kolon1 in 50den büyük 70den küçük eşit olma koşulu


print(result)