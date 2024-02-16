# from flask import Flask, render_template, request, redirect, url_for, session
# import sqlite3, os



# app = Flask(__name__)
# app.secret_key = b'g\xed\xe0\xcd\xbb\xea\xc2\x03\x8do\x10\xfe\xeb\xea7\xb7\xa9\xe4^\xb4'

# @app.route('/')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Connect to SQLite database
#         conn = sqlite3.connect('./UserData/main.db')
#         cursor = conn.cursor()

#         # Check if username and password match
#         cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#         user = cursor.fetchone()

#         conn.close()

#         if user:
#             if session['username'] == username and session['password'] == password:
#                 return redirect(url_for('dashboard'))
#         else:
#             return render_template('Login.html', error='Invalid username or password')

#     return render_template('Login.html')

# @app.route('/dashboard')
# def dashboard():
#     if 'username' in session:
#         return render_template('Dashboard.html', username=session['username'])
#     else:
#         return redirect(url_for('login'))

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=7770)

# from flask import Flask, render_template, request, redirect, url_for, session
# import sqlite3

# app = Flask(__name__)
# app.secret_key = b'g\xed\xe0\xcd\xbb\xea\xc2\x03\x8do\x10\xfe\xeb\xea7\xb7\xa9\xe4^\xb4'  # Set a fixed value for the secret key

# @app.route('/')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Connect to SQLite database
#         conn = sqlite3.connect('./UserData/main.db')
#         cursor = conn.cursor()

#         # Check if username and password match
#         cursor.execute('SELECT * FROM USERDATA WHERE Name = ? AND Password = ?', (username, password))
#         user = cursor.fetchone()

#         conn.close()

#         if user:
#             # Store username in session
#             session['username'] = username
#             return redirect(url_for('Dashboard'))
#         else:
#             return render_template('Login.html', error='Invalid username or password')

#     return render_template('Login.html')

# @app.route('/dashboard')
# def dashboard():
#     if 'username' in session:
#         return render_template('Dashboard.html', username=session['username'])
#     else:
#         return redirect(url_for('login'))  # Redirect to login if not logged in

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=7770)

"""
        Date And Time with Sensor Data Code
"""

# import sqlite3, os
# import flask, datetime, time
# from flask import Flask, render_template, render_template_string, redirect, request, url_for, session


# print("\n    Date\t   Time","\t\tSensor Data\n")

# while True:
    
#     Date = datetime.datetime.now().date()
#     Time = datetime.datetime.now().strftime('%H:%M:%S')
#     time.sleep(1)
#     print("\n",Date, "\t",Time, "\n")


from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a fixed value for the secret key

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to SQLite database
        conn = sqlite3.connect('./UserData/main.db')
        cursor = conn.cursor()

        # Check if username and password match
        cursor.execute('SELECT * FROM USERDATA WHERE Name = ? AND Password = ?', (username, password))
        user = cursor.fetchone()
        
        print("User from DB:", user)  # Debugging

        conn.close()

        if user:
            # Store username in session
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            print("Invalid username or password")  # Debugging
            return render_template('Login.html', error='Invalid username or password')

    return render_template('Login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('Dashboard.html', username=session['username'])
    else:
        return redirect(url_for('login'))  # Redirect to login if not logged in

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7770)
