from modelo.BebidaSQL import Bebida
from controlador.ControladorBebida import agregar_bebida_db, buscar_bebida_db, editar_bebida_db, eliminar_bebida_db


def menu_bebidas():
    while True:
        print("Menu bebidas")
        print("1.- Ingresar ")
        print("2.- Buscar")
        print("3.- Modificar")
        print("4.- Eliminar")
        print("5.- Volver al Menú Principal")
        print("=========================")

        opcion = input("=====Elija una opción====")
        if opcion == "1":
            agregar_bebida()
        elif opcion == "2":
            buscar_bebida()
        elif opcion == "3":
            modificar_bebida()
        elif opcion == "4":
            eliminar_bebida()  
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")         

def agregar_bebida():
    nombre = input("Ingrese el nombre de la bebida: ")  
    precio = input("Ingrese el precio de la bebida: ")
    categoria = input("Ingrese la categoria de la bebida: ")
    descripcion = input("Ingrese la descripcion de la bebida: ")
    cantidad = input("Ingrese la cantidad de la bebida: ")
    print("Bebida ingresada con exito")
    bebida = Bebida(nombre, precio, categoria, descripcion, cantidad)
    agregar_bebida_db(bebida)

def buscar_bebida():
    nombre_bebida = input("Ingrese nombre de la bebida")
    buscar_bebida = buscar_bebida_db(nombre_bebida)
    if buscar_bebida:
        print("Bebida encontrada")
        print(nombre_bebida)
    else:
        print("No se encontró Bebida ingresada")    

def modificar_bebida():
    print("=====Editar Bebida=====")
    try:
        nombre_bebida = input("Ingrese el  nombre de la Bebida a modificar: ")
        bebida = buscar_bebida_db(nombre_bebida)
        if not bebida:
            print("No se encontró bebida con ese nombre ")
            return 
        
        print(f"Bebida encontrada: ID: {bebida.get_id()}, Nombre: {bebida.get_nombre()}, Precio: {bebida.get_precio()}, Categoria: {bebida.get_categoria()}, "
            f"Descripcion: {bebida.get_descripcion()}, Cantidad: {bebida.get_cantidad()} ")        
        
        nuevo_nombre = input("Ingrese nuevo nombre: ") 
        nuevo_precio = input("Ingrese el nuevo precio de la bebida, presione Enter para mantener el actual: ")
        nueva_categoria = input("Ingrese la nueva categoria de la bebida, presione Enter para mantener el actual: ")
        nueva_descripcion = input("Ingrese la nueva descripcion de la bebida, presione Enter para mantener el actual: ")
        nueva_cantidad = input("Ingrese la nueva cantidad de la bebida, presione Enter para mantener el actual: ")

        if nuevo_nombre:
            bebida.set_nombre(nuevo_nombre)
        if nuevo_precio:
            bebida.set_precio(nuevo_precio)
        if nueva_categoria:
            bebida.set_categoria(nueva_categoria)
        if nueva_descripcion:
            bebida.set_descripcion(nueva_descripcion)
        if nueva_cantidad:
            bebida.set_cantidad(nueva_cantidad)  
        
        editar_bebida_db(bebida)
    except ValueError:
        print("Error: Por favor ingrese valores válidos. ")
    except Exception as e:
        print(f"Error al editar bebida: {e}")                



def eliminar_bebida():
    print("____Eliminar bebida____")
    nombre = input("Ingrese el nombre del bebida: ")
    bebida = buscar_bebida(nombre)  # Método en controlador_bebida
    if bebida is not None:
        print("bebida encontrado:")
        print(f"Nombre: {bebida.get_nombre()}")
        print(f"Precio: {bebida.get_precio()}")
        print(f"Categoria: {bebida.get_categoria()}")
        print(f"Descripción: {bebida.get_descripcion()}")
        print(f"Cantidad: {bebida.get_cantidad()}")

        
        confirmacion = input("¿Está seguro de que desea eliminar esta bebida? (s/n): ")
        if confirmacion.lower() == 's':
            eliminar_bebida_db(bebida)  # Método en controlador_bebida para eliminar
        else:
            print("Eliminación cancelada")
    else:
        print("bebida no encontrada")
        