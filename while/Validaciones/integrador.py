"""
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.

"""
print("----BIENVENIDO A CONSULTORIA DE DATOS----\n")
print("INGRESE LOS SIGUIENTES DATOS:\n")
apellido=input("Apellido: ")

edad=int(input("Edad: "))
  
while not (edad>=18 and edad<=90):
    print("Su edad no pertenec al rango establecido en nuestro sistema")
    edad=int(input("Ingrese su edad nuevamente: "))

estado_civil=input("Ingrese su estado civil: ")

while not (estado_civil=="Soltero" or estado_civil=="Soltera" or estado_civil=="Casado" or estado_civil=="Casada" or estado_civil=="Divorciado" or estado_civil=="Divorciada" or estado_civil=="Viudo" or estado_civil=="Viuda"):
    print("Ingrese un estado civil correcto")
    estado_civil=input("Ingrese su estado civil: ")

legajo=int(input("Ingrese su legajo: "))

while not (legajo >= 1000 and legajo <= 9999):
    print("Legajo invalido")
    legajo = int(input("Ingrese legajo nuevamente: "))
    

#MOSTRAR DATOS
print("\nDATOS INGRESADOS:")
print(f"Apellido: {apellido}\nEdad: {edad}\nEstado civil: {estado_civil}\nLegajo: {legajo}")

