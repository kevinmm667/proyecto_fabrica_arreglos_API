class Api_BD_maquinas:
    def __init__(self):
        self.Api_maquina = [
            [ "codigo","nombre","Modelo","Estado"],
            ["COD8974", "brazo mecanico","MZ002","apagada"],
            ["COD3423","cinta transportadora","M23X","mantenimiento"],
            ["COD4324", "elevador","LL90","Encendida"]
        ]
#metodos
   
    def imprimir_info(self):
        for i in range(len(self.Api_maquina)):
            print(self.Api_maquina[i])
    
    def buscar_info(self):
        return self.Api_maquina[2][2] 
    
    def agregar_info (self, nueva_maquina):
        self.Api_maquina.append(nueva_maquina)
        
    def agregar_infos (self, agregar_elementos):
        self.Api_maquina.extend(agregar_elementos)
           
    def insertar_info(self, insertar_nuevo_elemen):
        self.Api_maquina.insert(3,insertar_nuevo_elemen)
        
    def eliminar_elemento(self, remover_maquina):
        self.Api_maquina.remove(remover_maquina)
        
    def remover_elemento(self, quitar_elemento):
        self.Api_maquina.pop(quitar_elemento)

        
    def contar_elemento(self, contar_info):
        return self.Api_maquina.count(contar_info)