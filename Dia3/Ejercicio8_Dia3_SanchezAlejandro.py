###############################
#####         Dia 3        ####
###############################
#serie de fibonacci 
n1 = 0
n2 = 1
limite = int(input("digite hasta qué número deseas que llegue la serie de Fibonacci "))

print(n1)
while n2 <= limite:
    print(n2)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    
    

