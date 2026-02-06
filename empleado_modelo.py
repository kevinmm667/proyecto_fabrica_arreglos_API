class Empleado_modelo:
    
    def __init__(self, nombre, apellido, cedula, celular):
        self.nombre_empleado = nombre
        self.apellido_empleado = apellido
        self.cedula_empleado = cedula
        self.celular_empleado = celular
           
    def set_nombre(self,nuevo_nombre):
        self.nombre_empleado = nuevo_nombre
            
    def get_nombre(self):
        return self.nombre_empleado    
        
    def set_apellido(self,nuevo_apellido):
        self.apellido_empleado = nuevo_apellido
    
    def get_apellido(self):
        return self.apellido_empleado   
      
    def set_cedula(self,nueva_cedula):
        self.cedula_empleado = nueva_cedula
        
    def get_cedula(self):
        return self.cedula_empleado
     
    def set_celular(self,nuevo_celular):
        self.celular_empleado = nuevo_celular
    
    def get_celular(self):
        return self.celular_empleado
    
    def ver_infor(self):
        info= "nombre empleado: " + self.nombre_empleado + ", apellido empleado: " + self.apellido_empleado   
        info= info + " cedula del empleado: " + self.cedula_empleado + ", celular del empleado: " + self.celular_empleado 
        return info 