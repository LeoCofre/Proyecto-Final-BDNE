from controlador.ControladorVendedor import agregar_vendedor_db, buscar_vendedor_db, editar_vendedor_db, eliminar_vendedor_db
from modelo.VendedorSQL import Vendedor

def menu_vendedores():
    while True:
        print("\n===== Menú Vendedores =====")
        print("1.- Ingresar")
        print("2.- Buscar")
        print("3.- Modificar")
        print("4.- Eliminar")
        print("5.- Volver al Menú Principal")
        print("=========================")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ingresar_vendedor()
        elif opcion == "2":
            buscar_vendedor()
        elif opcion == "3":
            editar_vendedor()
        elif opcion == "4":
            eliminar_vendedor()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


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
    rut = input("Ingrese el rut del vendedor a buscar: ")
    rutbuscar = buscar_vendedor_db(rut)
    if rutbuscar:
        print("El vendedor existe")
        print(rut)
    else:
        print("No se encontro el rut")
    return rutbuscar

def editar_vendedor():
    try:
        nombre_vendedor=input("Ingrese el nombre del vendedor que desea editar: ")
        vendedor=buscar_vendedor_db(nombre_vendedor)
        if not vendedor:
            print("No se encontro el vendedor con ese nombre")
            return
        
        print(f"vendedor encontrado:ID: {vendedor.get_id_vendedor()},Nombre: {vendedor.get_nombres()},Apellido: {vendedor.get_apellidos()},Rut: {vendedor.get_rut(),}"
              f"Fecha Nacimiento: {vendedor.get_fecha_nacimiento()},Direccion: {vendedor.get_direccion()},Telefono: {vendedor.get_telefono()},Correo: {vendedor.get_correo()}")
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
