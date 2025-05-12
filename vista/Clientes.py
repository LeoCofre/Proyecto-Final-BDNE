from controlador.ControladorCliente import ingresar_cliente, buscar_cliente, modificar_cliente, eliminar_cliente

def menu_Clientes():
    while True:
        print("\n===== Menú Clientes =====")
        print("1.- Ingresar")
        print("2.- Buscar")
        print("3.- Modificar")
        print("4.- Eliminar")
        print("5.- Volver al Menú Principal")
        print("=========================")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ingresar_cliente()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
