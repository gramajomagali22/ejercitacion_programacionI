"""
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá
determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
● Menos de 160 cm: Base
● Entre 160 cm y 179 cm: Escolta
● Entre 180 cm y 199 cm: Alero
● 200 cm o más: Ala-Pívot o Pívot

"""

altura = int(input("Ingrese su altura: "))

if altura < 160:
    print("Usted será Base")
elif altura >= 160 and altura <= 179:
    print("Usted es Escolta")
elif altura >= 180 and altura <= 199:
    print("Usted es Alero")
else:
    print("Usted es Ala-Pívot o Pívot")
