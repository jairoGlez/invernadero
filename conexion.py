import sqlite3

db = sqlite3.connect("invernadero.db")
c = db.cursor()

def mostrarUsuario():
    r = c.execute("SELECT * FROM usuario")
    r = r.fetchall()
    
    for fila in r:
        print(fila)
        
def insertarUsuario(datos):
    c.execute("INSERT INTO usuario (nombre, apellido1, apellido2, correo, password, tipo) VALUES (?,?,?,?,?,?)", (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]))
    db.commit()
        
        
insertarUsuario(["J","G","G","j@hotmail.com","pswrd",5])
mostrarUsuario()