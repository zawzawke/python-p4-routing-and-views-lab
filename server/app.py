#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:num>')
def count(num):
    numbers = ''
    for i in range(num):
        numbers += f"{i}\n"
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2 
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1/num2 if num2 != 0 else 'Error: Divide by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Invalid Operation' 
    return str(result)   



if __name__ == '__main__':
    app.run(port=5555, debug=True) 
