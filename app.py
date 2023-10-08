from flask import Flask, render_template, request, redirect
import sqlite3
import control

app = Flask(__name__)


@app.route('/')
def index():
    # return redirect('https://api.kanye.rest/')
    return render_template("index.html")


@app.route('/relatorios')
def gerar():
    # return redirect('https://api.kanye.rest/')
    return render_template("home.html")


@app.route('/get_red', methods=['GET'])
def insert_user():
    if request.method == 'GET':
        print("entou?")
        control.red('red')
        return "mentiras"


@app.route('/get_orange', methods=['GET'])
def laran():
    if request.method == 'GET':
        print("entou?")
        control.red('orange')
        return "mentiras"


@app.route('/get_green', methods=['GET'])
def verde():
    if request.method == 'GET':
        print("entou?")
        control.red('green')
        return "mentiras"


if __name__ == '__main__':
    app.run(debug=True)
