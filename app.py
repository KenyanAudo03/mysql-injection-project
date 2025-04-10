from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)

app.secret_key = 'secret_key'

# Database Config

db = mysql.connector.connect(
    host = 'localhost',
    user = 'username',
    password = 'userpass',
    database = 'mysql_injection'
)
cursor = db.cursor(dictionary=True)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        
        query = "SELECT * FROM user WHERE username = '" + username + "' AND password = '" + password + "'"
        
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                session['username'] = username
                return redirect('/welcome')
            else:
                flash("Invalid Login Credentials")
        except Exception as e:
            flash(f"Error: {str(e)}")
            
        return redirect('/')
            
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        flash("You are not logged in")
        return redirect('/')
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)