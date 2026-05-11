def numero_solicitado():
    """
    # QUE HACE?
        Pide el ingreso de un numero en la funcion y lo retorna
    #RETORNA:
      float: Numero ingresado por el usuario 
    """
    numero=float(input("Ingrese un numero: "))
    return numero
    

print("El numero ingresado es: ",numero_solicitado())