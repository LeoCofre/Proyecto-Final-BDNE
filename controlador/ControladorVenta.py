from modelo.ConexionNOSQL import conectar_mongodb
from modelo.Venta import Venta

def agregar_venta_db(venta):
    #Agrega una venta a la base de datos MongoDB.
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["ventas"]
            coleccion.insert_one(venta.to_dict())  # Convertimos el objeto a diccionario
            print(" Venta ingresada con éxito.")
        except Exception as e:
            print(f" Error al agregar venta: {e}")
    else:
        print(" No se pudo conectar a la base de datos.")

def buscar_venta_db(id_venta):
    #Busca una venta en MongoDB por su ID que ingresamos de forma manual.
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["ventas"]
            venta = coleccion.find_one({"id_venta": id_venta})  # Buscamos por `id_venta`
            return venta if venta else None  # Devuelve None si no encuentra la venta
        except Exception as e:
            print(f" Error al buscar venta: {e}")
            return None
    else:
        print(" No se pudo conectar a la base de datos.")
        return None
def listar_ventas_db():
    #Obtiene la lista de todas las ventas en MongoDB.
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["ventas"]
            ventas = list(coleccion.find({}, {"_id": 0}))  # Excluimos el ID de MongoDB
            return ventas if ventas else " No hay ventas registradas."
        except Exception as e:
            print(f" Error al listar ventas: {e}")
            return None
    else:
        print(" No se pudo conectar a la base de datos.")
        return None

def editar_venta_db(id_venta, nuevos_datos):
    #Edita una venta en MongoDB usando el ID manual.
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["ventas"]
            resultado = coleccion.update_one({"id_venta": id_venta}, {"$set": nuevos_datos})
            return " Venta actualizada." if resultado.modified_count > 0 else " No se modificó ninguna venta."
        except Exception as e:
            print(f" Error al editar venta: {e}")
            return None
    else:
        print(" No se pudo conectar a la base de datos.")
        return None

def eliminar_venta_db(id_venta):
    #Elimina una venta de la base de datos MongoDB por su ID.
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["ventas"]
            resultado = coleccion.delete_one({"id_venta": id_venta})  # Eliminar por `id_venta`
            return " Venta eliminada." if resultado.deleted_count > 0 else " No se encontró la venta."
        except Exception as e:
            print(f" Error al eliminar venta: {e}")
            return None
    else:
        print(" No se pudo conectar a la base de datos.")
        return None
