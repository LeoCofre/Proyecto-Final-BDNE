import pymongo
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
 
import pymongo
from pymongo.errors import ConnectionFailure

def conectar_mongodb(): 
    try:
        MONGO_URI = "mongodb://localhost:27017/"
        MONGO_BASE_DATOS = "botilleria"

        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = cliente[MONGO_BASE_DATOS]
        cliente.server_info()
        print(f"Conexión exitosa a {MONGO_BASE_DATOS}")
        return db

    except ConnectionFailure as e:
        print(f"No se pudo conectar a la base de datos: {e}")
        return None

