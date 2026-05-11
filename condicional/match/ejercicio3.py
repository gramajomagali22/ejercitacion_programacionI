"""
Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año.
En caso de hacerlo mostrar por print el mensaje “Se viaja”, caso contrario mostrar “No se viaja”.
a. Si es invierno: solo se viaja a Bariloche.
b. Si es verano: se viaja a Mar del plata y Cataratas.
c. Si es otoño: se viaja a todos los lugares.
d. Si es primavera: se viaja a todos los lugares menos Bariloche.

"""
print("DESTINOS DE LA AGENCIA")
print("------------------------------")
print("Bariloche")
print("Mar del Plata")
print("Cataratas del Iguazú")
print("------------------------------")
print("\n")


estacion=input("Ingrese una estacion del año en la que desea realizar el viaje: \n").lower()
destino= input("Ingrese el destino: \n").lower()

match estacion:
    case "invierno":
        if destino=="bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "verano":
        if destino=="mar del plata" or destino=="cataratas del iguazú":
            print("se viaja")
        else:
            print("No se viaja")
    case "otoño":
        print("se viaja")
    case "primavera":
        if destino!="bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case _:
        print("Estación no válida")
            