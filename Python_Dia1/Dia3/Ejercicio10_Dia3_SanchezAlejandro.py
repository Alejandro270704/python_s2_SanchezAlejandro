###############################
#####         Dia 3        ####
###############################
#promedio de numeros 
cant=(int (input ("ingrese la cantidad de numeros para sacar el promedio ")))
suma=0

for i in range (cant):
     print ("numero",i+1)
     num=(int (input ("escribe el numero " )))
    
     suma += num 
  
resultado=suma / cant 
print ("el promedio es ",resultado)

## Desarrolado por Alejandro Andres Sanchez Carrillo 