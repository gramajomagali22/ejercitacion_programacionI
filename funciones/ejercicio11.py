def es_primo(numero:int)-> bool:
    """
    ##
    """
    divisores=0
    for i in range(2, numero):
        if numero % i == 0 :
            divisores+=1
    if divisores==0:
         return True
    else:
         return False

def mostrar_numero_primo(numero: int):
    
    contador=0

    for j in range(2,numero):
             
        if es_primo(j):
                contador+=1
                print(f"El numero {j} es primo")
    return(contador)             

numero=int(input("Ingrese un numero: "))
resultado=mostrar_numero_primo(numero)
print(f"Cantidad de numeros primos: {resultado}")
