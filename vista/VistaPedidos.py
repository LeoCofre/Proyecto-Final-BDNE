from modelo.Pedido import Pedido
from controlador.ControladorPedido import agregar_pedido_db, buscar_pedido_db, editar_pedido_db, eliminar_pedido_db,listar_pedidos_db

def menu_pedidos():
    print("=====Menu pedidos=====")
    print("1.- Ingresar Pedido ")
    print("2.- Buscar Pedido")
    print("3.- Mostrar Pedidos ")
    print("4.- Modificar Pedido")
    print("5.- Eliminar Pedido")
    print("6.- Volver al Menú Principal")
    print("=========================")

    opcion = int(input("===Elija una opción==="))
    while True:
        if opcion == 1:
            ingresar_pedido()
        elif opcion == 2:
            buscar_pedido()
        elif opcion == 3:
            mostrar_pedidos()
        elif opcion == 4:
            modificar_pedido()
        elif opcion == 5:
            eliminar_pedido()       
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        
def ingresar_pedido():
    id_pedido = input("Ingrese el ID del pedido: ")  # Ahora el usuario ingresa manualmente el ID
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

    pedido = Pedido(id_pedido, fecha, id_cliente, nombre_cliente, telefono, correo, id_vendedor, nombre_vendedor, estado, id_bebida, nombre_bebida, cantidad, precio_unitario)
    
    agregar_pedido_db(pedido)

    print("\n Pedido registrado con éxito.")
    menu_pedidos()  # Vuelve al menú automáticamente


def buscar_pedido():
    print("\n--- Buscar Pedido ---")
    id_pedido = input("Ingrese el ID del pedido a buscar: ")
    pedido = buscar_pedido_db(id_pedido)  # Este devuelve un diccionario, no un objeto `Pedido`

    if pedido and isinstance(pedido, dict):  # Verificamos que sea un pedido válido
        print("\n=== Pedido Encontrado ===")
        print(f"Fecha: {pedido['fecha']}")
        print(f"ID Cliente: {pedido['cliente']['id_cliente']}")
        print(f"Nombre Cliente: {pedido['cliente']['nombre_cliente']}")
        print(f"Teléfono: {pedido['cliente']['telefono']}")
        print(f"Correo: {pedido['cliente']['correo']}")
        print(f"ID Vendedor: {pedido['vendedor']['id_vendedor']}")
        print(f"Nombre Vendedor: {pedido['vendedor']['nombre_vendedor']}")
        print(f"Estado: {pedido['estado']}")
        print(f"ID Bebida: {pedido['detalles']['id_bebida']}")
        print(f"Nombre Bebida: {pedido['detalles']['nombre_bebida']}")
        print(f"Cantidad: {pedido['detalles']['cantidad']}")
        print(f"Precio Unitario: {pedido['detalles']['precio_unitario']}")
        print(f"Total: {pedido['detalles']['cantidad'] * pedido['detalles']['precio_unitario']}")
    else:
        print(" No se encontró el pedido en la base de datos.")

    menu_pedidos()


def mostrar_pedidos():
    print("\n--- Listado de Pedidos ---")
    pedidos = listar_pedidos_db()

    if isinstance(pedidos, list):
        for pedido in pedidos:
            print(f"\n ID Pedido: {pedido['id_pedido']}")
            print(f"Fecha: {pedido['fecha']}")
            print(f"Cliente: {pedido['cliente']['nombre_cliente']}")
            print(f"Estado: {pedido['estado']}")
            print(f"Bebida: {pedido['detalles']['nombre_bebida']}")
            print(f"Cantidad: {pedido['detalles']['cantidad']} | Precio: ${pedido['detalles']['precio_unitario']}")
            print("==================")
    else:
        print(pedidos)  # Mensaje si no hay pedidos

    menu_pedidos()


def modificar_pedido():
    try:
        id_pedido = input("Ingrese el ID del pedido que desea editar: ")
        pedido = buscar_pedido_db(id_pedido)

        if not pedido or not isinstance(pedido, dict):
            print(" No se encontró un pedido con ese ID.")
            return

        print("\nPedido encontrado:")
        print(f"Fecha: {pedido['fecha']}")
        print(f"Nombre Cliente: {pedido['cliente']['nombre_cliente']}")
        print(f"Estado: {pedido['estado']}")

        nuevo_estado = input("Ingrese el nuevo estado del pedido (Enter para mantener): ")

        # Preparamos los cambios en un diccionario para actualizar en MongoDB
        cambios = {}
        if nuevo_estado:
            cambios["estado"] = nuevo_estado

        if cambios:
            editar_pedido_db(id_pedido, cambios)
            print(" Pedido modificado exitosamente.")
        else:
            print("⚠ No se realizó ninguna modificación.")

    except Exception as e:
        print(f" Error al editar el pedido: {e}")
    menu_pedidos()    


def eliminar_pedido():
    try:
        id_pedido = input("Ingrese el ID del pedido que desea eliminar: ")
        pedido = buscar_pedido_db(id_pedido)

        if not pedido:
            print(" No se encontró el pedido.")
            return

        confirmar = input("¿Está seguro que desea eliminar este pedido? (s/n): ")

        if confirmar.lower() == 's':
            eliminar_pedido_db(id_pedido)
            print(" Pedido eliminado exitosamente.")
        else:
            print("Operación cancelada.")

    except Exception as e:
        print(f" Error al eliminar el pedido: {e}")
    menu_pedidos()