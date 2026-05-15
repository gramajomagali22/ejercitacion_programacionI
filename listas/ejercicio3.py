"""
3)Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números
"""
def calcular_promedio(lista: list)->float:
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]

    elementos= len(lista)
    return suma/elementos


lista=[1,15,36,44,5,8,70]

promedio=calcular_promedio(lista)

print("Elementos de la lista: ")
for i in range(len(lista)):
    print(f"Elemento[{i+1}]: {lista[i]}")

print(f"El promedio de la lista ingresada es: {promedio:.2f}")