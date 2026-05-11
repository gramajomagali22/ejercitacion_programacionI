def potencia_del_numero(base:int, exponente:int) -> int:
    resultado = base ** exponente
    return resultado

numero=int(input("Ingrese un número: "))
exponente=int(input("Ingrese el exponente: "))
resultado = potencia_del_numero(numero, exponente)
print(f"El resultado de {numero} elevado a {exponente} es: {resultado}")