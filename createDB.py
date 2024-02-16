import sqlite3


DB = sqlite3.connect('./UserData/User.db')

Curs = DB.cursor()

Curs.execute("""insert into User(id, Name, Mail, Password) values(1, 'Ajhay', 'ajhay.n50@gmail.com', 'Password')""")
DB.commit()
Curs.close()
DB.close()