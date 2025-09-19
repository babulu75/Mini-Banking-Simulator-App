from account import Account
from db import get_connection
conn,cursor=get_connection()
print("Database connection Successful..." if cursor else "Database connection Failed....")

print("........Welcome Just A Minute Bank Services........")
while True:
    user_type=int(input("choose one option \n1.Aleardy have an account \t 2.Create a New Account\n Select 1 or 2 or 3 for exit :"))
    if user_type==1:
        print("Enter your Details")
        username=input("Enter your Username :")
        password=input("Enter your password :")
        cursor.execute("SELECT * FROM USERS WHERE name = %s", (username,))
        row = cursor.fetchone()
        if row:
            if row[4]==password:
                obj=Account(row[1],row[3])
                print("****************************")
                print(f"______Welcome {row[1]}______")
                func=int(input("1.Check Balance \n2.Withdraw Money \n3.Deposit Money"))
                if func==1:
                    obj.showBalance()
                elif func==2:
                    withdraw_amount=int(input("Enter withdraw amount : "))
                    obj.withdraw(withdraw_amount)
                elif func==3:
                    deposit_amount=int(input("Enter deposit amount : "))
                    obj.deposit(deposit_amount)
                else:
                    print("Enter correct value")
            else:
                print("Invalid Password")
        else:
            print("User not found")
    elif user_type==3:
        break
    else:
        Account.bankPolicy()
        username=input("Enter your Name : ")
        phone_number=input("Enter your Phone Number : ")
        amount=int(input("Enter amount you greater than 1000 in your new account : "))
        password=input("Create Password : ")
        obj=Account(username,amount)
        query="INSERT INTO USERS (NAME,PHONE_NUMBER,AMOUNT,PASSWORD) VALUES (%s, %s, %s, %s)"
        val=(username,phone_number,amount,password)
        try:
            cursor.execute(query,val)
            conn.commit()
            print(f"Account creation successful {username} with account balance{amount}")
        except Exception as e:
            print("Account creation failed",e)