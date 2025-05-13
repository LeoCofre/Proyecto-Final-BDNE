class Bebida:
    def __init__(self, nombre, precio, categoria, descripcion, cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__id = 0

#Getters
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_categoria(self):
        return self.__categoria

    def get_descripcion(self):
        return self.__descripcion

    def get_cantidad(self):
        return self.__cantidad

    def get_id(self):
        return self.__id

#Setters

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        self.__precio = precio

    def set_categoria(self, categoria):
        self.__categoria = categoria 

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_id(self,id):
        self.__id=id

#ToString
def __str__(self):
    return f"Nombre: {self.__nombre}\nPrecio: {self.__precio},\nCategoria:{self.__categoria}\nDescripción : {self.__descripcion}\nCantidad: {self.__cantidad}"