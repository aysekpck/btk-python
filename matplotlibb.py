import matplotlib.pyplot as plt
import numpy as np
"""
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,color="red")
plt.axis([0,6,0,20]) #xin değeri 6ya kadar ynin feğeri 20ye

plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
"""
"""
x=np.linspace(0,2,100)
plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")
plt.xlabel("x label")
plt.ylabel("y label")

plt.legend()
"""

#3 ayrı tabloda gösterim
"""
x=np.linspace(0,2,100)
fig,axs= plt.subplots(3)

axs[0].plot(x,x,color="red")
axs[0].set_title("1linear")

axs[1].plot(x,x**2,color="green")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("qubic")

plt.tight_layout()#başlıklar birbirine geçmemesi içib
"""
"""
x=np.linspace(0,2,100)
fig,axs= plt.subplots(2,2)
fig.suptitle("gradik Başlığı")

axs[0,0].plot(x,x**2,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**2,color="green")
axs[1,1].plot(x,x**4,color="yellow")
"""


plt.show()
