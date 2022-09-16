"""mylist=[1,2,3]
mystring= "my string"
print(len(mylist))
print(len(mystring))
print(type(mystring))
print(type(mylist))"""

class Movie():
     def __init__(self,title,director,duration):
          self.title=title
          self.director=director
          self.duration=duration 
          print("movie objesi oluşturuldu")
     def __str__(self):
          return f"{self.title} by {self.director}"
     def __len__(self):
          return self.duration
     def __del__(self):
          print("film objesi silindi")
m=Movie("film adı","yönetmen",120)

print(m)#<__main__.Movie object at 0x0000026AEAE320A0>
print (len(m))


del m #NameError: name 'm' is not defined

print(m)
