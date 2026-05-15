def sumar_digitos(numero:int)->int:
    if numero<10:
        return numero
    return(numero % 10 + sumar_digitos(numero // 10))


numero= int(input("<< Ingrese un numero: "))
print(sumar_digitos(numero))