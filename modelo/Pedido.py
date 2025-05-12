class Pedido:
    def __init__(self, fecha, id_cliente, nombre_cliente, telefono, correo, id_vendedor, nombre_vendedor, estado, id_bebida, nombre_bebida, cantidad, precio_unitario):
        self.__id_pedido = 0
        self.__fecha = fecha
        self.__id_cliente = id_cliente
        self.__nombre_cliente = nombre_cliente
        self.__telefono = telefono
        self.__correo = correo
        self.__id_vendedor = id_vendedor
        self.__nombre_vendedor = nombre_vendedor
        self.__estado = estado
        self.__id_bebida = id_bebida
        self.__nombre_bebida = nombre_bebida
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario

       

    # Getters
    def get_id_pedido(self):
        return self.__id_pedido

    def get_fecha(self):
        return self.__fecha

    def get_id_cliente(self):
        return self.__id_cliente
    
    def get_nombre_cliente(self):
        return self.__nombre_cliente
    
    def get_telefono(self):
        return self.__telefono
    
    def get_correo(self):
        return self.__correo
    
    def get_id_vendedor(self):
        return self.__id_vendedor
    
    def get_nombre_vendedor(self):
        return self.__nombre_vendedor
    
    def get_estado(self):
        return self.__estado
    
    def get_id_bebida(self):
        return self.__id_bebida
    
    def get_nombre_bebida(self):
        return self.__nombre_bebida
    
    def get_cantidad(self):
        return self.__cantidad
    
    def get_precio_unitario(self):
        return self.__precio_unitario
    
    # Setters
    def set_id_pedido(self, id_pedido):
        self.__id_pedido = id_pedido

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def set_nombre_cliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_correo(self, correo):
         self.__correo = correo

    def set_id_vendedor(self, id_vendedor):
        self.__id_vendedor = id_vendedor

    def set_nombre_vendedor(self, nombre_vendedor):
        self.__nombre_vendedor = nombre_vendedor

    def set_estado(self, estado):
        self.__estado = estado

    def set_id_bebida(self, id_bebida):
        self.__id_bebida = id_bebida

    def set_nombre_bebida(self, nombre_bebida):
        self.__nombre_bebida = nombre_bebida

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio_unitario(self, precio_unitario):
        self.__precio_unitario = precio_unitario


    # Método tipo toString (representación del objeto)
    def __str__(self):
        return f"Pedido(id_pedido={self.__id_pedido},\nFecha='{self.__fecha}',\nid_cliente={self.__id_cliente},\nNombre_cliente='{self.__nombre_cliente}',\nTeléfono='{self.__telefono}',\nCorreo='{self.__correo}',\nId_vendedor={self.__id_vendedor},\nNombre_vendedor='{self.__nombre_vendedor}',\nEstado='{self.__estado}',\nId_bebida={self.__id_bebida},\nNombre_bebida={self.__nombre_bebida},\nCantidad={self.__cantidad},\nPrecio_unitario={self.__precio_unitario})"