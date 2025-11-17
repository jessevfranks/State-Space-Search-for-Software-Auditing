import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML templates for responses
login_page = '''
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
'''

welcome_page = "<h1>Welcome, admin!</h1>"
invalid_page = "<h1>Invalid username or password.</h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template_string(login_page)

    username = request.form.get('username')
    password = request.form.get('password')
    conn = None

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}")

        cursor.execute(query)
        result = cursor.fetchone()

        # found a user
        if result:
            return render_template_string(welcome_page), 200

        # did not find a user, but successful query
        else:
            return render_template_string(invalid_page), 200

    except sqlite3.OperationalError as e:
        error_message = f"Internal Server Error: SQL syntax error: {e}"
        return error_message, 500

    finally:
        if conn:
            conn.close()