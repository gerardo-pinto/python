import sqlite3

conn = sqlite3.connect('datos.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS datos
             (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, email TEXT)''')

conn.commit()
conn.close()
