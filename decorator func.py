#DECORATORS FONKSİYON:bir fonksiyona özellik eklemek için kullanılır
#bir özelliği bir kaç yerde kullanmayı sağlar
#daha az kod kullanmayı sağlar
"""
def my_decorator(func):
     def wrapper(name): #parametre alabilmek için wrapper ve func a ekleme yapılır
          print("fonkdan önce işlemler")
          func(name)
          print("fonkdan osnraki işlemler")
     return wrapper

@my_decorator
def sayhello(name):
     print("hello",name)

sayhello("ali")
"""


import math
import time

def calculate_time(func):
     def inner(*args,**kwargs):
          start=time.time()
          time.sleep(1)     
          func(*args,**kwargs)
          finish=time.time()
          print("fonksiyon" + func.__name__ + str(finish-start) +"saniye sürdü")
     return inner

@calculate_time
def usalma(a,b):
     print(math.pow(a,b))
     
@calculate_time    
def faktoriyel(num):
     print(math.factorial(num))

usalma(2,3)     
faktoriyel(4)










