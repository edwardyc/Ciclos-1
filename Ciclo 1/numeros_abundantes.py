inicio = int(input("Rango inicial: "))
final = int(input("Rango final: "))

print("Los numeros abundantes son:")

for numero in range(inicio, final + 1):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma = suma + divisor

    if suma > numero:
        print(numero)
