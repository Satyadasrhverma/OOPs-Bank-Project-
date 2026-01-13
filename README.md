# OOPs-Bank-Project-
A console-based ATM Banking System built in Python using Object-Oriented Programming principles.
📌 Project Overview

This project demonstrates:

Real-world use of OOP principles

Clean separation of logic using multiple Python modules

State management using class attributes

A looping ATM menu for continuous user interaction

It is beginner-friendly yet structured enough to show good coding practices.

⚙️ Features

Create a bank account with account number and opening balance

Debit money with balance validation

Credit money with amount validation

Check current balance

View full transaction history

Continuous ATM menu until user exits

🧠 OOP Concepts Used

Class & Object

Encapsulation

Constructor (__init__)

Instance variables

Method-based design

Modular programming

📂 Project Structure
OOPS-Banking-System/
│
├── bank.py        # Bank class (core business logic)
├── atm.py         # ATM operations & menu handling
├── main.py        # Program entry point
└── README.md      # Project documentation

🧾 File Description
bank.py

Contains the Bank class which handles:

Account number

Balance

Transaction list

Debit & credit logic

Balance and transaction retrieval

atm.py

Handles:

User input

ATM menu

Calls bank class methods

Continuous operation loop

main.py

Entry point of the application

Starts the ATM system

▶️ How to Run the Project
Step 1: Clone the Repository
git clone https://github.com/your-username/OOPS-Banking-System.git

Step 2: Navigate to Project Folder
cd OOPS-Banking-System

Step 3: Run the Program
python main.py

🖥️ Sample Output
Enter Account Number: 101
Enter Starting Balance: 5000

--- ATM MENU ---
1. Debit
2. Credit
3. Check Balance
4. Transaction History
5. Exit

🚫 Validations Implemented

Cannot debit more than available balance

Cannot credit or debit zero / negative amounts

Handles invalid menu choices safely

🚀 Future Enhancements (Optional)

Flask web interface

Database integration (SQLite/MySQL)

User authentication (PIN-based login)

Multiple accounts support

File-based transaction storage

REST API version using FastAPI

🎯 Who This Project Is For

Python beginners learning OOP

Students preparing for interviews

Anyone wanting a real mini-project for GitHub

OOP practice with practical logic

🧑‍💻 Author

Vivaan
Python | OOP | Backend Enthusiast

📜 License

This project is open-source and free to use for learning purposes.
