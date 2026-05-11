def numero_solicitado():
    """
    # QUE HACE?
        Pide el ingreso de un numero en la funcion y lo retorna
    #RETORNA:
      int: Numero ingresado por el usuario 
    """
    numero=int(input("Ingrese un numero: "))
    return numero
    
#Programa principal
print("El numero ingresado es: ",numero_solicitado())