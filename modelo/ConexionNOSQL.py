import pymongo
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
 
def conectar_mongodb():
    try:
        # Parámetros de conexión
        MONGO_URI = "mongodb://localhost:27017/"
        MONGO_BASE_DATOS = "botilleria"

        # Establecer conexión
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = cliente[MONGO_BASE_DATOS]
        
        # Probar conexión
        cliente.server_info()  # Esto lanza una excepción si la conexión falla
        print(f"Conexión exitosa a {MONGO_BASE_DATOS}")
        return db

    except ConnectionFailure as e:
        print(f"No se pudo conectar a la base de datos: {e}")
        return None

