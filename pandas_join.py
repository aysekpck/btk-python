
import pandas as pd
import numpy as np

v1=pd.DataFrame({"anahtar":["b","b","c","c","d","e"],"say1":range(6)})
v2=pd.DataFrame({"anahtar":["b","c","d","e"],"say2":range(4)})

print(v1)
print(v2)

result=pd.merge(v1,v2)
print(result)

result=pd.merge(v1,v2,on="anahtar")