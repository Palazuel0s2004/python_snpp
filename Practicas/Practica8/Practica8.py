from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/ver")
def saludar():
    return "<h1>hola mundo</h1>"

@app.route("/hora")
def hora():
    #calcular hora
    ahora = datetime.now().strftime("%H:%M:%S")
    return f"<h1>la hora es: {ahora}</h1>"

@app.route("/ip")
def mostrar_ip():
    # Obtener la IP del cliente
    ip_cliente = request.remote_addr
    return f"<h1>Tu dirección IP es: {ip_cliente}</h1>"

if __name__ == "__main__":
    app.run(debug=True)