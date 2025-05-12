from vista.Bebidas import menu_Bebidas
from vista.Clientes import menu_Clientes
from vista.Pedido import menu_Pedido
from vista.Vendedores import menu_vendedor
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
    print("===========================")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def iniciar_menu(usuario):
    while True:
        opcion = mostrar_menu_principal()
        if opcion == 1:
            menu_Clientes()
        elif opcion == 2:
            menu_Bebidas()
        elif opcion == 3:
            menu_vendedor()
        elif opcion == 4:
            menu_Pedido()
        elif opcion == 6:
            mostrar_menu(usuario)
        else:
            print("Opción no válida, intente de nuevo.")
