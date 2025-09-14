
class bankAccount:
    def __init__(self,account_number,name,init_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance= init_balance
    def deposit(self,amount):
        if amount >0:
            self.balance = self.balance + amount
            print(f"{amount}deposited sucessfully")
        else:
            print("Deposit amount must be postive")
    def withdraw(self,amount):
        if 0< amount <= self.balance:
            self.balance = self.balance -amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficent funds or Invaild amount.")
    def displayBalance(self):
        print(f"Account Number: {self.account_number} | Name: {self.name} | Balance: {self.balance}")
class Bank:
    def __init__(self):
            self.account = {} # Dictonary to store accounts by account #
    def createAccount(self, account_number,name,init_balance):
            if account_number in self.account:
                print("Account Number already exists")
            else:
                self.account[account_number] = bankAccount(account_number,name,init_balance)
                print("Account created sucessfully")

    def getAccount(self, account_number):
            return self.account.get(account_number,None)
    def listAccounts(self):
            if not self.account:
                 print("No account found.")
            else:
                 print("\nList of all accounts:")
                 for acct in self.account.values():
                      acct.displayBalance()
    # the main program
        
def main():
    bank=Bank()

    while True:
        print("\n ===Bank Menu===")
        print("1.Create Account")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Check Balance")
        print("5. List All Accounts")
        print("6. Exit")

        choice= input("Choose Option 1 thru 6")
            

        if choice=="1":
              acct_num=input("Please account numbers")
              name=input("Please enter account holders name")

              try:
                init_balance= float((input("Enter Initial Deposit")))
                bank.createAccount(acct_num,name, init_balance)
              except ValueError:
                   print("Invalid Input:Balance must be numeric")
        elif choice == "2":
            acct_num = input("Please enter account number: ")
            account = bank.getAccount(acct_num)
            if account:
                 try:
                    amount = float(input("Enter amount to deposit:"))
                    account.deposit(amount)
                 except ValueError:
                      print("Amount must be numeric")

            else:
                 print("Account not found")
        elif choice =="3":
            acct_num= input("Please enter acount number")
            account= bank.getAccount(acct_num)
            if account:
                try:
                    amount = float(input("Enter Enter amount to withdraw:"))
                    account.withdraw(amount)
                except ValueError:
                     print("Amount must be numeric")
            else:
                 print("Hush! Account not found")

        elif choice == "4":
            acct_num = input("Please enter account number: ")
            account = bank.getAccount(acct_num)
            if account:
                account.display_balance()
            else:
                 print("Account not found.")
        elif choice == "5":
            bank.listAccounts()
        elif choice == "6":
            print("Thank you for Banking with US!")
            break
        else:
             print("Invalid choice. Please try again.")
if __name__ == "__main__":
     main()
     
                      

        

        