class Account:
    account_count=0
    def __init__(self,name,bal):
        self.name=name
        self.__bal=bal   #abstraction of balance
        Account.account_count+=1
    @classmethod #class method demonstration
    def noOfAccounts(cls):
        return cls.account_count
    
    @staticmethod #static method demonstration where no need of object can be directly called using class name
    def bankPolicy():
        print("🏦 Welcome to *Just A Minute Bank*! 🎉")
        print("👉 Here are our Terms & Policies for all new users:")
        print("1. Minimum balance must not fall below ₹1000.")
        print("2. Daily withdrawal limit is ₹25,000.")
        print("3. Free deposits allowed any number of times.")
        print("4. Interest is credited monthly for savings accounts.")
        print("5. Please keep your PIN secure and do not share with anyone.")
        print("6. Bank is not responsible for transactions done by sharing credentials.")
        print("✅ Thank you for choosing Just A Minute Bank!")

    def showBalance(self):
        print(f"{self.name} your account balance {self.__bal}")
    def withdraw(self,amount):
        if self.__bal<amount:
            print("Insuffcient Balance")
            return
        self.__bal-=amount
        try:
            cursor.execute("UPDATE USERS SET AMOUNT=%s WHERE NAME=%s",(self.__bal,self.name))
            print(f"Withdraw of {amount} is successful...😇")
            print(f"Remaining account balance is {self.__bal}")
        except Exception as e:
            print("Withdraw failed..",e)
    def deposit(self,amount):
        self.__bal+=amount
        try:
            cursor.execute("UPDATE USERS SET AMOUNT=%s WHERE NAME=%s",(self.__bal,self.name))
            print(f"Deposit of {amount} is successful...😇")
            print(f"Updated account balance is {self.__bal}")
        except Exception as e:
            print("Deposit failed..",e)
    def getBalance(self):
        return self.__bal
    
#use of inheritance concept this is multiple inheritance
class SavingsAccount(Account):
    def __init__(self,name,amount,interest):
        super().__init__(name,amount)
        self.interest=interest
    def withdraw(self,amount):   #here concept of method overiding is applied 
        print("Transaction is under process...")
        super().withdraw(amount)
    def deposit(self, amount):
        return super().deposit(amount)
class CurrentAccount(Account):
    def __init__(self,name,amount,interest):
        super().__init__(name,amount)
        self.interest=interest
    def withdraw(self, amount):
        return super().withdraw(amount)
    def deposit(self, amount):
        return super().deposit(amount)