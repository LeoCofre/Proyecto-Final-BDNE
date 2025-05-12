def menu_pedidos():
    print("Menu pedidos")
    print("1.- Ingresar ")
    print("2.- Buscar")
    print("3.- Modificar")
    print("4.- Eliminar")

opcion = input("Elija una opción")
while True:
    if opcion == 1:
        ingresar_pedidos()
    elif opcion == 2:
        buscar_pedidos()
    elif opcion == 3:
        modificar_pedidos()
    elif opcion == 4:
        eliminar_pedidos()       

