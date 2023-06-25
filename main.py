from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors, re, hashlib
from flask_bootstrap import Bootstrap
import mysql.connector


app = Flask(__name__)
Bootstrap(app)
my_sql = MySQL(app)

app.secret_key = 'secretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'escape04'
app.config['MYSQL_DB'] = 'data_base'


db= mysql.connector.connect(
    host='localhost',
    user='root',
    password='escape04',
    database='data_base'
)

if db.is_connected():
    print("Connected to the database.")

db.close()




@app.route('/', methods=['GET', 'POST'])
def login():
    # Output a message if something goes wrong...
    msg = ''

    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = my_sql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database

        if username == 'admin' and password == 'passwords@12345':
        # User credentials are correct, create session data
            session['loggedin'] = True
            session['username'] = username

            return redirect ('/admin')
        elif account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully!'
            return render_template("data.html",msg=msg)

        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

@app.route("/data",methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        quantity = request.form['quantity']
        weight = request.form['weight']
        boxcount = request.form['boxcount']

        db.reconnect()
        cursor = db.cursor()

        sql = "INSERT INTO customers (ItemCustomer, customer1) VALUES (%s, %s);"

        values = [
            ('Quantity', quantity),
            ('Weight', weight),
            ('BoxCount', boxcount)
        ]

        for value in values:
            cursor.execute(sql, value)

        db.commit()
        data = cursor.fetchall()
        cursor.close()
        # return render_template('view.html', data=data)
        return render_template("index.html")

    return render_template("data.html")

@app.route('/admin')
def view():
    db.reconnect()
    cursor = db.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()

    return render_template('view.html', data=data)

app.run(debug=True)