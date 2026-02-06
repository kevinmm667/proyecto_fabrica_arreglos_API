class Maquina_modelo:
    def __init__(self, codigo, nombre, modelo, estado):
        self.codigo_maquina = codigo
        self.nombre_maquina = nombre
        self.modelo_maquina = modelo
        self.estado_maquina = estado
        
    def set_codigo(self, nuevo_codigo):
        self.codigo_maquina = nuevo_codigo
    def get_codigo(self):
        return self.codigo_maquina
    
    def set_nombre(self, nuevo_nombre):
        self.nombre_maquina = nuevo_nombre
    def get_nombre(self):
        return self.nombre_maquina
    
    def set_modelo(self, nuevo_modelo):
        self.modelo_maquina = nuevo_modelo
    def get_modelo(self):
        return self.modelo_maquina
    
    def set_estado(self, nuevo_estado):
        self.estado_maquina = nuevo_estado
    def get_estado(self):
        return self.estado_maquina
    
    def ver_info(self):
        infor="codigo: " + self.codigo_maquina + ", nombre: " + self.nombre_maquina
        infor = infor + " modelo: " + self.modelo_maquina + ", estado: " + self.estado_maquina 
        return infor