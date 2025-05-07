
###############################
#####         Dia 6      ####
###############################
def resultado1(num1,num2 ):
    return( num1+num2 )

def resultado2(num1,num2 ):
    return (num1-num2)

def resultado3(num1,num2 ):
    return(num1*num2 )
def resultado4(num1,num2 ):
    return(num1/num2 )

num1=int (input("ingresa el primer numero "))
num2=int (input("ingresa el segundo numero"))
          
print ("escoge la opcion que desees")
print ("1.       sumar ")
print ("2.       restar ")
print ("3.          multiplicar ")
print ("4.            dividir    ")
opc=int(input ())
if opc==1:
   
    print(resultado1(num1,num2 ))
    

if opc ==2:

    print(resultado2(num1,num2))

if opc==3:
  
    print (resultado3(num1,num2))

if opc==4:
    
    print (resultado4(num1,num2))
    ## Desarrolado por Alejandro Andres Sanchez Carrillo 