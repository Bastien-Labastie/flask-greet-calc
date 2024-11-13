from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a, b)

    return str(res)

@app.route('/sub')
def subtraction():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a, b)

    return str(res)

@app.route('/mult')
def multiplication():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a, b)

    return str(res)

@app.route('/div')
def devision():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a, b)

    return str(res)

operations = {"add": add, "sub": sub, "mult": mult, "div": div}

@app.route('/math/<oper>')
def math(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = operations[oper](a, b)

    return str(res)