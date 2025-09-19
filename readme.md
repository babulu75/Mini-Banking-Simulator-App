🏦 Just A Minute Bank – OOPs Based Banking System
📌 Overview

This project is a Banking System simulation built in Python that demonstrates the core Object-Oriented Programming (OOPs) concepts.
It allows users to:

Create a new account

Login to an existing account

Deposit and withdraw money

Check account balance

The project also integrates with MySQL database to persist user details and account transactions.

🚀 Features

✔️ User-friendly menu-driven interface
✔️ Secure account creation with password authentication
✔️ Database-backed using MySQL
✔️ Multiple account types: SavingsAccount & CurrentAccount
✔️ Demonstrates all Pillars of OOPs

🧑‍💻 OOPs Concepts Covered
🔹 1. Class & Objects

Account, SavingsAccount, CurrentAccount classes

Objects represent individual user accounts

🔹 2. Encapsulation

Balance (__bal) is private, accessed via methods only

Hides sensitive account data from direct access

🔹 3. Inheritance

SavingsAccount and CurrentAccount inherit from Account

Reuse and extend functionality

🔹 4. Polymorphism

Method Overriding in withdraw() for SavingsAccount

Different behavior with the same method name

🔹 5. Abstraction

Internal DB queries hidden from users

Users interact only through simple methods like deposit(), withdraw()

🔹 6. Class & Static Methods

noOfAccounts() → Class method

bankPolicy() → Static method (no need for object creation)

📂 Project Structure
bank_app/
│── account.py   # All OOP classes (Account, SavingsAccount, CurrentAccount)
│── db.py        # Database connection setup (MySQL)
│── main.py      # Main program (menu & user interaction)

⚙️ Setup & Installation
🔧 Prerequisites

Python 3.x

MySQL installed & running

📦 Install Dependencies
pip install mysql-connector-python

🗄️ Create Database & Table

In MySQL, run:

CREATE DATABASE bank;
USE bank;

CREATE TABLE USERS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100),
    PHONE_NUMBER VARCHAR(15),
    AMOUNT INT,
    PASSWORD VARCHAR(50)
);

▶️ Run the Application
python main.py

🎯 Example Flow

Start the program

Choose option:

1 → Login if you already have an account

2 → Create a new account

3 → Exit

Perform actions:

Check Balance

Deposit Money

Withdraw Money

📘 Learning Outcomes

This project helps understand:

How OOPs concepts work in real-world applications

How to modularize Python code into multiple files

How to connect Python with MySQL

How to build a simple yet functional banking system

🌟 Future Enhancements

🔹 Add transaction history for each account
🔹 Implement password hashing for better security
🔹 Add GUI interface using Tkinter / Flask
🔹 Support for multiple currencies

👨‍💻 Author

Babulu Digamarti

🎓 AI & Data Science Student

💻 Full Stack Developer

🔍 Exploring OOPs & Database Systems

✨ This project is more than just a banking system – it’s a complete showcase of OOP concepts in Python with real-world implementation.