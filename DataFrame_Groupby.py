import pandas as pd



personeller = {
    "Çalışan":["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    "Departman":["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","Bilgi İşlem"],
    "Yaş":[30,25,45,50,23,34,42],    
    "Semt":["Kadıköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadıköy"],
    "Maaş":[5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
result=df
result=df["Maaş"].sum() #maaşları toplamını verir
result=df.groupby("Departman").groups #hangilerinin grup olduğunu gösterir

#semtler=df.groupby("Semt")
#for name, group in semtler:
#    print(name)
#    print(group)                #semtlere göre for ile grupladı


#departmanlar=df.groupby("Departman")
#for name, group in departmanlar:
#   print(name)
#   print(group)  

result=df.groupby("Semt").get_group("Kadıköy") #sadece kadıköyde oturanlar




print(result)

