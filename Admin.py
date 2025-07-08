class Admin:
    def __init__(self):
       self.user_list=[]
       self.password_list=[]

    def Register_User(self):
       name_user=input("Name of user: ")
       password_user=input("Password of user: ")
       print("User successfully registered!!\n")

       self.user_list.append(name_user)
       self.password_list.append(password_user)


    
    def Excel_User(self):
        pass


def Menu_Admin():
    admin=Admin()
    while True:
        print("1.Register an user")
        print("2.Export excel of users list")
        print("3.Exit")
        try:
           op=int(input("Select an option: "))
           match op:
                case 1:
                    admin.Register_User()
                case 2:
                    admin.Excel_User()
                case 3:
                    print("Exiting the menu..")
                    break
        except ValueError:
            print("Please, introduce a valid number.\n")
