"""
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

"""

clave=input("Ingrese una clave: ")
i=1

while clave!= "123456" and i<3:
    i+=1
    print("Clave incorrecta")
    clave=input("Ingrese una clave nuevamente: ")
    