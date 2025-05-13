def agregar_bebida_db(bebida):
    pass
def buscar_bebida_db(nombre_bebida):
    pass
def editar_bebida_db(bebida):
    pass    
def eliminar_bebida_db(bebida):
        conn=conectar()
        try:
            if conn is not None:
                cursor=conn.cursor()
                cursor.execute("DELETE FROM bebidas WHERE id_bebida=%s",
                            (bebida.get_id_bebida(),))
                conn.commit()
                print("Bebida eliminada")
        except Exception as e:
            print(f"No se eliminaron registros {e}")
        finally:
            cursor.close()
            conn.close()