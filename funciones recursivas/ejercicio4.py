def funcion_fibonacci(numero: int) -> int:
    if numero==0:
        return 0
    elif numero==1:
        return 1
    else:
        return (funcion_fibonacci(numero -1)+ funcion_fibonacci(numero-2))
    

numero=int(input("<< Ingrese un numero: "))
print(funcion_fibonacci(numero))