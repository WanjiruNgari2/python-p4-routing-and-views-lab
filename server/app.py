#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter


@app.route('/count/<parameter>')
def count(parameter):
    count = ''
    for i in range(int(parameter)):
        count += str(i) + '\n'
    return count

@app.route('/math/<int:parameter1>/<operation>/<int:parameter2>')
def math(parameter1, operation, parameter2):
    if operation == '+':
        return str(parameter1 + parameter2)
    elif operation == '-':
        return str(parameter1 - parameter2)
    elif operation == '*':
        return str(parameter1 * parameter2)
    elif operation == '/':
        return str(parameter1 / parameter2)
    elif operation == '%':
        return str(parameter1 % parameter2)
    elif operation == '**':
        return str(parameter1 ** parameter2)
    elif operation == "div":
        return str(parameter1 // parameter2)  if parameter1 % parameter2 != 0 else str(float(parameter1 // parameter2))
    else:
        return 'Invalid operation' 



if __name__ == '__main__':
    app.run(port=5555, debug=True)
