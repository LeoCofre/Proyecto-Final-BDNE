class Pedido:
    def __init__(self, id_pedido, fecha, id_cliente, nombre_cliente, telefono, correo, id_vendedor, nombre_vendedor, estado, id_bebida, nombre_bebida, cantidad, precio_unitario):
        self.id_pedido = id_pedido  # Ahora lo ingresará manualmente el usuario
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.telefono = telefono
        self.correo = correo
        self.id_vendedor = id_vendedor
        self.nombre_vendedor = nombre_vendedor
        self.estado = estado
        self.id_bebida = id_bebida
        self.nombre_bebida = nombre_bebida
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def to_dict(self):
        """Convierte el objeto Pedido en un diccionario compatible con MongoDB."""
        return {
            "id_pedido": self.id_pedido,  # Guardamos el ID manualmente
            "fecha": self.fecha,
            "cliente": {
                "id_cliente": self.id_cliente,
                "nombre_cliente": self.nombre_cliente,
                "telefono": self.telefono,
                "correo": self.correo
            },
            "vendedor": {
                "id_vendedor": self.id_vendedor,
                "nombre_vendedor": self.nombre_vendedor
            },
            "estado": self.estado,
            "detalles": {
                "id_bebida": self.id_bebida,
                "nombre_bebida": self.nombre_bebida,
                "cantidad": self.cantidad,
                "precio_unitario": self.precio_unitario
            }
        }
