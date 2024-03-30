from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def greet():
    return("hello world welcome")

@app.route('/greet1')
def greet1():
    return ("TATA Bye")

@app.route("/greet2")
def greet2():
    return 'hi sahil bhai'

@app.route('/addition')
def addition():
    a=10
    b=20
    return str([a+b])

@app.route('/addition1', methods=["POST"])
def addition1():
    a=10
    b=20
    return ([a+b])

if __name__=='__main__':
     app.run(host='0.0.0.0',port=8000)
