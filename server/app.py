#!/usr/bin/env python3

from flask import Flask
from urllib.parse import quote as url_quote


app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero'
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Error: Invalid operation'
    return 'Operation not recognized. Please use one of the following: + - * div %'

if __name__ == "__main__":
    app.run(debug=True, port=5555)