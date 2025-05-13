from modelo.ConexionSQL import conectar
from modelo.VendedorSQL import Vendedor

def agregar_vendedor_db(vendedor):
    conn = conectar()
    try:
        if conn is not None:
           cursor= conn.cursor()
           cursor.execute("INSERT INTO vendedores(nombres, apellidos, rut, fecha_nacimiento, direccion, telefono, correo) VALUES (%s,%s,%s,%s,%s,%s,%s)",
           (vendedor.get_nombres(), vendedor.get_apellidos(), vendedor.get_rut(), vendedor.get_fecha_nacimiento(), vendedor.get_direccion(), vendedor.get_telefono(), vendedor.get_correo()) )
           conn.commit()
           print("vendedor ingresado con exito")
    except Exception as e:
        print(f"Error al agregar vendedor: ", {e})
    finally:
        cursor.close()
        conn.close()


def buscar_vendedor_db(rut):
    conn=conectar()
    try:
        if conn is not None:
            cursor=conn.cursor()
            cursor.execute(
                "SELECT * FROM vendedores WHERE rut=%s",
                (rut,))
            vendedor = cursor.fetchone()
            if vendedor is not None:
                vendedor_encontrado=Vendedor(vendedor [1],vendedor[2],vendedor[3],vendedor[4],vendedor[5],vendedor[6],vendedor[7])
                vendedor_encontrado.set_id_vendedor(vendedor[0])
            else:
                vendedor_encontrado=None
            return vendedor_encontrado
        else:
            return None
    except Exception as e:
        print(f"Error al buscar vendedor: {e}")
    finally:
        cursor.close()
        conn.close()

def editar_vendedor_db(vendedor):
    conn = conectar()
    try:
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("UPDATE vendedores SET nombres=%s, apellidos=%s,rut=%s, fecha_nacimiento=%s, direccion=%s, telefono=%s, correo=%s WHERE id_vendedor=%s",
                           (vendedor.get_nombres(), vendedor.get_apellidos(), vendedor.get_rut(), vendedor.get_fecha_nacimiento(),vendedor.get_direccion(),vendedor.get_telefono(),vendedor.get_correo(),vendedor.get_id_vendedor()))
            conn.commit()
            print("vendedor editado con exito")
    except Exception as e:
        print(f"Error al editar vendedor: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_vendedor_db(vendedor):
        conn=conectar()
        try:
            if conn is not None:
                cursor=conn.cursor()
                cursor.execute("DELETE FROM vendedores WHERE id_vendedor=%s",
                            (vendedor.get_id_vendedor(),))
                conn.commit()
                print("vendedor eliminado")
        except Exception as e:
            print(f"No se eliminaron registros {e}")
        finally:
            cursor.close()
            conn.close()


