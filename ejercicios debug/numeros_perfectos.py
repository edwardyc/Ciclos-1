numero = int(input("Ingrese un numero (negativo para terminar): "))

while numero >= 0:
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma = suma + divisor

    if suma == numero:
        print("Es perfecto")
    else:
        print("No es perfecto")

    numero = int(input("Ingrese un numero (negativo para terminar): "))

print("Fin")
