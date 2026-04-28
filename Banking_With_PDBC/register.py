class Register:
    def __init__(self,n,ac_no,bal,pin_no,conf_pin_no):
        from db_connection import cursor
        queryCreatingTable = """
        create table if not exists users(
        customer_id int primary key auto_increment,
        name varchar(50) not null unique,
        acc_number varchar(16) not null unique,
        balance decimal(10,2) not null,
        pin_number varchar(4) not null
        )
        """

        cursor.execute(queryCreatingTable)
        print("Table Created Successfully...")

        if pin_no == conf_pin_no:
            queryInsertValues = "insert into users(name, acc_number, balance, pin_number) values(%s,%s,%s,%s)"
            data = (n,ac_no,bal,pin_no)
            cursor.execute(queryInsertValues,data)
            from db_connection import db_con
            db_con.commit()
            print("User Registered successfully...")

            if True:
                from login import Login
                ac_no = input("Enter the account number :")
                pin_no = input("Enter your PIN Number :")
                Login(ac_no,pin_no)
        else:
            print("PIN Number does not match with Conform Pin")





