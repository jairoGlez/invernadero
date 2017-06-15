import sqlite3

db = sqlite3.connect("invernadero.db")
c = db.cursor()

def mostrarUsuario():
    r = c.execute("SELECT * FROM usuario")
    r = r.fetchall()
    print(r)
    
    #for fila in r:
     #   print(fila)
        
        
mostrarUsuario()