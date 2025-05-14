from modelo.ConexionNOSQL import conectar_mongodb
from modelo.Pedido import Pedido

def agregar_pedido_db(pedido):
    #Agrega un pedido a la base de datos MongoDB.
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["pedidos"]
            coleccion.insert_one(pedido.to_dict())  # Convertimos el objeto a diccionario
            print(" Pedido ingresado con éxito.")
        except Exception as e:
            print(f" Error al agregar pedido: {e}")
    else:
        print(" No se pudo conectar a la base de datos.")

def buscar_pedido_db(id_pedido):
    """Busca un pedido en MongoDB por su ID manual."""
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["pedidos"]
            pedido = coleccion.find_one({"id_pedido": id_pedido})  # Ahora buscamos por `id_pedido`
            return pedido if pedido else None  # Devuelve None si no encuentra el pedido
        except Exception as e:
            print(f" Error al buscar pedido: {e}")
            return None
    else:
        print(" No se pudo conectar a la base de datos.")
        return None


def editar_pedido_db(id_pedido, nuevos_datos):
    """Edita un pedido en MongoDB usando el ID manual."""
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["pedidos"]
            resultado = coleccion.update_one({"id_pedido": id_pedido}, {"$set": nuevos_datos})
            return " Pedido actualizado." if resultado.modified_count > 0 else " No se modificó ningún pedido."
        except Exception as e:
            print(f" Error al editar pedido: {e}")
            return None
    else:
        print(" No se pudo conectar a la base de datos.")
        return None

def eliminar_pedido_db(id_pedido):
    """Elimina un pedido de la base de datos MongoDB por su ID."""
    db = conectar_mongodb()
    if db is not None:
        try:
            coleccion = db["pedidos"]
            resultado = coleccion.delete_one({"id_pedido": id_pedido})  # Eliminar por `id_pedido`
            return " Pedido eliminado." if resultado.deleted_count > 0 else " No se encontró el pedido."
        except Exception as e:
            print(f" Error al eliminar pedido: {e}")
            return None
    else:
        print(" No se pudo conectar a la base de datos.")
        return None

