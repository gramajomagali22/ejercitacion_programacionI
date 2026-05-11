suma=0
for i in range(10):
    numero=int(input("ingrese un numero: "))
    suma+=numero
    if numero==0:
        break

promedio=suma/i
print(suma)