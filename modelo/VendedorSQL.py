class Vendedor:
    def __init__(self,nombres,apellidos,rut,fecha_nacimiento,direccion,telefono,correo):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__rut = rut
        self.__fecha_nacimiento = fecha_nacimiento
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo
        self.__id_vendedor = 0
    
    def get_nombres(self):
        return self.__nombres
    def get_apellidos(self):
        return self.__apellidos
    def get_rut(self):
        return self.__rut
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono
    def get_correo(self):
        return self.__correo
    def get_id_vendedor(self):
        return self.__id_vendedor
    
    def set_nombres(self,nombres):
        self.__nombres = nombres

    def set_apellidos(self,apellidos):
        self.__apellidos = apellidos

    def set_rut(self,rut):
        self.__rut = rut

    def set_fecha_nacimiento(self,fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_direccion(self,direccion):
        self.__direccion = direccion
    
    def set_tefono(self,telefono):
        self.__telefono = telefono
    
    def set_correo(self,correo):
        self.__correo = correo
    
    def set_id_vendedor(self,id_vendedor):
        self.__id_vendedor = id_vendedor
    
    def __str__(self):
        return f"Nombres: {self.__nombres}\nApellidos: {self.__apellidos}\nRut: {self.__rut}\nFecha de Nacimiento: {self.__fecha_nacimiento}\nDireccion: {self.__direccion}\nTelefono: {self.__telefono}\nCorreo: {self.__correo}"