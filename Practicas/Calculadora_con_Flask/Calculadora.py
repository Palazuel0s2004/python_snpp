from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method == "POST":
        try:
            numero1 = float(request.form["num1"])
            numero2 = float(request.form["num2"])
        except ValueError:
            return render_template("index.html", error="Error: Entrada no válida. Asegúrate de ingresar números.")
        
        operacion = request.form.get('op')
        
        if operacion not in ["+", "-", "x", "/"]:
            return render_template("index.html", error="Error: Operación no válida.")

        if operacion == "+":
            resultado = numero1 + numero2
        elif operacion == "-":
            resultado = numero1 - numero2
        elif operacion == "x":
            resultado = numero1 * numero2
        elif operacion == "/":
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                return render_template("index.html", error="Error: División por cero no permitida.")
        
        return render_template("index.html", result=resultado)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)