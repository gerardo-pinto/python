from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('datos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM datos')
    datos = c.fetchall()
    conn.close()
    return render_template('index.html', datos=datos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    email = request.form['email']
    conn = sqlite3.connect('datos.db')
    c = conn.cursor()
    c.execute('INSERT INTO datos (nombre, email) VALUES (?, ?)', (nombre, email))
    conn.commit()
    conn.close()
    return 'Datos agregados correctamente'

if __name__ == '__main__':
    app.run(debug=True)
