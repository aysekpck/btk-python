import json
import os
class User:
     def __init__(self,username,password,email):
          self.username = username
          self.password = password
          self.email = email
class UserRepository:
     def __init__(self):
          self.users = []
          self.isLoggedIn = False
          self.currentUser = {}         
          #self.loadUsers()
          
     def loudUsers(self):
          if os.path.exists("user.json"):
               with open("users.json","r",encoding="utf-8") as file:
                   users=json.load(file)
                   for user in users:
                        user=json.loads(user)
                        newUser =User(username=user["username"], password=user["password"], email=user["email"])
                        self.users.append(newUser)
               print(self.users)                       
            
     def register(self,user:User):
          self.users.append(user)
          self.savetoFile()
          print("kulanıcı oluşturuldu")
          
     def login(self,username,password):
          for user in self.users:
               if user.username == username and user.password==password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("login yapıldı.")
                    break
     def logout(self):
          self.isLoggedIn= False
          self.currentUser={}
          print("çıkış yapıldı")
     def identity(self):
          if self.isLoggedIn:
               print(f'username: {self.currentUser.username}')
          else:
               print("giriş yapılmadı.")
               

     def savetoFile(self):
          list= []
     
  


          
     with open("users.json","w") as file:
          json.dump(list,file)
               
               
     
repository=UserRepository()

while True:
     print("Menü".center(50,"*"))
     secim=input("1-Register\n2- Login\n3- logout\n4- İdentity\n5- Exit\nseçiminiz: ")
     if secim == "5":
          break
     else:
          if secim == "1":
               username = input("username:")
               password = input("password:")
               email = input("email:")

               user=User(username=username,password=password, email=email)
               repository.register(user)
               print(repository.users)
          elif secim == "2":
               username=input("username")
               password=input("password")
               repository.login(username,password)
          elif secim == "3":
               pass #logout
          elif secim == "4":
               repository.identity()
          else:
               print("yanlış seçim")
     
