
# #### Clase Dia 6 ######
# ##########################
# Diccionarios
#Un DICccionario  es una colección de elementos , donde cada elementos insertado tiene una llave úntica, 
# la cual va acompañada de un valor 

##Diccionario con listas
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[{"codigo":57,"numero":3023019865,"tipo":"trabajo"}
                ,{"codigo":1,"numero":3983054625,"tipo":"personal"}]
}
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"}
                ,{"codigo":22,"numero":6857493658,"tipo":"personal"}]
}
listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)


booleanito = True
while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        numId=listaRobusta[len(listaRobusta)-1]["id"]+1
        diccionarioVacio={
            "id":numId,
            "nombre":input("nombre "),
            "apellido":input("apellido "),
            "edad":int(input("edad ")),
            
            "telefonos":[{"codigo":int(input("codigo ")),"numero":int(input("numero telefonico ")),"tipo":input(" trabajo o personal ")},
                    {"codigo":int(input("segundo codigo ")),"numero":int(input("numero telefonico dos ")),"tipo":input("trabajo o personal ")}]
            }
        listaRobusta.append(diccionarioVacio)
        
        

    
    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                
                print("---------------------------")
            
    elif(opcionUsuario==3):
        print ("    ####   elegir a una persona  ####  ")
        for i in range (len(listaRobusta)):
            print("Nombre:",listaRobusta[i]["nombre"])
        for i in range (len(listaRobusta)):
            print ("id:",listaRobusta[i]["id"])
        nombre_de_persona=input("escribe el nombre de la persona o la id ")
        for persona in (listaRobusta):
            if persona["nombre"].lower()==nombre_de_persona.lower() or (nombre_de_persona.isdigit() and persona["id"]== int(nombre_de_persona)):
                print ("id",persona["id"])
                print ("nombre",persona["nombre"])
                print ("apellido",persona["apellido"])
                print ("edad",persona["edad"])
                
                for q in range(len(listaRobusta[i]["telefonos"])):
                    print("---------------------------")
                    print("Telefono#",q+1,":")
                    print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                    print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                    
    elif opcionUsuario==4 :          
            print  ("        #### actualizar datos de una persona ####")        
            for i in range (len(listaRobusta))  :
                print ("nombre",listaRobusta[i]["nombre"])  
    
    
    
            actualizar=(input ("escribe el nombre de la persona que quieres actualizar "))
            
        
            for persona in (listaRobusta):
                if persona["nombre"].lower()==actualizar.lower():
                    print ("elige el campo que quieres cambiar ")
                    print ("1.   id ")
                    print ("2.   nombre ")
                    print ("3.   apellido ")
                    print ("4.   edad ")
                    print ("5. numeros de telefono ")
                    opcion=int(input( "   eliga: "))
                    if opcion== 1:
                        nuevoid=input ("nueva id : ")
                        persona["id"]=nuevoid
                    elif opcion==2:
                        nuevoN=input ("nuevo nombre :")
                        persona["nombre"]=nuevoN
                        
                    elif opcion==3:
                        nuevoA=input("nuevo apellido: ")
                        persona["apellido"]=nuevoA
                    elif opcion==4:
                        nuevaEdad=input("nueva edad : ")
                        persona["edad"]=nuevaEdad
                    elif opcion ==5:
                        nuevoTelefono=[{"codigo":int(input("codigo ")),"numero":int(input("numero telefonico ")),"tipo":input(" trabajo o personal ")},
                        {"codigo":int(input("segundo codigo ")),"numero":int(input("numero telefonico dos ")),"tipo":input("trabajo o personal ")}]
                        persona["telefonos"]=nuevoTelefono
    
    elif (opcionUsuario==5):
        print ("      ### eliminar a una persona ###")
        for persona in listaRobusta:
            print("Nombre:", persona["nombre"])
    
        nombreEliminar=input("escriba la persona que quiere eliminar: ")
        
        for persona in listaRobusta:
            if persona["nombre"].lower() == nombreEliminar.lower():
                listaRobusta.remove(persona)
                print("Persona eliminada ")
                
            else :
                print ("no se encontro la persona ")
                
        
        
        
    elif(opcionUsuario==6):
        print("adios ....")
        booleanito = False
    else:
        print("No es una opción válida")

#desarrollado por Alejandro Andres Sanchez Carrillo 
