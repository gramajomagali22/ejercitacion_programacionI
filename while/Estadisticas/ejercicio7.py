print("Antes de empezar tenga en cuenta terminar el ingreso de numeros debe apretar 0")
numero=int(input("Ingrese un numero: "))

suma_positivos=0
producto_negativos=1
bandera=0


while numero!=0:

    if numero>0:
        suma_positivos+=numero
    else:
        producto_negativos*=numero
        bandera=1
    numero=int(input("Ingrese un numero: "))

print("SUMA DE POSITIVOS:\t",suma_positivos)

if bandera==1:
    print("PRODUCTO DE NEGATIVOS:\t", producto_negativos)
else:
    print("No se ingresaron numeros negativos")