###############################
#####         Dia 3        ####
###############################
#menu de comida con funciones 
def calculoServicio(resultado):
    return (resultado *0.04)

def calculoTotal(resultado, calculoservicio):
    return  (resultado+ servicio) 

numH=(int (input ("ingrese el numero de hamburguesas que va a ordenar ")))
resultado=0
for i in range (numH):
      
    print ("escoja su complemeto para la hamburguesa")
    print ("                   a.pan                       ")
    print ("           1. centeno valor de      1000$   ")
    print( "               2.   avena              1500$   ")
    opc=(int (input ()))
    if opc==1:
     resultado=resultado+1000
    elif opc==2:
     resultado=resultado+1500
     
    print ("                   b.carne                     ")
    print ("           1. 150g      5000$   ")
    print( "               2.   300g             7000$   ")
    opc=(int (input ()))
    if opc==1:
     resultado=resultado+5000
    elif opc==2:
     resultado=resultado+7000
    
    print ("                   c.pollo                   ")
    print ("           1. 200g                   4500$   ")
    print( "               2.   340g             5500$   ")
    opc=(int (input ()))
    if opc==1:
     resultado=resultado+4500
    elif opc==2:
     resultado=resultado+5500

    print ("                   d.pollo  desmechado                ")
    print ("           1. 250g                   6500$   ")
    print( "               2.   350g             7500$   ")
    opc=(int (input ()))
    if opc==1:
     resultado=resultado+6500
    elif opc==2:
     resultado=resultado+7500

    print ("                   e.tocineta                  ")
    print ("           1. lonja de tocineta    1500$   ")
    print( "               2.  lonja de tocineta    2500$   ")
    opc=(int (input ()))
    if opc==1:
     resultado=resultado+1500
    elif opc==2:
     resultado=resultado+2500
     
    print ("                   f.papa frita               ")
    print ("           1.francesa       5000$   ")
    print( "               2.  casco          6000$    ")
    opc=(int (input ()))
    if opc==1:
     resultado=resultado+5000
    elif opc==2:
     resultado=resultado+6000

    print ("                   g.bebida               ")
    print ("           1.gaseosa          5000$    ")
    print( "               2.  cerveza club colmbia    8000$   ")
    print( "               3.  naranjada       9000$    ")
    opc=(int (input ()))
    if opc==1:
     resultado=resultado+5000
    elif opc==2:
     resultado=resultado+8000
    elif opc==3:
     resultado=resultado+9000

servicio=(calculoServicio(resultado))
total=(calculoTotal(resultado,servicio))
print ("su subtotal es ",resultado)
print ("su servicio es ",servicio)
print ("su totsl es",total)
## Desarrolado por Alejandro Andres Sanchez Carrillo 

