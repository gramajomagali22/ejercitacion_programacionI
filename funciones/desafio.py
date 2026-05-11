#FUNCION
def get_int(mensaje_ingreso: str, mensaje_error: str, min: int, max:int, reintentos:int) -> int|None:
    """
    #
    #
    #
    """
    bandera=0
    while reintentos!=0:
        numero=int(input(mensaje_ingreso))
        if numero>=min and numero<=max:
            bandera=1
            break
        else:
            print(mensaje_error)
        reintentos-=1
    
    if reintentos==0 and bandera==0:
        return None
    else:
        return numero


#MAIN
numero= get_int(
    mensaje_ingreso="<<📝Ingrese un numero: ",
    mensaje_error="<<❌ Valor inválido ❌>>",
    min=1,
    max=120,
    reintentos=3

)
print(numero)



