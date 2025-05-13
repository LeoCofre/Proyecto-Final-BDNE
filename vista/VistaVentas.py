from controlador.ControladorVenta import agregar_venta_db, buscar_venta_db, editar_venta_db, eliminar_venta_db
from modelo.Venta import Venta
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
    fecha = input("Ingrese la fecha de la venta: ")
    id_pedido = input("Ingrese el ID del pedido: ")
    id_cliente = input("Ingrese el ID del cliente: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    total = input("Ingrese el total de la venta: ")
    medio_de_pago = input("Ingrese el medio de pago: ")

    venta = Venta(fecha, id_pedido, id_cliente, nombre_cliente, total, medio_de_pago)
    agregar_venta_db(venta)

def buscar_venta():
    pass
def editar_venta():
    pass
def eliminar_venta():
    pass

