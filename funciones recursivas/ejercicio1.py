def numeros_naturales(numero:int)-> int:
    if numero == 1:
        return 1
    return numero + numeros_naturales(numero-1)

num=int(input("Ingrese un numero: "))
while not(num>=1):
    num=int(input("VALOR NO VALIDO\n<<Ingrese un numero: "))

print(numeros_naturales(num))