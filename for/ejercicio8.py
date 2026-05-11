numero=int(input("Ingrese el numero: "))
numero_actual=0

for i in range(1, numero+1):
    numero_actual*=10
    numero_actual+=i

    print(numero_actual)