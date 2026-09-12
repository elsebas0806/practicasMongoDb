from pymongo import MongoClient

usuario = "hector1985"
password = "Aime131985"
cluster = "utvt.qqqotrr.mongodb.net"


uri = f"mongodb+srv://{usuario}:{password}@{cluster}/"

cliente = MongoClient(uri)


bd = cliente["Jael-Sebastián-Segura-Segura"]


coleccion = bd["Jael_Sebastian_Segura"]


dato = {
    "nombre": "Jael-Sebastián-Segura-Segura"
}

coleccion.insert_one(dato)

print("===================================")
print("Conexion exitosa con MongoDB Atlas")
print("Base de datos: Jael Sebastián Segura Segura")
print("Coleccion: Jael_Sebastian_Segura")
print("Nombre guardado correctamente")
print("===================================")

cliente.close()