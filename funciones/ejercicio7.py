def verificar_par(numero: int):
    if numero % 2 == 0:
        es_par= True
    else:
        es_par=False

    return (es_par)

numero= int(input("Ingrese un numero: "))

if verificar_par(numero) == True:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")