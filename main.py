import flask, datetime
import os, time
import sqlite3
import platform
from flask import Flask, request, redirect, render_template, render_template_string, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a fixed value for the secret key

@app.route('/')
@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        ID = request.form['ID']
        Password = request.form['Password']
        
        
        conn = sqlite3.connect('./UserData/User.db')
        cursor = conn.cursor()

        
        cursor.execute('SELECT * FROM USER WHERE Name = ? AND Password = ?', (ID, Password))
        user = cursor.fetchone()
        
        conn.close()

        if user:
        
            session['ID'] = ID
            return redirect('/Dashboard')
        else:
            return render_template('Login.html', error='User Not Found')

    return render_template('Login.html')

@app.route('/Dashboard')
def dashboard():
    if 'ID' in session:
        return render_template('Dashboard.html', User=session['ID'])
    else:
        return redirect('/Login')  

# @app.route('/Signup', methods=['GET', 'POST'])
# def Signup():

#     if request.method == 'POST':

#         ID = request.form['ID']
#         Name = request.form['Name']
#         Name = request.form['']
#         Name = request.form['']

#     return render_template('Signup.html')


@app.route('/Logout')
def Logout():
    session.pop('ID', None)
    return redirect('/Login')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7770)
