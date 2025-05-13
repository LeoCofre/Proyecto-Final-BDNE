class Venta:
    def __init__(self, id_venta, fecha , id_pedido, id_cliente, nombre_cliente, total, medio_de_pago):
        self.__id_venta = id_venta
        self.__fecha = fecha
        self.__id_pedido = id_pedido
        self.__id_cliente = id_cliente
        self.__nombre_cliente = nombre_cliente
        self.__total = total
        self.__medio_de_pago = medio_de_pago

#Getters
    def get_id_venta(self):
        return self.__id_venta
    
    def get_fecha(self):
        return self.__fecha
    
    def get_id_pedido(self):
        return self.__id_pedido
    
    def get_id_cliente(self):
        return self.__id_cliente
    
    def get_nombre_cliente(self):
        return self.__nombre_cliente
    
    def get_total(self):
        return self.__total
    
    def get_medio_de_pago(self):
        return self.__medio_de_pago
    
#Setters

    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def set_nombre_cliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente

    def set_total(self,total):
        self.__total = total

    def set_medio_de_pago(self, medio_de_pago):
        self.__medio_de_pago = medio_de_pago

def __str___(self):
    return f"ID Venta: {self.__id_venta},\nFecha: {self.__fecha}, \nID Pedido: {self.__id_pedido},\nID Cliente: {self.__id}, \nNombre Cliente: {self.__nombre_cliente},\nTotal: {self.__total}, \nMedio de Pago: {self.__medio_de_pago}"
