cantidad=int(input("Ingrese la cantidad de numeros que desea operar (min:5): "))

if cantidad>=5:
    i=0
    suma=0
    while i<cantidad:
        numero=int(input("Ingrese un numero: "))
        suma+=numero
        i+=1
    
    print("SUMA:\t", suma)

    promedio=suma/cantidad

    print("PROMEDIO:\t", promedio)
else:

    print("La cantidad no pertenece al rango establecido")