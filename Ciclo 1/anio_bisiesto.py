def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    if anio % 4 == 0 and anio % 100 != 0:
        return True
    return False


anio1 = int(input("Primer anio: "))
anio2 = int(input("Segundo anio: "))

bisiesto1 = es_bisiesto(anio1)
bisiesto2 = es_bisiesto(anio2)

print("Anio 1 es bisiesto:", bisiesto1)
print("Anio 2 es bisiesto:", bisiesto2)
print("Misma condicion:", bisiesto1 == bisiesto2)
