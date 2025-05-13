from vista.Bebidas import menu_bebidas
from vista.Clientes import menu_clientes
from vista.Pedidos import menu_pedidos
from vista.Vendedores import menu_vendedores
from vista.Ventas import menu_ventas
import os


def limpiar_consola():
    os.system('cls')

def mostrar_menu_principal():
    limpiar_consola()
    print("##### Menu Principal ##### ")
    print("____Elija una opción____")
    print("1.- Menu Clientes")
    print("2.- Menu Bebidas")
    print("3.- Menu Vendedor")
    print("4.- Menu Pedido")
    print("5.- Menu Ventas ")
    print("===========================")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

    
def iniciar_menu():
    print("_____Aqui voy___")
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
 