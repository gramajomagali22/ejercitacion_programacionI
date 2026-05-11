numero=int(input("Ingrese un numero: "))
contador_divisores=0

for i in range(2, numero):

    if numero%i==0:
        contador_divisores+=1

if not(contador_divisores>=1):
    print("El numero es primo")

else:
    print("No es primo")  
