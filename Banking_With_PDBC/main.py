from decimal import Decimal
print("SELECT FEATURES FROM BELOW")
print("1. Register")
print("2. Login")
print("3. Exit")
print()

o = int(input("Choose one Feature from above :"))

if o == 1:
    from register import Register
    name = input("Enter Your Name :")
    acc_no = input("Enter Your Account Number :")
    balance = Decimal(input("Enter Your Balance :"))
    pin_number = input("Enter Your Password :")
    conf_pin_no = input("Enter Your Conform Password :")
    Register(name,acc_no,balance,pin_number,conf_pin_no)

elif o == 2:
    from login import Login
    acc_number = input("Enter the account number :")
    pin_number = input("Enter your PIN Number :")
    Login(acc_number,pin_number)

elif o == 3:
    print("Thank you for using Banking System")
    exit()

else:
    print("Invalid choice")


