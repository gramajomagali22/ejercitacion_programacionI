def area_circular(radio:int):
    """
    Calcular el area de un circulo teniendo como dato 
    PI: 3,1416
    radio

    area=PI*(radio*radio)
    """
    PI= 3.1416

    area=PI*(radio**2)

    return area

radio=int(input("Ingrese el radio del circulo: "))

print("El area del Circulo es: ", area_circular(radio))
    


