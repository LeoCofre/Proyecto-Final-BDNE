from modelo.Pedido import Pedido
from controlador.ControladorPedido import agregar_pedido_db, buscar_pedido_db, editar_pedido_db, eliminar_pedido_db

def menu_pedidos():
    while True:
        print("\n===== Menú Pedido =====")
        print("1.- Ingresar Pedido ")
        print("2.- Buscar Pedido")
        print("3.- Modificar Pedido")
        print("4.- Eliminar Pedido")
        print("5.- Volver al Menú Principal")
        print("=========================")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            ingresar_pedido()
        elif opcion == "2":
            buscar_pedido()
        elif opcion == "3":
            modificar_pedido()
        elif opcion == "4":
            eliminar_pedido()       
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

            
def ingresar_pedido():
    
    pass
def buscar_pedido():
    pass
def modificar_pedido():
    pass
def eliminar_pedido():
    pass
