from controlador.ControladorCliente import agregar_cliente_db, buscar_cliente_db, eliminar_cliente_db, editar_cliente_db, listar_clientes_db
from modelo.ClienteSQL import Cliente

def menu_clientes():
    while True:
        print("\n👥  ===== Menú Clientes =====  👥")
        print("1️⃣  ➕  Agregar Cliente")
        print("2️⃣  🔍  Buscar Cliente")
        print("3️⃣  📜  Mostrar Clientes")
        print("4️⃣  ✏️  Modificar Cliente")
        print("5️⃣  ❌  Eliminar Cliente")
        print("6️⃣  🔙  Volver al Menú Principal")
        print("===============================")

        opcion = input("🔍  Ingrese una opción: ")

        if opcion == "1":
            ingresar_cliente()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            mostrar_clientes()
        elif opcion == "4":
            modificar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            return   
        else:
            print("⚠️  Opción no válida. Intente de nuevo.")


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
    rut = input("🔍  Ingrese el RUT del cliente a buscar: ")
    rut_buscar = buscar_cliente_db(rut)
    
    if rut_buscar:
        print("\n✅  Cliente encontrado:")
        print("🆔  RUT:", rut_buscar.get_rut())
        print("📝  Nombre:", rut_buscar.get_nombres(), rut_buscar.get_apellidos())  # Nombre y apellido juntos
        print("───────────────────────")
    else:
        print("⚠️  No se encontró el cliente con ese RUT.")

    return rut_buscar

 

def mostrar_clientes():
    print("\n👥  --- Listado de Clientes ---  👥")
    clientes = listar_clientes_db()

    if isinstance(clientes, list):
        for cliente in clientes:
            print("\n📌  ID Cliente:", cliente[0])
            print("📝  Nombre:", cliente[1], cliente[2])  # Nombre y apellido juntos
            print("🆔  RUT:", cliente[3])
            print("📞  Teléfono:", cliente[4])
            print("📧  Correo:", cliente[5])
            print("───────────────────────")
    else:
        print("⚠️  No hay clientes registrados.")

    return

def modificar_cliente():
    try:
        rut_cliente=input("Ingrese el rut del cliente que desea editar: ")
        cliente=buscar_cliente_db(rut_cliente)
        if not cliente:
            print("No se encontro el cliente con ese rut")
            return
        print("\n=== Cliente Encontrado ===")
        print(f"ID Cliente: {cliente.get_id_cliente()}")
        print(f"Nombre: {cliente.get_nombres()}")
        print(f"Apellido: {cliente.get_apellidos()}")
        print(f"Rut: {cliente.get_rut()}")
        print(f"Fecha de Nacimiento: {cliente.get_fecha_nacimiento()}")
        print(f"Dirección: {cliente.get_direccion()}")
        print(f"Teléfono: {cliente.get_telefono()}")
        print(f"Correo: {cliente.get_correo()}\n")  
        
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
        print(f"Nombre:{cliente.get_nombres()}")
        print(f"Apellido:{cliente.get_apellidos()}")
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
