import pandas as pd
from numpy import *
import os
class Admin:
    def __init__(self):
       self.user_list=[]
       self.password_list=[]
       self.data={
            "Username":self.user_list,
            "Password":self.password_list,
        }

    def Register_User(self):
       name_user=input("Name of user: ")
       password_user=input("Password of user: ")
       print("User successfully registered!!\n")

       self.user_list.append(name_user)
       self.password_list.append(password_user)
    
    def Excel_User(self):
        if not self.user_list:
            print("No users to export\n")
            return
        
        archivo="usuarios.xlsx"
        new_data=pd.DataFrame({
            "Username":self.user_list,
            "Password":self.password_list
        })

        if os.path.exists(archivo):
            #Lee usuarios anteriores
            past_data=pd.read_excel(archivo)
            #Combina los datos viejos con los nuevos
            df=pd.concat([past_data,new_data],ignore_index=True)
        else:
            df=new_data
           
        df.to_excel(archivo,index=False)
        print("User list exported to 'usuarios.xlsx'!\n")
        self.user_list.clear()
        self.password_list.clear()

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