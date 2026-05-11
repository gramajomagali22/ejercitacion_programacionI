
print("Antes de empezar tenga en cuenta terminar el ingreso de numeros debe apretar 0")
numero=int(input("Ingrese un numero: "))

suma=0
i=0

while numero!=0:
    suma+=numero
    i+=1
    numero=int(input("Ingrese un numero: "))

print("SUMA:\t",suma)
promedio=suma/i
print("PROMEDIO:\t",promedio)
