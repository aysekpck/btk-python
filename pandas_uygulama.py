
import pandas as pd
import numpy as np

df=pd.read_csv("IMDB_datas.csv")

 #1. ilk 5i verir
result=df.head()

 #2. ilk 10
result=df.head(10)

 #3. son 5
result=df.tail(5)

 #4. son 10
result=df.tail(5)

 #5. movielerin ilk beşi
result=df["Movie_Title"].head()

 #6. sadece movie_title kolonu
result=df["Movie_Title"]

 #7. sadece movie_title ve rating içeren ilk beş kayıt
result=df[["Movie_Title","Rating"]].head(5)

 #8. sadece movie_title ve rating içeren son yedi kayıt
result=df[["Movie_Title","Rating"]].tail(7)

 #9. sadece movie_title ve rating içeren ikinci beş kayıt
result=df[5:][["Movie_Title","Rating"]].head(5)

 #10. sadece movie_title ve rating içeren ve imdb 8 üstü olan ilk 50 kayıt
result=df[df["Rating"]>=8.0][["Movie_Title","Rating"]].head(5)
print(result)
