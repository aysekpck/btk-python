import matplotlib.pyplot as plt


#stack plot
"""

yil=[2011,2012,2013,2014,2015]
oyuncu1=[8,10,12,7,9]
oyuncu2=[7,12,5,15,21]
oyuncu3=[18,20,22,25,19]

plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")


plt.stackplot(yil,oyuncu1,oyuncu3,oyuncu3, colors=["y","r","b"])
plt.legend()
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("Gol sayisi")

plt.show()
"""


#pie grafiği
"""
goal_types="Penaltı","kaleye atılan şut","serbest vuruş"
goals=[14,35,7]
plt.pie(goals,labels=goal_types,colors=["y","r","b"],shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")
plt.show()
"""

#bar grafiği
"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label= "BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label= "AUDI",width=.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")
 
plt.show()
"""

#hisyogram grafiği
"""
yaslar=[22,12,15,99,56,58,100,88,95,77,54,48,75,30,69,82,31,115,1,6,7,9,85]
yas_gruplari=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype='bar',rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("kişi sayısı")
plt.title("histogram grafiği")

plt.show()
"""