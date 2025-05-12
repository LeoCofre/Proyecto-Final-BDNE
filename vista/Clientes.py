from controlador.ControladorCliente import agregar_cliente_db, buscar_cliente_db, eliminar_cliente_db, editar_cliente_db
from modelo.ClienteSQL import Cliente

def menu_clientes():
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

def ingresar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    rut = input("Ingrese el RUT del cliente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    cliente = Cliente(nombre,apellido,rut,fecha_nacimiento,direccion,telefono,correo)
    agregar_cliente_db(cliente)

def buscar_cliente():
    rut = input("Ingrese el rut del cliente a buscar: ")
    rut_buscar = buscar_cliente_db(rut)
    if rut_buscar:
        print("El cliente existe")
        print(f"Rut: {rut_buscar.get_rut()}")
        print(f"Nombres: {rut_buscar.get_nombres()}")
        print(f"Apellidos: {rut_buscar.get_apellidos()}")
    else:
        print("No se encontro el rut")
    return rut_buscar

def modificar_cliente():
    try:
        rut_cliente=input("Ingrese el rut del cliente que desea editar: ")
        cliente=buscar_cliente_db(rut_cliente)
        if not cliente:
            print("No se encontro el cliente con ese rut")
            return
        
        print(f"Cliente encontrado:ID: {cliente.get_id()},Nombre: {cliente.get_nombres()},Apellido: {cliente.get_apellidos()},Rut: {cliente.get_rut(),}"
              f"Fecha Nacimiento: {cliente.get_fecha_nacimiento()},Direccion: {cliente.get_direccion()},Telefono: {cliente.get_telefono()},Correo: {cliente.get_correo()}")
        nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del cliente: ")
        nuevo_rut = input("Ingrese el nuevo RUT del cliente: ")
        nuevo_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del cliente (YYYY/MM/DD), presione Enter para mantener el actual): ")
        nueva_direccion = input("Ingrese la nueva dirección del cliente (presione Enter para mantener la actual):")
        nuevo_telefono = input("Ingrese el nuevo teléfono del cliente (presione Enter para mantener el actual:")
        nuevo_correo = input("Ingrese el nuevo correo del cliente (presione Enter para mantener el actual:")

        if nuevo_nombre:
            cliente.set_nombres(nuevo_nombre)
        if nuevo_apellido:
            cliente.set_apellidos(nuevo_apellido)
        if nuevo_rut:
            cliente.set_rut(nuevo_rut)
        if nuevo_fecha_nacimiento:
            cliente.set_fecha_nacimiento(nuevo_fecha_nacimiento)
        if nueva_direccion:
            cliente.set_direccion(nueva_direccion)
        if nuevo_telefono:
            cliente.set_telefono(nuevo_telefono)
        if nuevo_correo:
            cliente.set_correo(nuevo_correo)
    
        editar_cliente_db(cliente)
    except ValueError:
        print("Error al editar el cliente")
    except Exception as e:
        print(f"Error al editar el cliente: {e}")
    
def eliminar_cliente():
    rut = input("Ingrese el rut del cliente a eliminar: ")
    cliente = buscar_cliente_db(rut)
    if cliente is not None:
        print("Cliente Encontrado:")
        print(f"Nombre:{cliente.get_nombre()}")
        print(f"Apellido:{cliente.get_apellido()}")
        print(f"Rut:{cliente.get_rut()}")
        print(f"Fecha Nacimiento:{cliente.get_fecha_nacimiento()}")
        print(f"Direccion:{cliente.get_direccion()}")
        print(f"Telefono:{cliente.get_telefono()}")
        print(f"Correo:{cliente.get_correo()}")

        confirmacion = input("¿Desea eliminar el cliente? (s/n): ")
        if confirmacion.lower() == "s":
            eliminar_cliente_db(cliente)
        else:
            print("Eliminacion cancelada")
    else:
        print("Cliente no encontrado")
