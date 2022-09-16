import pandas as pd

data= pd.read_csv("nba.csv")

data.dropna(inplace=True)

data["Name"] = data["Name"].str.upper()

print(data)