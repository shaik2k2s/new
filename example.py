from flask import Flask,rquest
app=Flask(__name__)

@app.route('/')
def greet():
    print("hello world welcome")
    
