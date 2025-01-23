MoneyMentor - Personal Finance Tracker
MoneyMentor is a web application designed to help users manage their personal finances. It allows users to track their income, expenses, and financial transactions efficiently. The application also provides a dashboard for users to visualize their financial data, such as balance, transaction history, and more.

This project is built using Angular for the frontend, Python (Flask) for the backend API, and MySQL for the database.

Table of Contents
Features
Technologies Used
Installation Instructions
Usage
API Documentation
Database Setup
Folder Structure
Contributing
License
Features
User Authentication: Secure login and registration.
Dashboard: View the balance, income, and expense details.
Transaction Management: Add, view, and delete transactions (expenses and incomes).
User Profile: Customize the profile with basic information.
Responsive Design: The application is fully responsive for both desktop and mobile devices.
Technologies Used
Frontend:

Angular
HTML5, CSS3, JavaScript
Bootstrap for UI components
NgRx for state management (optional)
Backend:

Python (Flask)
Flask-RESTful for building API
MySQL Database for storing user and transaction data
Others:

MySQL Workbench for managing the database
Postman for API testing (optional)
Installation Instructions
Prerequisites
Before you begin, ensure you have the following installed:

Node.js and npm (for Angular frontend)
Python (for backend Flask API)
MySQL (for database)
Git (to clone the repository)
1. Clone the Repository
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/your-username/MoneyMentor.git
cd MoneyMentor
2. Setup Frontend (Angular)
Navigate to the Angular folder:

bash
Copy
Edit
cd frontend
Install the dependencies:

bash
Copy
Edit
npm install
Start the Angular development server:

bash
Copy
Edit
ng serve
Your Angular app should now be running on http://localhost:4200.

3. Setup Backend (Python Flask)
Navigate to the backend folder:

bash
Copy
Edit
cd backend
Create a virtual environment:

bash
Copy
Edit
python3 -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy
Edit
venv\Scripts\activate
On Linux/macOS:
bash
Copy
Edit
source venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Start the Flask backend server:

bash
Copy
Edit
python app.py
The Flask app should now be running on http://localhost:5000.

4. Database Setup
Create a MySQL database for the project:
Login to MySQL:
bash
Copy
Edit
mysql -u root -p
Create a database:
sql
Copy
Edit
CREATE DATABASE moneymentor;
Import the schema from the provided db.sql file:
bash
Copy
Edit
source db.sql
Usage
User Registration: Go to /register and create a new account by providing your email, username, and password.
Login: After registration, you can log in with your credentials at /login.
Dashboard: Once logged in, the dashboard will display your financial summary.
Add Transaction: Add new financial transactions (expenses or income) from the /add-transaction page.
View Transactions: View your transaction history on the /view-transactions page.
API Documentation
Base URL
All the endpoints can be accessed at http://localhost:5000/api.

Endpoints
POST /register

Register a new user.
Request body:
json
Copy
Edit
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123"
}
POST /login

Login with the registered credentials.
Request body:
json
Copy
Edit
{
  "username": "john_doe",
  "password": "password123"
}
GET /dashboard

Fetch user dashboard data (balance, total expenses, total income).
POST /add-transaction

Add a new financial transaction.
Request body:
json
Copy
Edit
{
  "amount": 100,
  "type": "expense",
  "description": "Groceries",
  "date": "2025-01-23"
}
GET /view-transactions

View all transactions for the logged-in user.
DELETE /delete-transaction/:id

Delete a transaction by ID.
Folder Structure
csharp
Copy
Edit
MoneyMentor/
│
├── backend/
│   ├── app.py           # Flask API server
│   ├── db.sql           # Database schema
│   ├── requirements.txt # Python dependencies
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   │   ├── login/
│   │   │   │   ├── register/
│   │   │   │   ├── dashboard/
│   │   │   │   ├── add-transaction/
│   │   │   │   └── view-transactions/
│   │   │   ├── services/
│   │   │   │   └── api.service.ts
│   │   │   ├── app.component.ts
│   │   │   └── app.module.ts
│   └── package.json
│
├── README.md            # Project documentation
└── ...
Contributing
Feel free to contribute to this project by forking the repository, making your changes, and submitting a pull request. Here are some ways you can contribute:

Fix bugs or issues.
Improve documentation.
Add new features or enhancements.
License
This project is licensed under the MIT License.
