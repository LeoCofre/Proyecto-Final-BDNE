from modelo.ConexionSQL import conectar
from modelo.ClienteSQL import Cliente

def agregar_cliente_db(cliente):
    conn = conectar()
    try:
        if conn is not None:
           cursor= conn.cursor()
           cursor.execute("INSERT INTO clientes(nombres, apellidos, rut, fecha_nacimiento, direccion, telefono, correo) VALUES (%s,%s,%s,%s,%s,%s,%s)",
           (cliente.get_nombres(), cliente.get_apellidos(), cliente.get_rut(), cliente.get_fecha_nacimiento(), cliente.get_direccion(), cliente.get_telefono(), cliente.get_correo()) )
           conn.commit()
           print("Cliente ingresado con exito")
    except Exception as e:
        print(f"Error al agregar cliente: ", {e})
    finally:
        cursor.close()
        conn.close()


def buscar_cliente_db(rut):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM clientes WHERE rut=%s",
                (rut,))
            cliente = cursor.fetchone()
            if cliente is not None:
                cliente_encontrado=Cliente(cliente [1],cliente[2],cliente[3],cliente[4],cliente[5],cliente[6],cliente[7])
                cliente_encontrado.set_id(cliente[0])
            else:
                cliente_encontrado=None
            return cliente_encontrado
        else:
            return None
    except Exception as e:
        print(f"Error al buscar cliente: {e}")
    finally:
        cursor.close()
        conn.close()

def editar_cliente_db(cliente):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET nombres=%s, apellidos=%s,rut=%s, fecha_nacimiento=%s, direccion=%s, telefono=%s, correo=%s WHERE id=%s",
                           (cliente.get_nombres(), cliente.get_apellidos(), cliente.get_rut(), cliente.get_fecha_nacimiento(),cliente.get_direccion(),cliente.get_telefono(),cliente.get_correo(),cliente.get_id_cliente()))
            conn.commit()
            print("Cliente editado con exito")
    except Exception as e:
        print(f"Error al editar cliente: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_cliente_db(cliente):
        conn=conectar()
        try:
            if conn is not None:
                cursor=conn.cursor()
                cursor.execute("DELETE FROM clientes WHERE id_cliente=%s",
                            (cliente.get_id_cliente(),))
                conn.commit()
                print("Cliente eliminado")
        except Exception as e:
            print(f"No se eliminaron registros {e}")
        finally:
            cursor.close()
            conn.close()


