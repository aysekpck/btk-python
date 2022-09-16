import pandas as pd
import numpy as np

#letters = ["a","b","c","d",20]
#numbers=[20,30,40,50]
#scalar=5
#dict={"a":10,"b":20,"c":30,"d":40}
#random_numbers = np.random.randint(10,100,6)

#pandas_series=pd.Series(letters)
#pandas_series=pd.Series(numbers)
#pandas_series=pd.Series(5,[0,1,2,3]) #her indekse 5 yazar
#pandas_series=pd.Series(numbers,["a","b","c","d"]) #indeks yerine abcd koyar
#pandas_series=pd.Series(random_numbers)

#pandas_series=pd.Series([20,30,40,50],["a","b","c","d"])
#result=pandas_series[0] #20 gösterir
#result=pandas_series.ndim  #boyutumu gösterir bu 1 boyutlu
#result=pandas_series.shape #(4,) verir
#result=pandas_series.sum() toplama
#result=np.sqrtpandas_series karekökü alır
#result=pandas_series >=50 tru false verir

#print(pandas_series)

#print(result)


opel2018=pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019=pd.Series([20,30,20,10],["astra","corsa","grandland","insignia"])
total= opel2018+opel2019
print(total)