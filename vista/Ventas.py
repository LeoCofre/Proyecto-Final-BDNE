from controlador.ControladorVenta import agregar_venta_db, buscar_venta_db, editar_venta_db, eliminar_venta_db

def menu_ventas():
    while True:
        print("\n===== Menú Ventas =====")
        print("1.- Ingresar")
        print("2.- Buscar")
        print("3.- Modificar")
        print("4.- Eliminar")
        print("5.- Volver al Menú Principal")
        print("=========================")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ingresar_venta()
        elif opcion == "2":
            buscar_venta()
        elif opcion == "3":
            editar_venta()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
def ingresar_venta():
    pass
def buscar_venta():
    pass
def editar_venta():
    pass
def eliminar_venta():
    pass

