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

    return '', 501

