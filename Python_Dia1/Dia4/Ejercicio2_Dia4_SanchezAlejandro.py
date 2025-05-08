###############################
#####         Dia 3        ####
###############################
#area de un triangulo 
numeroEmpleados=int (input ("ingrese el numero de empleados "))
valorhora=20000
print ("empiece a digitar el nombre y las horas trabajas ")
nombre=str(input ("ingrese el nombre "))
nombreMayor=nombre 
nombreMenor=nombre 

cantidadHoras=int (input ("ingresa las horas trabajadas "))
horaMayor=cantidadHoras
horaMenor=cantidadHoras
for i in range (1,numeroEmpleados,1):
    nombre=str(input ("ingrese el nombre "))
    cantidadHoras=int (input ("ingresa las horas trabajadas "))
       
    if cantidadHoras>horaMayor :
        horaMayor=cantidadHoras
        nombreMayor=nombre 
        
        
    if cantidadHoras<horaMenor:
         horaMenor=cantidadHoras
         nombreMenor=nombre
            
            
sueldobrutomayor=horaMayor*valorhora
epsMayor=sueldobrutomayor*0.04
pensionMayor=sueldobrutomayor*0.04

resultado1=int (sueldobrutomayor+epsMayor+pensionMayor)


sueldobrutoMenor=horaMenor*valorhora
epsMenor=sueldobrutoMenor*0.04
pensionMenor=sueldobrutoMenor*0.04
resultado2=int (sueldobrutoMenor+epsMenor+pensionMenor)

print ("el que mas gana es ",nombreMayor,resultado1," pesos" )
print (sueldobrutomayor)
print (epsMayor)
print (pensionMayor)


print ("el que menos gana es ",nombreMenor,resultado2," pesos ")
print (sueldobrutoMenor)
print(epsMenor)
print(pensionMenor)
## Desarrolado por Alejandro Andres Sanchez Carrillo 