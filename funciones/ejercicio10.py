def numero_primo(numero:int)-> bool:
    cont=0
    for i in range(2,numero):
        if numero % i == 0:
            cont+=1
    
    if cont>=1:
        resultado=False
    else:
        resultado=True

    return resultado


numero=int(input("Ingrese un numero: "))

if numero_primo(numero) :
    print(f"El numero {numero} es primo.")
else:
    print(f"El numero {numero} no es primo.")