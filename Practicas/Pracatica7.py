import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="traductor_python_ezequiel"
)

cursor = mydb.cursor()

while True:
    palabra = input("Ingrese la palabra a traducir: ")
    sentencia = f"select ingles from traductor where español like '{palabra}'"
    cursor.execute(sentencia)

    resultado = cursor.fetchall()

    #si eciste imprimir, sino solicitar para agregar una nueva palabra
    for x in resultado:
        print(f"{palabra} : {x[0]}")