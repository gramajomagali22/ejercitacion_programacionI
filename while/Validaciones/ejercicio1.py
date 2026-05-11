"""
Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

"""
clave=input("Ingrese una clave: ")

while clave != "123456":
    print("CLAVE INCORRECTA")
    clave=input("Ingrese una clave nuevamente: ")