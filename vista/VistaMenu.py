from vista.VistaBebidas import menu_bebidas
from vista.VistaClientes import menu_clientes
from vista.VistaPedidos import menu_pedidos
from vista.VistaVendedores import menu_vendedores
from vista.VistaVentas import menu_ventas
import os


def limpiar_consola():
    os.system('cls')

def mostrar_menu_principal():
    limpiar_consola()
    print("🛒  ##### Menú Principal #####  🛒")
    print("\n📌  Elija una opción:")
    print("1️⃣  👥  Menú Clientes")
    print("2️⃣  🍹  Menú Bebidas")
    print("3️⃣  🏪  Menú Vendedor")
    print("4️⃣  📦  Menú Pedido")
    print("5️⃣  💰  Menú Ventas")
    print("===============================")
    
    opcion = input("🔍  Ingrese una opción: ")
    return int(opcion)

    
def iniciar_menu():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == 1:
            menu_clientes()
        elif opcion == 2:
            menu_bebidas()
        elif opcion == 3:
            menu_vendedores()
        elif opcion == 4:
            menu_pedidos()
        elif opcion == 5:
            menu_ventas()    
        else:
            print("Opción no válida, intente de nuevo.")
 