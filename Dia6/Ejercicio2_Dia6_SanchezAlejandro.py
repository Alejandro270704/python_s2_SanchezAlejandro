
num1=int (input("ingresa el primer numero "))
num2=int (input("ingresa el segundo numero"))
          
print ("escoge la opcion que desees")
print ("1.       sumar ")
print ("2.       restar ")
print ("3.          multiplicar ")
print ("4.            dividir    ")
opc=int(input ())

if opc==1:
    resultado1=int (num1+num2)
    print(resultado1)
    

if opc ==2:
    resultado2=num1-num2
    print(resultado2)

if opc==3:
    resultado3=num1*num2
    print (resultado3)

if opc==4:
    resultado4=float (num1/num2 )
    print (resultado4)
    