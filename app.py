from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import mysql.connector

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="personal_finance_tracker"
)
cursor = db.cursor()

# User Registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    hashed_password = generate_password_hash(password, method='sha256')

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'User registered successfully!'}), 201


# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401

    token = create_access_token(identity=username)
    return jsonify({'access_token': token}), 200

# Add Transaction
@app.route('/add-transaction', methods=['POST'])
@jwt_required()
def add_transaction():
    data = request.get_json()
    username = request.jwt_identity
    amount = data.get('amount')
    category = data.get('category')
    date = data.get('date')

    if not amount or not category or not date:
        return jsonify({'error': 'Amount, category, and date are required'}), 400

    cursor.execute("INSERT INTO transactions (username, amount, category, date) VALUES (%s, %s, %s, %s)",
                   (username, amount, category, date))
    db.commit()
    return jsonify({'message': 'Transaction added successfully'}), 201

# Get Transactions
@app.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    username = request.jwt_identity

    cursor.execute("SELECT amount, category, date FROM transactions WHERE username = %s", (username,))
    transactions = cursor.fetchall()

    return jsonify({'transactions': transactions}), 200

# Get Financial Summary
@app.route('/summary', methods=['GET'])
@jwt_required()
def get_summary():
    username = request.jwt_identity

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE username = %s", (username,))
    total_spent = cursor.fetchone()[0] or 0

    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE username = %s GROUP BY category", (username,))
    category_summary = cursor.fetchall()

    summary = {
        'total_spent': total_spent,
        'category_summary': {category: amount for category, amount in category_summary}
    }
    return jsonify(summary), 200

if __name__ == '__main__':
    app.run(debug=True)
