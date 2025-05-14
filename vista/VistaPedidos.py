from modelo.Pedido import Pedido
from controlador.ControladorPedido import agregar_pedido_db, buscar_pedido_db, editar_pedido_db, eliminar_pedido_db


def menu_pedidos():
    print("=====Menu pedidos=====")
    print("1.- Ingresar Pedido ")
    print("2.- Buscar Pedido")
    print("3.- Modificar Pedido")
    print("4.- Eliminar Pedido")
    print("5.- Volver al Menú Principal")
    print("=========================")

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
    print("\n--- Buscar Pedido ---")
    id_cliente = input("Ingrese el ID del cliente para buscar su pedido: ")
    pedido = buscar_pedido_db(id_cliente)

    if pedido:
        print("\n=== Pedido Encontrado ===")
        print(f"Fecha: {pedido.get_fecha()}")
        print(f"ID Cliente: {pedido.get_id_cliente()}")
        print(f"Nombre Cliente: {pedido.get_nombre_cliente()}")
        print(f"Teléfono: {pedido.get_telefono()}")
        print(f"Correo: {pedido.get_correo()}")
        print(f"ID Vendedor: {pedido.get_id_vendedor()}")
        print(f"Nombre Vendedor: {pedido.get_nombre_vendedor()}")
        print(f"Estado: {pedido.get_estado()}")
        print(f"ID Bebida: {pedido.get_id_bebida()}")
        print(f"Nombre Bebida: {pedido.get_nombre_bebida()}")
        print(f"Cantidad: {pedido.get_cantidad()}")
        print(f"Precio Unitario: {pedido.get_precio_unitario()}")
        print(f"Total: {pedido.get_cantidad() * pedido.get_precio_unitario()}")
    else:
        print("No se encontró un pedido para ese ID de cliente.")
    return pedido



def modificar_pedido():
    try:
        id_cliente = input("Ingrese el ID del cliente del pedido que desea editar: ")
        pedido = buscar_pedido_db(id_cliente)
        
        if not pedido:
            print("No se encontró un pedido con ese ID de cliente.")
            return

        print(f"\nPedido encontrado:")
        print(f"ID Pedido: {pedido.get_id_pedido()}")
        print(f"Fecha: {pedido.get_fecha()}")
        print(f"Nombre Cliente: {pedido.get_nombre_cliente()}")
        print(f"Teléfono: {pedido.get_telefono()}")
        print(f"Correo: {pedido.get_correo()}")
        print(f"ID Vendedor: {pedido.get_id_vendedor()}")
        print(f"Nombre Vendedor: {pedido.get_nombre_vendedor()}")
        print(f"Estado: {pedido.get_estado()}")
        print(f"ID Bebida: {pedido.get_id_bebida()}")
        print(f"Nombre Bebida: {pedido.get_nombre_bebida()}")
        print(f"Cantidad: {pedido.get_cantidad()}")
        print(f"Precio Unitario: {pedido.get_precio_unitario()}")

        nueva_fecha = input("Ingrese la nueva fecha del pedido (presione Enter para mantener actual): ")
        nuevo_nombre_cliente = input("Ingrese el nuevo nombre del cliente (Enter para mantener): ")
        nuevo_telefono = input("Ingrese el nuevo teléfono del cliente (Enter para mantener): ")
        nuevo_correo = input("Ingrese el nuevo correo del cliente (Enter para mantener): ")
        nuevo_id_vendedor = input("Ingrese el nuevo ID del vendedor (Enter para mantener): ")
        nuevo_nombre_vendedor = input("Ingrese el nuevo nombre del vendedor (Enter para mantener): ")
        nuevo_estado = input("Ingrese el nuevo estado del pedido (Enter para mantener): ")
        nuevo_id_bebida = input("Ingrese el nuevo ID de la bebida (Enter para mantener): ")
        nuevo_nombre_bebida = input("Ingrese el nuevo nombre de la bebida (Enter para mantener): ")
        nueva_cantidad = input("Ingrese la nueva cantidad (Enter para mantener): ")
        nuevo_precio_unitario = input("Ingrese el nuevo precio unitario (Enter para mantener): ")

        if nueva_fecha:
            pedido.set_fecha(nueva_fecha)
        if nuevo_nombre_cliente:
            pedido.set_nombre_cliente(nuevo_nombre_cliente)
        if nuevo_telefono:
            pedido.set_telefono(nuevo_telefono)
        if nuevo_correo:
            pedido.set_correo(nuevo_correo)
        if nuevo_id_vendedor:
            pedido.set_id_vendedor(nuevo_id_vendedor)
        if nuevo_nombre_vendedor:
            pedido.set_nombre_vendedor(nuevo_nombre_vendedor)
        if nuevo_estado:
            pedido.set_estado(nuevo_estado)
        if nuevo_id_bebida:
            pedido.set_id_bebida(nuevo_id_bebida)
        if nuevo_nombre_bebida:
            pedido.set_nombre_bebida(nuevo_nombre_bebida)
        if nueva_cantidad:
            pedido.set_cantidad(int(nueva_cantidad))
        if nuevo_precio_unitario:
            pedido.set_precio_unitario(int(nuevo_precio_unitario))

        editar_pedido_db(pedido)
        print("Pedido modificado exitosamente.")

    except ValueError:
        print("Error: La cantidad y el precio deben ser valores numéricos.")
    except Exception as e:
        print(f"Error al editar el pedido: {e}")

def eliminar_pedido():
    try:
        id_cliente = input("Ingrese el ID del cliente del pedido que desea eliminar: ")
        pedido = buscar_pedido_db(id_cliente)

        if not pedido:
            print("No se encontró un pedido con ese ID de cliente.")
            return

        print("\nPedido encontrado:")
        print(f"ID Pedido: {pedido.get_id_pedido()}")
        print(f"Nombre Cliente: {pedido.get_nombre_cliente()}")
        print(f"Fecha: {pedido.get_fecha()}")
        print(f"Estado: {pedido.get_estado()}")
        confirmar = input("¿Está seguro que desea eliminar este pedido? (s/n): ")

        if confirmar.lower() == 's':
            eliminar_pedido_db(id_cliente)
            print("Pedido eliminado exitosamente.")
        else:
            print("Operación cancelada.")

    except Exception as e:
        print(f"Error al eliminar el pedido: {e}")

