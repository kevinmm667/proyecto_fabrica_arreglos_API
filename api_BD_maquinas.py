class Api_BD_maquinas:
    def __init__(self):
        self.Api_maquina = [
            [ "codigo","nombre maquina","Modelo Maquina","Estado maquina"],
            ["COD8974", "brazo mecanico","MZ002","apagada"],
            ["COD3423","cinta transportadora","M23X","mantenimiento"],
            ["COD4324", "elevador","LL90","Encendida"]
        ]
        
    def imprimir_info(self):
        for i in range(len(self.Api_maquina)):
            print(self.Api_maquina[i])
    
    def buscar_info(self):
        return self.Api_maquina[2][2] 
    
    def agregar_info (self, nueva_maquina):
        self.Api_maquina.append(nueva_maquina)
        
    def agregar_infos (self, agregar_elementos):
        self.Api_maquina.extend(agregar_elementos)
           
    def insertar_info(self,posicion, insertar_nuevo_elemen):
        self.Api_maquina.insert(posicion,insertar_nuevo_elemen)