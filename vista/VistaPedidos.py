from modelo.Pedido import Pedido
from controlador.ControladorPedido import agregar_pedido_db, buscar_pedido_db, editar_pedido_db, eliminar_pedido_db
def menu_pedidos():
    print("Menu pedidos")
    print("1.- Ingresar Pedido ")
    print("2.- Buscar Pedido")
    print("3.- Modificar Pedido")
    print("4.- Eliminar Pedido")
    print("5.- Volver al Menú Principal")
    print("=========================")

def main_pedido():
    opcion = int(input("===Elija una opción==="))
    while True:
        if opcion == 1:
            ingresar_pedido()
        elif opcion == 2:
            buscar_pedido()
        elif opcion == 3:
            modificar_pedido()
        elif opcion == 4:
            eliminar_pedido()       
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

            
def ingresar_pedido():
    fecha = input("Ingrese la fecha del pedido: ")
    id_cliente = input("Ingrese el ID del cliente: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    id_vendedor = input("Ingrese el ID del vendedor: ")
    nombre_vendedor = input("Ingrese el nombre del vendedor: ")
    estado = input("Ingrese el estado del pedido: ")
    id_bebida = input("Ingrese el ID de la bebida: ")
    nombre_bebida = input("Ingrese el nombre de la bebida: ")
    cantidad = int(input("Ingrese la cantidad de bebidas: "))
    precio_unitario = int(input("Ingrese el precio unitario: "))

    pedido = Pedido(fecha, id_cliente, nombre_cliente, telefono, correo, id_vendedor, nombre_vendedor, estado, id_bebida, nombre_bebida, cantidad, precio_unitario)
    agregar_pedido_db(pedido)

def buscar_pedido():
    pass
def modificar_pedido():
    pass
def eliminar_pedido():
    pass
