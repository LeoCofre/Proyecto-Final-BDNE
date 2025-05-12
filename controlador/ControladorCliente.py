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


def buscar_cliente_db(nombre_cliente):
    pass

def editar_cliente_db(cliente):
    pass

def eliminar_cliente_db(cliente):
    pass

