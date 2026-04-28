# Smart Banking System (Python + MySQL + OOP)

This project is a database-driven banking application that simulates real-world banking operations. It is built using Python with MySQL integration and follows a modular OOP-based architecture.

The system includes:

A registration module to create new users
A login system that validates credentials from the database
A dashboard for performing banking operations like deposit, withdrawal, and balance checking

The project emphasizes database interaction, transaction management, and clean code structure, making it a solid foundation for backend development.



A production-inspired, modular banking system built using Python and MySQL, designed to simulate real-world banking operations with clean architecture and database integration.

🚀 Live Highlights
🔐 Secure Authentication System
💰 Real-time Balance Management
🧱 Modular OOP Architecture
🗄️ Persistent Data Storage (MySQL)
⚡ Optimized Queries (No full-table scans)


Demo (Console Preview)
WELCOME TO SMART BANKING SYSTEM

1. Register
2. Login
3. Exit

> Login Successful

--- Dashboard ---
1. Check Balance
2. Deposit
3. Withdraw
4. Logout


Problem Statement

Traditional beginner projects lack real database handling, modular structure, and scalability.

This project solves that by:

Integrating Python with MySQL (PDBC)
Using structured OOP design
Implementing real banking workflows



Architecture :

main.py 
    ↓ 
Authentication Layer (login.py / register.py) 
    ↓ 
Business Logic (dashboard.py) 
    ↓
Database Layer (db_connection.py)


🛠️ Tech Stack
Layer          	Technology
Language	       Python
Database	       MySQL
Connector        mysql-connector-python
Architecture	   OOP (Object-Oriented Programming)



Key Features:

🔐 Authentication

User Registration with validation
Secure Login using DB verification
Optimized query using WHERE clause

💰 Banking Operations
Check Balance
Deposit Money (Decimal precision)
Withdraw Money (with validation)
Logout system

🗄️ Database Integration
Persistent storage using MySQL
ACID-compliant transactions (commit)
Structured schema design


📂 Project Structure
Banking-System/
│── main.py
│── register.py
│── login.py
│── dashboard.py
│── db_connection.py
│── README.md


⚡ Getting Started
1️⃣ Clone Repo
git clone https://github.com/ThirumalJeegari/PDBC_Project_With_OOPS.git
cd PDBC_Project_With_OOPS

2️⃣ Install Dependencies
pip install mysql-connector-python

3️⃣ Setup Database
CREATE DATABASE BankingProject;

4️⃣ Configure DB

Update in db_connection.py:

host="localhost"
user="root"
password="your_password"
database="BankingProject"

5️⃣ Run Project
python main.py


📊 Key Learnings:

Database connectivity using Python (PDBC)
Writing optimized SQL queries
Handling transactions (commit)
Structuring applications using OOP
Managing real-world data flow

⚠️ Current Limitations:
PIN stored in plain text (no hashing)
No transaction history
No UI (console-based)
No concurrency handling

🚀 Future Enhancements (Roadmap):
🔥 Phase 2 (Intermediate)
Password hashing (bcrypt)
Transaction history table
Input validation layer
Exception handling

🚀 Phase 3 (Advanced)
REST API using Flask / FastAPI
Frontend (React / HTML-CSS)
JWT Authentication
Docker deployment

🧑‍💻 Author
Jeegari Thirumal
💼 Aspiring Software Engineer
🔗 GitHub: https://github.com/ThirumalJeegari
🔗 LinkedIn: https://linkedin.com/in/thirumaljeegari

⭐ Portfolio Value
This project demonstrates:

End-to-end backend development
Database-driven application design
Clean code practices
Real-world problem modeling

🤝 Contributions
Pull requests are welcome. For major changes, please open an issue first.

📜 License
This project is open-source and available under the MIT License.
