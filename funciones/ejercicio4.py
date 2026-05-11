
def area_rectangulo(base:int, altura:int ):
    """
    #QUE HACE?

        La función recibe la base y la altura y retorna el área. 

    #RETORNA:

        Int: el area del rectangulo

    """
    area=base*altura

    return area

base=int(input("Ingrese la base del rectangulo: "))
altura=int(input("Ingrese la altura del rectangulo: "))
print("El area del rectangulo es: ", area_rectangulo(base,altura))
