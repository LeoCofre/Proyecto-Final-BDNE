def menu_pedidos():
    print("Menu pedidos")
    print("1.- Ingresar Pedido ")
    print("2.- Buscar Pedido")
    print("3.- Modificar Pedido")
    print("4.- Eliminar Pedido")


def main_pedido():
    opcion = input("===Elija una opción")
    while True:
        if opcion == 1:
            ingresar_pedido()
        elif opcion == 2:
            buscar_pedido()
        elif opcion == 3:
            modificar_pedido()
        elif opcion == 4:
            eliminar_pedido()       

        def ingresar_pedido():
            pass
        def buscar_pedido():
            pass
        def modificar_pedido():
            pass
        def eliminar_pedido():
            pass
