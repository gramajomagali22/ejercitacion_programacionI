i=0

while i<10:
    numero=int(input("iNgrese un nuemero: "))
    if i==0:
        maximo=numero
        minimo=numero
    else:
        if numero>maximo:
            maximo=numero
        elif numero<minimo:
                minimo=numero
    i+=1

print(maximo)
print(minimo)