numero=int(input("Ingrese un numero: "))
contador_divisores=0

for i in range(1, numero+1):

    if not(numero%i==0):
        continue
    contador_divisores+=1

    print(f"Divisor: {i}")

print(f"Contador de divisores: {contador_divisores}")
    
