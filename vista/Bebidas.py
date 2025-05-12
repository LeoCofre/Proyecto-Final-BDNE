
def menu_bebidas():
    print("Menu bebidas")
    print("1.- Ingresar ")
    print("2.- Buscar")
    print("3.- Modificar")
    print("4.- Eliminar")

opcion = input("Elija una opción")
while True:
    if opcion == 1:
        ingresar_bebida()
    elif opcion == 2:
        buscar_bebida()
    elif opcion == 3:
        modificar_bebida()
    elif opcion == 4:
        eliminar_bebida()       
