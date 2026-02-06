from empleado_modelo import Empleado_modelo 
from base_datos import Api_BD
from api_BD_maquinas import Api_BD_maquinas
from maquina_modelo import Maquina_modelo

# codigo principal 
obj_Api = Api_BD()
obj_Api_maquina = Api_BD_maquinas()
print(obj_Api_maquina.buscar_info())

#objetos

nueva_maquina = ["COD4563","prensa hidraulica","JH777","reparacion"]
obj_Api_maquina.agregar_info(nueva_maquina)

agregar_elementos = [
                        ["COD3344","cierra electrica","KO999","apagada"],
                        ["COD2637","cuchilla","GF666","dañada"]
]                       
obj_Api_maquina.agregar_infos(agregar_elementos)

insertar_nuevo_elemen = ["COD7777","martillo","JJS2","funcionando"]
obj_Api_maquina.insertar_info(insertar_nuevo_elemen)

remover_maquina = ["COD4563","prensa hidraulica","JH777","reparacion"]
obj_Api_maquina.eliminar_elemento(remover_maquina)

quitar_elemento = 2
obj_Api_maquina.remover_elemento(quitar_elemento)


contar_info = obj_Api_maquina.contar_elemento("KO999")
print (contar_info)




obj_Api_maquina.imprimir_info()



obj_Empleado = Empleado_modelo("kevin","sanchez","1092049876","313-6476354")
obj_Empleado2 = Empleado_modelo("Mia","castrillon","1098998765","311-6253789")
obj_Empleado3 = Empleado_modelo("Emily","Lopez","1081273689","310-16283098")

obj_Api.guardar_empleado(obj_Empleado)
obj_Api.guardar_empleado(obj_Empleado2)
obj_Api.guardar_empleado(obj_Empleado3)
obj_Api.imprimir_Api()
