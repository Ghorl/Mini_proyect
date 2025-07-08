from Admin import Menu_Admin

class Login:
  
  def __init__(self):
    self.user_admin="adrian"
    self.password_admin="capi123"
  def LoginAdmin(self):
      admin=input("Admin: ")
      password=input("password: ")
      if admin!=self.user_admin or password!=self.password_admin:
         print("User or password incorrect")
      else:
         print("\nWelcome admin")
         Menu_Admin()
         #Pondre una funcion que lo llevara al menu del admin
         
  def LoginUser(self):
     pass
  
  
def MenuLogin():
    login=Login()
    while True:
      print("\nWelcome ADMIN/USER")
      print("1. Login ADMIN")
      print("2. Login User")
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




