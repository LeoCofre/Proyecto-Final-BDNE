from controlador.ControladorVendedor import agregar_vendedor_db, buscar_vendedor_db, editar_vendedor_db, eliminar_vendedor_db, listar_vendedores_db
from modelo.VendedorSQL import Vendedor

def menu_vendedores():
    while True:
        print("\n🏪  ===== Menú Vendedores =====  🏪")
        print("1️⃣  ➕  Agregar Vendedor")
        print("2️⃣  🔍  Buscar Vendedor")
        print("3️⃣  📜  Mostrar Vendedores")
        print("4️⃣  ✏️  Modificar Vendedor")
        print("5️⃣  ❌  Eliminar Vendedor")
        print("6️⃣  🔙  Volver al Menú Principal")
        print("===============================")

        opcion = input("🔍  Ingrese una opción: ")

        if opcion == "1":
            ingresar_vendedor()
        elif opcion == "2":
            buscar_vendedor()
        elif opcion == "3":
            mostrar_vendedores()
        elif opcion == "4":
            editar_vendedor()
        elif opcion == "5":
            eliminar_vendedor()
        elif opcion == "6":
            return  
        else:
            print("⚠️  Opción no válida. Intente de nuevo.")



def ingresar_vendedor():
    nombre = input("Ingrese el nombre del vendedor: ")
    apellido = input("Ingrese el apellido del vendedor: ")
    rut = input("Ingrese el RUT del vendedor: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del vendedor: ")
    direccion = input("Ingrese la dirección del vendedor: ")
    telefono = input("Ingrese el teléfono del vendedor: ")
    correo = input("Ingrese el correo del vendedor: ")
    vendedor = Vendedor(nombre,apellido,rut,fecha_nacimiento,direccion,telefono,correo)
    agregar_vendedor_db(vendedor)

def buscar_vendedor():
    rut = input("🔍  Ingrese el RUT del vendedor a buscar: ")
    vendedor_encontrado = buscar_vendedor_db(rut)
    
    if vendedor_encontrado:
        print("\n✅  Vendedor encontrado:")
        print("🆔  RUT:", vendedor_encontrado.get_rut())
        print("📝  Nombre:", vendedor_encontrado.get_nombres(), vendedor_encontrado.get_apellidos())  # Nombre y apellido juntos
        print("───────────────────────")
    else:
        print("⚠️  No se encontró el vendedor con ese RUT.")

    return vendedor_encontrado

 

def mostrar_vendedores():
    print("\n🏪  --- Listado de Vendedores ---  🏪")
    vendedores = listar_vendedores_db()

    if isinstance(vendedores, list):
        for vendedor in vendedores:
            print("\n📌  ID Vendedor:", vendedor[0])
            print("📝  Nombre:", vendedor[1], vendedor[2])  # Nombre y apellidos juntos
            print("🆔  RUT:", vendedor[3])
            print("📞  Teléfono:", vendedor[4])
            print("📧  Correo:", vendedor[5])
            print("───────────────────────")
    else:
        print("⚠️  No hay vendedores registrados.")

    return



def editar_vendedor():
    try:
        nombre_vendedor=input("Ingrese el rut del vendedor que desea editar: ")
        vendedor=buscar_vendedor_db(nombre_vendedor)
        if not vendedor:
            print("No se encontro el vendedor con ese rut")
            return
        
        print("\n=== Vendedor Encontrado ===")
        print(f"ID: {vendedor.get_id_vendedor()}")
        print(f"Nombre: {vendedor.get_nombres()}")
        print(f"Apellido: {vendedor.get_apellidos()}")
        print(f"Rut: {vendedor.get_rut()}")
        print(f"Fecha de Nacimiento: {vendedor.get_fecha_nacimiento()}")
        print(f"Dirección: {vendedor.get_direccion()}")
        print(f"Teléfono: {vendedor.get_telefono()}")
        print(f"Correo: {vendedor.get_correo()}\n")  

        nuevo_nombre = input("Ingrese el nuevo nombre del vendedor: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del vendedor: ")
        nuevo_rut = input("Ingrese el nuevo RUT del vendedor: ")
        nuevo_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del vendedor (YYYY/MM/DD), presione Enter para mantener el actual): ")
        nueva_direccion = input("Ingrese la nueva dirección del vendedor (presione Enter para mantener la actual):")
        nuevo_telefono = input("Ingrese el nuevo teléfono del vendedor (presione Enter para mantener el actual:")
        nuevo_correo = input("Ingrese el nuevo correo del vendedor (presione Enter para mantener el actual:")

        if nuevo_nombre:
            vendedor.set_nombres(nuevo_nombre)
        if nuevo_apellido:
            vendedor.set_apellidos(nuevo_apellido)
        if nuevo_rut:
            vendedor.set_rut(nuevo_rut)
        if nuevo_fecha_nacimiento:
            vendedor.set_fecha_nacimiento(nuevo_fecha_nacimiento)
        if nueva_direccion:
            vendedor.set_direccion(nueva_direccion)
        if nuevo_telefono:
            vendedor.set_telefono(nuevo_telefono)
        if nuevo_correo:
            vendedor.set_correo(nuevo_correo)
    
        editar_vendedor_db(vendedor)
    except ValueError:
        print("Error al editar el vendedor")
    except Exception as e:
        print(f"Error al editar el vendedor: {e}")
    
def eliminar_vendedor():
    rut = input("Ingrese el rut del vendedor a eliminar: ")
    vendedor = buscar_vendedor_db(rut)
    if vendedor is not None:
        print("vendedor Encontrado:")
        print(f"Nombre:{vendedor.get_nombres()}")
        print(f"Apellido:{vendedor.get_apellidos()}")
        print(f"Rut:{vendedor.get_rut()}")
        print(f"Fecha Nacimiento:{vendedor.get_fecha_nacimiento()}")
        print(f"Direccion:{vendedor.get_direccion()}")
        print(f"Telefono:{vendedor.get_telefono()}")
        print(f"Correo:{vendedor.get_correo()}")

        confirmacion = input("¿Desea eliminar el vendedor? (s/n): ")
        if confirmacion.lower() == "s":
            eliminar_vendedor_db(vendedor)
        else:
            print("Eliminacion cancelada")
    else:
        print("vendedor no encontrado")
