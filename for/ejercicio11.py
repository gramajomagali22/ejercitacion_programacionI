numero=int(input("Ingrese un numero: "))
contador_primos=0


for i in range(2,numero):

    contador_divisores=0

    for j in range(2,i):

        if i % j == 0:
            contador_divisores+=1
        
    if contador_divisores==0:
        print(f"El numero {i} es primo")
        contador_primos+=1

print(f"Total de numeros Primos: {contador_primos}")
