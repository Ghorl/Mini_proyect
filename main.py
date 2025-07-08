from Admin import Menu_Admin
from User import Menu_User
import pandas as pd

class Login:
  
  def __init__(self):
    self.data=pd.read_excel('usuarios.xlsx',header=0)
    self.user_admin="adrian"
    self.password_admin="capi123"

  def LoginAdmin(self):
      admin=input("Admin: ")
      password=input("password: ")
      if admin!=self.user_admin or password!=self.password_admin:
         print("User or password incorrect")
         return
      else:
         print("\nWelcome admin")
         Menu_Admin()
         #Pondre una funcion que lo llevara al menu del admin
         
  def LoginUser(self):
      user=input("Username: ")
      password=input("Password: ")
      if not user in self.data['Username'].values or not password in self.data['Password'].values:
         print("Username or password incorrect")
         return
      else:
         print("\nWelcome User")
         Menu_User()
  
def MenuLogin():
    login=Login()
    while True:
      print("\nWelcome ADMIN/USER")
      print("1. Login ADMIN")
      print("2. Login User")
      print("3. Exit")
      try:
        op=int(input("Choose an option: "))
        match op:
            case 1:
                login.LoginAdmin()
            case 2:
                login.LoginUser()
            case 3:
                print("Leaving the program..")
                break
      except ValueError:
        print("Please, introduce a valid number.\n")

MenuLogin()