from flask import Flask,render_template
import sqlite3
app=Flask(__name__)

def __init__(self) :
    con=sqlite3.connect('user1.db')
    c=con.cursor
    c.execute("CREATE TABLE user1 (name text,password text)")
    con.commit
    

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    return render_template('market.html')


@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

