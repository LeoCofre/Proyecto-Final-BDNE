from vista.Bebidas import menu_bebidas

print("Menu Principal")
print("1.- Menu bebidad")
print("2.- Menu Clientes")
print("3.- Menu Vendedores")
print("4.- Menu Pedidos")

opcion = input("Elija una opción")
while True:
    if opcion == 1:
        menu_bebidas()
    elif opcion == 2:
        menu_clientes()
    elif opcion == 3:
        menu_vendedores()
    elif opcion == 4:
        menu_pedidos()       