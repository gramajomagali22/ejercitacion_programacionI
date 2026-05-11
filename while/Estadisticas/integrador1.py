print("Bienvenido/a tenga en cuenta que para terminar el ingreso de numero debe presionar 0")
numero=int(input("Ingrese un numero: "))

cantPositivos=0
cantNegativos=0

sumaPositivos=0
sumaNegativos=0

i=0
maximo=numero

while numero!=0:
    if numero>0:
        cantPositivos+=1
        sumaPositivos+=numero

        if numero>maximo:
            maximo=numero
    else:
        cantNegativos+=1
        sumaNegativos+=numero

    i+=1
    numero=int(input("Ingrese un numero: "))

print("Cantidad total de numeros:\t",i)
print("Suma de numeros positivos:\t",sumaPositivos)
print("Cantidad de numeros positivos:\t",cantPositivos)
print(f"Promedio de numeros positivos:\t {sumaPositivos/cantPositivos}")
print("Numero de valor Maximo:\t",maximo)
print("Suma de numeros negativos:\t",sumaNegativos)
print("Cantidad de numeros negativos:\t",cantNegativos)
print(f"Porcentaje de numeros negativos respecto al total de ingresos:\t {(cantNegativos/i)*100}")

