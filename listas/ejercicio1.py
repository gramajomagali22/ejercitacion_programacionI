def crear_array( parametro: int) -> list:
    lista=[]
    for i in range(parametro):
        numero=int(input("Ingrese un numero: "))
        lista.append(numero)
    
    return lista


cantidad_elementos=int(input("Ingrese la cantidad de elementos de la lista: "))
lista=crear_array(cantidad_elementos)


for i in range(cantidad_elementos):
    print(lista[i])