class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.name = ""
        
        #self.welcome()
        self.menu()


    def menu(self):
        user_input = input("""
        What you want to do?
        1. Enter 1 To Create Pin
        2. Enter 2 To Deposit
        3. Enter 3 To Withdraw
        4. Enter 4 To Check Balance
        5. Enter 5 To Withdraw
""")

        if user_input == "1":
            self.create_pin()

        elif user_input == "2":
            self.deposit()

        elif user_input == "3":
            self.withdraw()
    
        elif user_input == "4":
            self.check_balance()

        elif user_input == "5":
            self.exit()

        else:
            print("Enter Value From 1 to 5")
            self.menu()


    def create_pin(self):
        self.name = str(input("Enter Your Name:"))
        self.account = int(input("Enter Your Bank Account Number:"))
        self.pin = int(input("Create Your Pin:"))
        temp1 = int(input("Re-write Your Pin:"))

        if self.pin == temp1:
            #temp = self.pin
            print("Congratultions, Pin Created Successfully!!!")

        else:
            print("Both Pin Should be Match!!")

    def deposit(self):
        temp = int(input("Enter Your Pin:"))
        if temp == self.pin:
            amount = int(input("Enter Your Deposit Amount:"))
            self.balance+=amount
            print(amount, "Have Been Added to Your Account")

        else:
            print("Invalid Pin!!!")


    def withdraw(self):
        temp = int(input("Enter Your Pin:"))
        if temp == self.pin:
            bal = int(input("Enter Your Amount:"))
            print(bal, "Have Been Withdrawn Successfully!!!")
            if self.balance<bal:
                print("Insufficient Balance")

            else:
                self.balance-=bal

        else:
            print("Invalid Pin!!!")


    def check_balance(self):
        temp = int(input("Enter Your Pin:"))
        if temp == self.pin:
            print("Hi", self.name, "Your Available Balance is:", self.balance)

        else:
            print("Invalid Pin!!!")

    def exit(self):
        print("Bye", self.name, "See You Soon")
        
        
        
        

    
            

        
