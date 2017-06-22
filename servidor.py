from flask import Flask, jsonify
from conexion import invernadero

app = Flask("bd")
inv = invernadero()

@app.route("/")
def raiz():
    return("Hola")

@app.route("/usuarios")
def usuarios():
    usuarios = inv.mostrarUsuario()
    print(usuarios)
    respuesta = jsonify(usuarios)
    return respuesta

app.run()
