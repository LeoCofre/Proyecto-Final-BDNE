from modelo.ConexionSQL import conectar 
from modelo.BebidaSQL import Bebida

def agregar_bebida_db(bebida):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute( "INSERT INTO bebidas (nombre, precio, categoria, descripcion, cantidad ) VALUES (%s,%s,%s,%s,%s)",
                           (bebida.get_nombre(),
                            bebida.get_precio(),
                            bebida.get_categoria(),
                            bebida.get_descripcion(),
                            bebida.get_cantidad()))
            conn.commit()
            print("Bebida ingresada con éxito")
    except Exception as e:
        print(f"Error al agregar la bebida: {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_bebida_db(nombre_bebida):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM bebidas WHERE nombre = %s",
                (nombre_bebida,))
            bebida = cursor.fetchone()
            if bebida is not None:
                bebida_encontrada=Bebida(bebida[1],bebida[2],bebida[3],bebida[4],bebida[5])
                bebida_encontrada.set_id(bebida[0])
            else:
                bebida_encontrada=None
            return bebida_encontrada
        else:
            return None 
    except Exception as e:
        print(f"Error al buscar la bebida: {e}")
    finally:
        cursor.close()  
        conn.close()
def listar_bebidas_db():
    #Obtiene la lista de todas las bebidas en la base de datos SQL.
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, precio, categoria, descripcion, cantidad FROM bebidas")
            bebidas = cursor.fetchall()

            return bebidas if bebidas else "No hay bebidas registradas."  # Devolvemos directamente las tuplas
        else:
            return "No se pudo conectar a la base de datos."
    except Exception as e:
        print(f"Error al listar bebidas: {e}")
        return None
    finally:
        cursor.close()
        conn.close()


def editar_bebida_db(bebida):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("UPDATE bebidas SET nombre=%s,precio=%s,categoria=%s,descripcion=%s,cantidad=%s WHERE id=%s",
                           (bebida.get_nombre(),bebida.get_precio(),bebida.get_categoria(),bebida.get_descripcion(),bebida.get_cantidad(),bebida.get_id()))
            conn.commit()
            print("Bebida editada con éxito")
    except Exception as e:
        print(f"Error al editar la bebida: {e}")
    finally:
        cursor.close()  
        conn.close()

def eliminar_bebida_db(bebida):
        conn=conectar()
        try:
            if conn is not None:
                cursor=conn.cursor()
                cursor.execute("DELETE FROM bebidas WHERE id=%s",
                            (bebida.get_id(),))
                conn.commit()
                print("Bebida eliminada")
        except Exception as e:
            print(f"No se eliminaron registros {e}")
        finally:
            cursor.close()
            conn.close()