"""
2) Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
"""
def crear_array( parametro: int) -> list:
    """
     RECIBE:
        Cantidad de elementos de la lista.

    HACE:
        Solicita números y los agrega a una lista.

    RETORNA:
        La lista creada.
    """
    lista=[]
    for i in range(parametro):
        numero=int(input("<< Ingrese un numero: "))
        lista.append(numero)
    
    return lista

def ingresar_cantidad():
    """
    RECIBE: 
        No recibe ningun parametro
    HACE:
        Pide el Parametro para que otra funcion cree una lista segun ese parametro
    RETORNA:
        Retorna la lista
    """
    cantidad= int(input("<< Ingrese la cantidade de elementos de la lista que desea crear: "))

    lista=crear_array(cantidad)

    return lista

lista_numeros = ingresar_cantidad()

print("\nLista creada:")

for i in range(len(lista_numeros)):
    print(lista_numeros[i])
