import sqlite3

class invernadero:
    db = sqlite3.connect("invernadero.db")
    c = db.cursor()

    def mostrarUsuario(self):
        r = self.c.execute("SELECT * FROM usuario")
        r = r.fetchall()
        lista = []

        for fila in r:
            lista.append(fila)
            
        return lista;

    def insertarUsuario(self,datos):
        self.c.execute("INSERT INTO usuario (nombre, apellido1, apellido2, correo, password, tipo) VALUES (?,?,?,?,?,?)", (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]))
        self.db.commit()
        
        
