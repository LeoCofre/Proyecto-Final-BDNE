from controlador.ControladorVendedor import ingresar_vendedor,buscar_vendedor,modificar_vendedor,eliminar_vendedor

def menu_Vendedores():
    while True:
        print("\n===== Menú Vendedores =====")
        print("1.- Ingresar")
        print("2.- Buscar")
        print("3.- Modificar")
        print("4.- Eliminar")
        print("5.- Volver al Menú Principal")
        print("=========================")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ingresar_vendedor()
        elif opcion == "2":
            buscar_vendedor()
        elif opcion == "3":
            modificar_vendedor()
        elif opcion == "4":
            eliminar_vendedor()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
