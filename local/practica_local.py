from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")


bd = cliente["escuela"]


coleccion = bd["estudiantes"]

estudiante = {
    "nombre": "Sebastian",
    "edad": 18,
    "carrera": "Informatica"
}
estudiante = {
    "nombre": "Geronimo",
    "edad": 20,
    "carrera": "Negocios"
}
estudiante = {
    "nombre": "Saul",
    "edad": 22,
    "carrera": "Merca"
}




resultado = coleccion.insert_one(estudiante)

print("Conexion exitosa con MongoDB")
print("Base de datos: escuela")
print("Coleccion: estudiantes")
print("Estudiante insertado correctamente")
print("ID:", resultado.inserted_id)

# Cerrar conexión
cliente.close()