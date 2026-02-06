class Api_BD:
    def __init__(self):
      self.Api_datos = []
      
    def guardar_empleado(self,obj_nuevo_empleado):
        self.Api_datos.append(obj_nuevo_empleado)
        
    def imprimir_Api(self):
        for empleado in self.Api_datos:
            print(empleado)        
    
    def eliminar_empleado(self,obj_empleado):
        self.Api_datos.pop(obj_empleado)
        
    def agregar_elemen_lista(self,obj_nuevo_elemento):
        self.Api_datos.extend(obj_nuevo_elemento)
    