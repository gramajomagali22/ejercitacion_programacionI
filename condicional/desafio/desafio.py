"""
ENTRADAS:
cliente (Residencial, Comercial ,Industrial)
cantidad de m3

SALIDAS:
subtotal
IVA
bonificaciones
Recargo
Total

CONSTANTES:
costo 200
cargo fijo 7000

OPERACIONES:

Cliente Residencial:

● Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del
consumo.
● Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

Cliente Comercial:

● Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del
consumo.
● Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
● Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

Cliente Industrial:

● Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del
 consumo.
● Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
● Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

Casos especiales:

● Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones es menor a
$35000, se aplica un descuento adicional del 5%.

En todos los casos, se aplica el IVA del 21% sobre el total.

"""

print("BIENVENIDO/A A GOTITA S.A")
print("----------------------------")
print("Categoria de Clientes:\n Industrial\n Comercial\n Residencial")


cliente=input("Ingrese su categoria como cliente en minusculas: ")
consumo=int(input("Ingrese la cantidad de agua en metros cubicos: "))

COSTO_POR_M3=200
CARGO_FIJO=7000
IVA= 0.21

subtotal=consumo*COSTO_POR_M3

bonificacion=0
recargo=0
adicional=0

match cliente:

    case "residencial":
        if subtotal<35000:
            adicional=0
        elif consumo<30:
            bonificacion=0.30
        elif consumo>80:
            recargo=0.15
    

    case "comercial":

        if consumo>300:
            bonificacion=0.08
        elif consumo>150:
            bonificacion=0.12
        elif consumo<50:
            recargo=0.05
    

    case "industrial":

        if consumo>1000:
            bonificacion= 0.20
        elif consumo>500:
            bonificacion= 0.30
        elif consumo<200:
            recargo=0.10
    
    case _:
        print("Categoria no válida")


totalRecargos=subtotal*recargo
totalBonificacion= subtotal*bonificacion
totalIva=subtotal*0.21
totalAdicional=subtotal*adicional
total=subtotal+CARGO_FIJO+totalRecargos-totalBonificacion-totalAdicional
total_neto=total+totalIva

print("CLIENTE:", cliente)

print("SUBTOTAL:\t", subtotal)

print("BONIFICACIONES:\t", totalBonificacion)

print("RECARGO:\t", totalRecargos)

if cliente=="residencial" and subtotal>35000:
    print("ADICIONAL:\t", totalAdicional)

print("IVA (21%):\t",totalIva)

print("TOTAL NETO:\t", total_neto)


        