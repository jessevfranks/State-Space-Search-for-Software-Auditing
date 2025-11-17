import sqlite3
from flask import Flask, request, render_template_string
from src.app.setup_db import setup_db

app = Flask(__name__)

# HTML templates for responses
root_page = "<h1> Use /login to view login screen </h1>"

login_page = '''
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
'''

welcome_page = "<h1>Welcome, admin!</h1>"
invalid_page = "<h1>Invalid username or password.</h1>"
internal_server_error = "<h1>Internal server error.</h1>"

@app.route('/', methods=['GET'])
def root():
    return render_template_string(root_page)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template_string(login_page), 200

    if not setup_db():
        return render_template_string(internal_server_error), 500

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)