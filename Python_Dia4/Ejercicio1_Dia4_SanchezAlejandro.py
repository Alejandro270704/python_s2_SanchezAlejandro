
#ejercicio 1 dia 4#
import json
from funciones import agregarUsuario,informe
def lista_json(Datos_json):
    with open(Datos_json, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

lista_usuarios=lista_json("Datos.json")
contador=True
lista_usuarios=[]
while contador==True:
    
    print ("digita la opcion ")
    print ("1.crear artista  ")
    print ("2. informe de reportes")
    print ("3.modulo de reportes ")
    print ("4.salir del programa")
    opc=int(input())
    if opc==1 :
        nuevousario=agregarUsuario(1)
        lista_usuarios.append(nuevousario)
        print ("se ha creado el artista")
        
    elif opc==2:
       reporte=informe()
       
    elif opc ==4 :
        contador=False
    else :
        print ("esta opcion no existe ")


       
       
        
        
        
        
    
 