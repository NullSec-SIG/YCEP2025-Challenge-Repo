from flask import Flask, request, render_template_string
import mysql.connector
from mysql.connector import errorcode
import time

app = Flask(__name__)

# Database configuration
db_config = {
    'user': '[REDACTED]',
    'password': '[REDACTED]',
    'host': 'db',
    'database': 'mydatabase'
}

# Initialize the database connection
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Create users table and insert a dummy user
def init_db():
    retries = 5
    while retries > 0:
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)
            print("Table created successfully or already exists.")
            cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '[REDACTED]') ON DUPLICATE KEY UPDATE username=username")
            connection.commit()
            print("Dummy user inserted or already exists.")
            cursor.close()
            connection.close()
            break
        except mysql.connector.Error as err:
            print(f"Error: {err.msg}")
            retries -= 1
            time.sleep(3)
        except Exception as e:
            print(f"Unexpected error: {e}")
            retries -= 1
            time.sleep(3)

# Login page template
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            margin: 0;
        }
        .login-container {
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            box-sizing: border-box;
        }
        .login-container h1 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #333;
            text-align: center;
        }
        .login-container input {
            display: block;
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 16px;
        }
        .login-container button {
            width: 100%;
            padding: 10px;
            background-color: #5cb85c;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .login-container button:hover {
            background-color: #4cae4c;
        }
        .error {
            color: red;
            margin-top: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <form method="POST" action="/">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="text" name="auth" placeholder="Auth" required>
            <button type="submit">Login</button>
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

banned_keywords = [
    'INSERT', 'UPDATE', 'DELETE', 'MERGE',
    'CREATE', 'ALTER', 'DROP', 'TRUNCATE', 'RENAME',
    'COMMIT', 'ROLLBACK', 'SAVEPOINT',
    'GRANT', 'REVOKE', 'DENY', 'BACKUP', 'RESTORE', 'SHUTDOWN', 'EXEC',
    'BEGIN', 'END', 'LOCK', 'SET',
    'xp_cmdshell', 'sp_configure', 'sp_executesql', 
    'sp_addextendedproc', 'sp_addsrvrolemember', 'sp_droprolemember'
]

# SQL Injection vulnerable login
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        auth = request.form['auth']

        if auth != "T0pS3cr3tP@ssw0rd":
            error = "Invalid auth value"
            return render_template_string(login_page, error=error)
        
        # Vulnerable SQL query
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        if any(keyword in query.upper() for keyword in banned_keywords):
            error = "Banned keywords used."
            return render_template_string(login_page, error=error)
        
        print(f"Executing query: {query}")
        
        # Execute the query
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            if result:
                return "Login successful! Flag: YCEP24{[REDACTED]}"
            else:
                error = "Invalid credentials"

        except mysql.connector.Error as err:
            print(f"Error: {err.msg}")
            error = f"Database error: {err.msg}"
            
    return render_template_string(login_page, error=error)

init_db()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)