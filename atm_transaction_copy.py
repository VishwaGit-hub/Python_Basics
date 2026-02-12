class Atm:
    def __init__(self,uname,password,amount):
        self.uname=uname
        self.__password=password
        if amount<=500:
            print()
            print("="*20)
            print("Minimum amount 500 is required!")
            print("*"*20)
        else:
            self.amount=amount
            print()
            print("="*20)
            print("Account Created!")
            print("*"*20)
    
    def get_info(self):
        print()
        print("="*20)
        print("User: ",self.uname)
        print("Password: ","*"*int(len(str(self.__password))))
        print("Amount: ",self.amount)
        print("="*20)
    
    def withdraw(self,amount):
        if amount<=self.amount:
            if (self.amount - amount)<500:
                print()
                print("="*20)
                print("You Must Maintain 500 rupees in amount")
                print("="*20)
            else:
                self.amount-=amount
                print()
                print("="*20)
                print(f'Amount {amount} withdrawed Remaining Amount {self.amount}!')
                print("="*20)
        else:
            print("Insufficient Balance!")
    
    def deposit(self,amount):
        if amount<=0:
            print()
            print("="*20)
            print("Invalid amount!")
            print("="*20)
        else:
            self.amount+=amount
            print()
            print("="*20)
            print(f'Amount {amount} deposited New Amount {self.amount}!')
            print("="*20)

while True:
    print()
    print("Welcome to ATM!")
    print("======================")
    print("1.Create Account")
    print("2.Check Balance")
    print("3.Withdraw Money")
    print("4.Deposit Money")
    print("5.Exit")
    print()
    
    try:
        ch=int(input("Enter your choice..."))
        if ch<0 or ch>5:
            print("Please choose between given option!!!") 
    except ValueError:
        print("Invalid Choice")
       
    match ch:
        case 1:
            try:
                uname=input("Enter username...")
                password=int(input("Enter password..."))
                ini_amt=float(input("Enter initial amount..."))
                
            except ValueError:
                print("Invalid input,try again!!")
            a1=Atm(uname,password,ini_amt)
                
        case 2:
            a1.get_info()
        case 3:
            try:
                with_amt=float(input('Enter withdraw amount...'))
            except ValueError:
                print("Invalid Amount!!")
            a1.withdraw(with_amt)
        case 4:
            try:
                depo_amt=float(input("Enter deposit amount..."))
            except ValueError:
                print("Invalid Amount!!")
            a1.deposit(depo_amt)
        case 5:
            print("THANK YOU FOR VISITING!!!")
            break
    
    
    
    
        