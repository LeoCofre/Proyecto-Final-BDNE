class Venta:
    def __init__(self, id_venta, fecha, id_cliente, nombre_cliente, id_vendedor, nombre_vendedor, total, productos):
        self.id_venta = id_venta 
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.id_vendedor = id_vendedor
        self.nombre_vendedor = nombre_vendedor
        self.total = total
        self.productos = productos  

    def to_dict(self):
        #Convierte la venta en un diccionario para MongoDB.
        return {
            "id_venta": self.id_venta,
            "fecha": self.fecha,
            "cliente": {
                "id_cliente": self.id_cliente,
                "nombre_cliente": self.nombre_cliente
            },
            "vendedor": {
                "id_vendedor": self.id_vendedor,
                "nombre_vendedor": self.nombre_vendedor
            },
            "total": self.total,
            "productos": self.productos  
        }
