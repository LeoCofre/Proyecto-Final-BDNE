from modelo.Venta import Venta
from controlador.ControladorVenta import agregar_venta_db, buscar_venta_db, editar_venta_db, eliminar_venta_db, listar_ventas_db

def menu_ventas():
    while True:
        print("\n💰  ===== Menú Ventas =====  💰")
        print("1️⃣  ➕  Registrar Venta")
        print("2️⃣  🔍  Buscar Venta")
        print("3️⃣  📜  Mostrar Ventas")
        print("4️⃣  ✏️  Modificar Venta")
        print("5️⃣  ❌  Eliminar Venta")
        print("6️⃣  🔙  Volver al Menú Principal")
        print("===============================")

        opcion = input("🔍  Ingrese una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            buscar_venta()
        elif opcion == "3":
            mostrar_ventas()
        elif opcion == "4":
            modificar_venta()
        elif opcion == "5":
            eliminar_venta()
        elif opcion == "6":
            return  # 🔙 Permite regresar correctamente sin quedar atrapado en el menú
        else:
            print("⚠️  Opción no válida. Intente de nuevo.")


        
def registrar_venta():
    id_venta = input("Ingrese el ID de la venta: ")  # ID manual, igual que pedidos
    fecha = input("Ingrese la fecha de la venta: ")
    id_cliente = input("Ingrese el ID del cliente: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    id_vendedor = input("Ingrese el ID del vendedor: ")
    nombre_vendedor = input("Ingrese el nombre del vendedor: ")
    total = int(input("Ingrese el total de la venta: "))  # Ahora es entero

    productos = []
    while True:
        nombre_producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre_producto.lower() == "fin":
            break
        cantidad = int(input(f"Ingrese la cantidad de {nombre_producto}: "))
        precio_unitario = int(input(f"Ingrese el precio unitario de {nombre_producto}: "))  # Ahora es entero
        productos.append({"nombre_producto": nombre_producto, "cantidad": cantidad, "precio_unitario": precio_unitario})

    venta = Venta(id_venta, fecha, id_cliente, nombre_cliente, id_vendedor, nombre_vendedor, total, productos)
    
    agregar_venta_db(venta)

    print("\n Venta registrada con éxito.")
    menu_ventas()  # Vuelve al menú automáticamente


def buscar_venta():
    print("\n💰  --- Buscar Venta ---  💰")
    id_venta = input("🔍  Ingrese el ID de la venta a buscar: ")
    venta = buscar_venta_db(id_venta)

    if venta and isinstance(venta, dict):
        print("\n✅  Venta encontrada:")
        print("📅  Fecha:", venta["fecha"])
        print("👤  Cliente:", venta["cliente"]["nombre_cliente"], "| ID:", venta["cliente"]["id_cliente"])
        print("🏪  Vendedor:", venta["vendedor"]["nombre_vendedor"], "| ID:", venta["vendedor"]["id_vendedor"])
        print("💲  Total Venta: $", venta["total"])
        
        print("\n🛍️  Productos:")
        for producto in venta["productos"]:
            print(f"📦  {producto['nombre_producto']} | 🛒 Cantidad: {producto['cantidad']} | 💰 Precio: ${producto['precio_unitario']}")
        print("───────────────────────")
    else:
        print("⚠️  No se encontró la venta en la base de datos.")

    return


 

def mostrar_ventas():
    print("\n💰  --- Listado de Ventas ---  💰")
    ventas = listar_ventas_db()

    if isinstance(ventas, list):
        for venta in ventas:
            print("\n📌  ID Venta:", venta["id_venta"])
            print("📅  Fecha:", venta["fecha"])
            print("👤  Cliente:", venta["cliente"]["nombre_cliente"])
            print("💲  Total: $", venta["total"])
            print("\n🛍️  Productos:")
            for producto in venta["productos"]:
                print(f"📦  {producto['nombre_producto']} | 🛒 Cantidad: {producto['cantidad']} | 💰 Precio: ${producto['precio_unitario']}")
            print("───────────────────────")
    else:
        print("⚠️  No hay ventas registradas.")

    return

    

def modificar_venta():
    try:
        id_venta = input("Ingrese el ID de la venta que desea editar: ")
        venta = buscar_venta_db(id_venta)

        if not venta or not isinstance(venta, dict):
            print(" No se encontró una venta con ese ID.")
            return

        print("\nVenta encontrada:")
        print(f"Fecha: {venta['fecha']}")
        print(f"Total actual: {venta['total']}")

        nuevo_total = input("Ingrese el nuevo total de la venta (Enter para mantener): ")

        cambios = {}
        if nuevo_total:
            cambios["total"] = int(nuevo_total)

        if cambios:
            editar_venta_db(id_venta, cambios)
            print(" Venta modificada exitosamente.")
        else:
            print("No se realizó ninguna modificación.")

    except Exception as e:
        print(f" Error al editar la venta: {e}")
    menu_ventas()    


def eliminar_venta():
    try:
        id_venta = input("Ingrese el ID de la venta que desea eliminar: ")
        venta = buscar_venta_db(id_venta)

        if not venta:
            print(" No se encontró la venta.")
            return

        confirmar = input("¿Está seguro que desea eliminar esta venta? (s/n): ")

        if confirmar.lower() == 's':
            eliminar_venta_db(id_venta)
            print(" Venta eliminada exitosamente.")
        else:
            print("Operación cancelada.")

    except Exception as e:
        print(f" Error al eliminar la venta: {e}")
    return
