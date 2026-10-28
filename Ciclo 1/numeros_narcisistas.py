numero = int(input("Ingrese un numero (0 o negativo para terminar): "))

while numero > 0:
    texto = str(numero)
    cantidad = len(texto)
    suma = 0

    for digito in texto:
        suma = suma + int(digito) ** cantidad

    if suma == numero:
        print("Es narcisista")
    else:
        print("No es narcisista")

    numero = int(input("Ingrese un numero (0 o negativo para terminar): "))

print("Fin")
