###############################
#####         Dia 3        ####
###############################
#empresa con funciones 
def calcularsueldobruto(horas,valorHora):
    return (horas * valorHora)
def descuento(sueldobruto ):
    return sueldobruto*0.04 


numeroEmpleados=int (input ("ingrese el numero de empleados "))
valorhora =20000
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
            
            
            
sueldoBrutoMayor=calcularsueldobruto(cantidadHoras,valorhora)
pensionMayor=descuento(sueldoBrutoMayor)
epsMayor=descuento(sueldoBrutoMayor)
resultado1=int (sueldoBrutoMayor+pensionMayor+epsMayor)
 

sueldoBrutoMenor=calcularsueldobruto(cantidadHoras,valorhora)
pensionMenor=descuento(sueldoBrutoMenor)
epsMenor=descuento(sueldoBrutoMenor)
resultado2=int (sueldoBrutoMenor+pensionMenor+epsMenor)


print ("el que mas gana es ",nombreMayor,resultado1," pesos" )
print (sueldoBrutoMayor)
print (epsMayor)
print (pensionMayor)

print ("el que menos gana es ",nombreMenor,resultado2," pesos ")
print (sueldoBrutoMenor)
print(epsMenor)
print(pensionMenor)
    ## Desarrolado por Alejandro Andres Sanchez Carrillo 
