from conexion import invernadero

class Menu:
    inv = invernadero()
    def __init__(self):
        while True:
            print("1) Mostrar usuarios")
            print("2) Agregar usuarios")
            print("0) Salir")
            op = input()
            
            if op =="1":
                self.mostrar()
            elif op =="2":
                self.capturar()
            elif op =="0":
                break
                
    def mostrar(self):
        usuarios = self.inv.mostrarUsuario()
        for u in usuarios:
            print("{0:2} {1:10} {2:10} {3:10} {4:25} {5:8} {6:2}".format(u[0],u[1],u[2],u[3],u[4],u[5],u[6]))
            
    def capturar(self):
        nombre = input("Nombre: ")
        apellido1 = input("Apellido paterno: ")
        apellido2 = input("Apellido materno: ")
        correo = input("Correo: ")
        password = input("Contraseña: ")
        tipo = input("Tipo: ")
        
        self.inv.insertarUsuario([nombre,apellido1,apellido2,correo,password,tipo])