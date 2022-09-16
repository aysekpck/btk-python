#PANDAS İLE FARKLI DOSYA TİPLERİNDEN VERİ OUKMA

import pandas as pd

df=pd.read_csv("netflix_titles_for_pandas.csv")
print(df)
#df.head() ilk beşi verir
#df=pd.read_excel("netflix_titles_for_pandas.xlsx") excel dosyası okuma
# bunu çalıştırmak için pip install xlrd indirilmeli
