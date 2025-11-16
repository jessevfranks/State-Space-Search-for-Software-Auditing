from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    return '', 501

