🏦 Just A Minute Bank – OOPs Based Banking System with API Integration
📌 Overview

This project is a Banking System simulation built using Python (OOPs) for the client-side and a Node.js + Express backend with MySQL for persistent storage.

It demonstrates core Object-Oriented Programming (OOPs) concepts while also showing how to integrate Python applications with REST APIs.

🚀 Features

✔️ User-friendly menu-driven Python interface
✔️ Secure account creation with password authentication
✔️ Backend server built with Node.js & Express
✔️ Database-backed using MySQL
✔️ Multiple account types: SavingsAccount & CurrentAccount
✔️ API communication using requests library in Python
✔️ Demonstrates all pillars of OOPs + real-world API integration

🧑‍💻 OOPs Concepts Covered
🔹 1. Class & Objects

Account, SavingsAccount, CurrentAccount classes

Objects represent individual user accounts

🔹 2. Encapsulation

Balance (__bal) is private, accessed only via methods

🔹 3. Inheritance

SavingsAccount and CurrentAccount inherit from Account

🔹 4. Polymorphism

Method overriding in withdraw() for SavingsAccount

🔹 5. Abstraction

Internal DB queries are hidden in the backend API

Python client interacts only via API calls (deposit(), withdraw(), etc.)

🔹 6. Class & Static Methods

noOfAccounts() → Class method

bankPolicy() → Static method (no object needed)

📂 Project Structure
bank_app/
│── account.py        # OOP classes (Account, SavingsAccount, CurrentAccount)
│── main.py           # Python client (menu-driven + API calls)
│── server.js         # Node.js + Express backend (REST APIs)
│── db.js             # MySQL connection setup for Node.js

⚙️ Setup & Installation
🔧 Prerequisites

Python 3.x

Node.js & npm

MySQL installed & running

📦 Python Dependencies
pip install requests

📦 Node.js Dependencies
npm install express mysql2 body-parser cors

🗄️ Database Setup

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

🌐 API Endpoints (Node.js Server)
Method	Endpoint	Description
POST	/createuser	Create a new user account
POST	/getuser	Fetch user details by username
PUT	/deposit	Deposit money into account
PUT	/withdraw	Withdraw money from account
▶️ Running the Application
Start Backend Server
node server.js


Server runs on http://localhost:3000

Run Python Client
python main.py

🎯 Example Flow

Start Node.js server (server.js)

Run Python program (main.py)

Choose option:

1 → Login if you already have an account

2 → Create a new account

3 → Exit

Perform actions (via API calls):

Check Balance

Deposit Money

Withdraw Money

📘 Learning Outcomes

How OOPs concepts apply in real-world applications

How to modularize Python code into multiple files

How to connect Node.js with MySQL

How to consume REST APIs from Python using requests

How client-server systems work in practice

🌟 Future Enhancements

🔹 Add transaction history per account
🔹 Implement password hashing for better security
🔹 Add GUI (Tkinter / Flask frontend)
🔹 JWT authentication for secure login
🔹 Support multiple currencies

👨‍💻 Author

Babulu Digamarti
🎓 AI & Data Science Student
💻 Full Stack Developer
🔍 Exploring OOPs, Databases & API systems

✨ This project is not just a banking system – it’s a full-stack OOPs showcase with real-world API integration
