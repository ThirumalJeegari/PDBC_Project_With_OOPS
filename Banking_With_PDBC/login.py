class Login:
    def __init__(self,acc_no,pin_no):
        from db_connection import cursor
        queryfetchingTable = "select * from Users"
        cursor.execute(queryfetchingTable)
        data = cursor.fetchall()


        found = False
        for i in data:
            if i[2] == acc_no and i[4] == pin_no:
                print(f"Logined Succesfully..{i[1]}")
                print()
                from dashboard import Dashboard
                Dashboard(i)

                found = True
                break
        if not found:
            print("Invalid Credentials")
