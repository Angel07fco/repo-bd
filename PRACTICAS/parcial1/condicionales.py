# Programa para convertir segundos a dias, horas, minutos y segundos
""" s = int(input("Entra segundos: "))
print("Introduciste ", s, " segundos")

# Conversión a minutos
m = s//60
s = s%60

# Conversión a horas
h = m//60
m = m%60

# Conversión a dias
d = h//24
h = h%24
print(d, " dias ", h, " horas ", m, " minutos ", s, " segundos") """

""" edad = int(input("Introduce tu edad: "))
print("Esto esta fuera del if (ANTES)")

if edad >= 18:
    print("Tienes edad para votar")
    print("Tramita tu INE")
    print("Tienes edad para conducir")
else:
    print("Eres menor de edad")
    print("Aun no puedes votar")

print("Esto esta fuera del if (DESPUES)") """

x = float(input("Introduce un número: "))

if x < 0:
    signo = "negativo"
elif x == 0:
    signo = 0
else:
    signo = "positivo"

print("La variable x es de signo: ", signo)