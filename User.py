class User:
    def __init__(self):
        pass
    
    def Add_Product(self):
        pass
    
    def Excel_Report(self):
        pass

    def Menu_User(self):
     
     while True:
        print("1.Add Product to inventory")
        print("2.Create report excel of inventory")
        print("3.Exit")
        try:
            op=int(input("Select an option: "))
            match op:
                case 1:
                    self.Add_Product()
                case 2:
                    self.Excel_Report()
                case 3:
                    print("Exiting the menu...")
                    break
        except ValueError:
            print("Please, introduce a valid number.\n")