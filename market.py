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
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template('market.html',items=items)


@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

