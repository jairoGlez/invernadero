from flask import Flask
app = Flask("bd")

@app.route("/")
def raiz():
    return ("Hola")

app.run()
