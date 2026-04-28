from decimal import Decimal
class Dashboard:
        
    def __init__(self,i):
        print(f"WELCOME TO DASHBOARD {i[1]}")
        print()

        print("Select below options for Services")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        print()

        o = int(input("Choose our services :"))



        if o == 1:
            def checkbalance(pin_check_balance):  #Checking  Balance 
                if pin_check_balance == i[len(i)-1]:
                    print(i[len(i)-4],"Your Balance =",i[len(i)-2])
                else:
                    print("Pin Number does not match")
            checkbalance(input("Enter Pin number to check Balance :"))


        elif o == 2:
            def deposit(pin_number,dep_Amount):  #depositing Balance 
                nonlocal i
                if pin_number == i[len(i)-1]:
                    dep_Amount = Decimal(dep_Amount)
                    if dep_Amount > 0:
                        i = list(i)
                        i[len(i)-2] += dep_Amount
                        queryUpdateTable = "Update users set balance = %s where acc_number = %s and pin_number = %s"
                        data = ( i[len(i)-2],i[2],i[len(i)-1])
                        from db_connection import cursor,db_con
                        print(cursor.fetchone())
                        cursor.execute(queryUpdateTable,data)
                        db_con.commit()
                        print("Deposit Amount Successfully from",i[len(i)-4])
                        print(f"{i[len(i)-4]} Your amount After Deposit = {i[len(i)-2]}")
            deposit(input("Enter the Pin Number To Deposit:"),Decimal(input("Enter the Amount To Deposit :")))
        
        elif o == 3:    
            def withdraw(pin_number,Withdraw_Amount):  #withdrawing Balance 
                nonlocal i
                if pin_number == i[len(i)-1]:
                    Withdraw_Amount=Decimal(Withdraw_Amount)
                    if Withdraw_Amount > 0:
                        i = list(i)
                        i[len(i)-2] -= Withdraw_Amount
                        queryUpdateTable = "Update users set balance = %s where acc_number = %s and pin_number = %s"
                        data = ( i[len(i)-2],i[2],i[len(i)-1])
                        from db_connection import cursor,db_con
                        print(cursor.fetchall())
                        cursor.execute(queryUpdateTable,data)
                        db_con.commit()
                        print(" Withdraw amount Successfully from ",i[len(i)-4])
                        print(f"{i[len(i)-4]} Your amount After Withdraw = {i[len(i)-2]}")

                    else:
                        print("Enter a valid Amount")
                else:
                    print("Invalid Pin Number")
                        

            withdraw(input("Enter the Pin Number To Deposit:"),Decimal(input("Enter the Amount To Withdraw :")))

        elif o == 4:
            def logout():  #logout  
                 print("Logged out successfully")
            logout()
            exit()
        



