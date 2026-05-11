
#Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

nota=int(input("Ingrese una nota: "))

while not (nota>=1 and nota<=10):
    print("La nota no pertenece al rango establecido")
    nota=int(input("Ingrese una nota nuevamente: "))