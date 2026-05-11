i=0
contador1=0
contador2=0
mayor=0

while i<10:
    
    nombre=input("Ingrese su nombre: ")

    edad=int(input("Ingrese su edad: "))

    genero=input("Ingrese su Género (M/F/O): ")

    tecnologia=input("Ingrese su votacion (IA/RV/RA/IOT): ")

    if edad>=18:

        # Mayor masculino
        if genero=="M":
            if i==0 or edad>mayor:
                mayor=edad
                nombreMayor=nombre
                votacionMayor=tecnologia

        
        if (genero=="M") and (tecnologia=="IOT" or tecnologia=="IA") and (25<=edad and edad<=50):
            contador1+=1

        
        if (genero!="F") and (33<=edad and edad<=40) and (tecnologia!="IA"):
            contador2+=1

    else:
        print("No puede votar tiene que ser mayor de edad.")
        i-=1

    i+=1

porcentaje=(contador2/10)*100

print("Cantidad:", contador1)
print("Porcentaje que NO votaron IA:", porcentaje)

if mayor>0:
    print(f"Mayor masculino: {nombreMayor} - {votacionMayor}")
else:
    print("No hubo masculinos.")