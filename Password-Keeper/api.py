from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector 

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user= "root", 
    password="MySQL123",
)

def createdb():
    cursor = mydb.cursor()
    sql = '''CREATE TABLE users(
        u_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        u_name VARCHAR(50) NOT NULL,
        email VARCHAR(60) NOT NULL,
        password VARCHAR(70) NOT NULL) ;'''
    cursor.execute(sql)

    cursor = mydb.cursor()
    sql =  ''' CREATE TABLE id_pass(
        up_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        u_id FOREIGN KEY REFERENCES users(u_id) ON DELETE CASCADE,
        u_site VARCHAR(60),
        u_pass VARCHAR(70),
        u_uname VARCHAR(60)
    ) ;'''

def check_user(username, password):
    cursor = mydb.cursor()
    cursor.execute('SELECT username FROM users WHERE username=? AND password=?', (username,password))
    checkUsername = mycursor.fetchone()
    if checkUsername != 0:
        return false 
    else:
        return true 

def create_user(u_username, u_email, u_password):
    cursor = mydb.cursor()
    cursor.execute('INSERT INTO users(u_name, email, password) values(u_username, u_email, u_password)')
    return render_template('auth.html') 

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST', 'GET'])
def auth():
    if request.method == 'POST':
        info = request.form 
        return render_template('auth.html', info = info)
    else:
        return "Sorry, some error occured. Try again!"

if __name__ == '__main__':
    app.run(debug=True) 