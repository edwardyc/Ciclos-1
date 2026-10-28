def es_multiplo(numero, divisor):
    if divisor == 0:
        return False
    if numero % divisor == 0:
        return True
    else:
        return False


a = int(input("Primer valor: "))
b = int(input("Segundo valor: "))

print(a, "es multiplo de", b, ":", es_multiplo(a, b))
print(b, "es multiplo de", a, ":", es_multiplo(b, a))
