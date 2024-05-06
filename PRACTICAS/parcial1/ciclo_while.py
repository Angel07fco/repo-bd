""" suma = 0
opc = 's'

while opc == 's' or opc == 'S':
    num = float(input("Introduce un número: "))
    suma += num
    opc = input("Desea introducir otro número? S/N: ")

print("La suma es: ", suma) """

n = int(input("Ingrese un número entero: "))
k = 1
while k<=10:
    print(n, ' x ', k, ' = ', n*k)
    k = k+1