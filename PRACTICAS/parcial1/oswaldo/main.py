import mylib

def main():
    clientes = []

    while True:
        print("\nBienvenido al sistema de gestión de clientes")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre del cliente: ")
            apellido = input("Ingrese apellido del cliente: ")
            edad = int(input("Ingrese edad del cliente: "))
            if edad < 18:
                print("Error: La edad debe ser mayor a 18 años.")
                continue
            telefono = input("Ingrese número de teléfono del cliente: ")
            mylib.agregar_cliente(clientes, nombre, apellido, edad, telefono)
        elif opcion == "2":
            mylib.mostrar_clientes(clientes)
        elif opcion == "3":
            telefono = input("Ingrese número de teléfono del cliente a actualizar: ")
            encontrados = mylib.buscar_por_telefono(clientes, telefono)
            if encontrados:
                nombre = input("Ingrese nuevo nombre del cliente: ")
                apellido = input("Ingrese nuevo apellido del cliente: ")
                edad = int(input("Ingrese nueva edad del cliente: "))
                if edad < 18:
                    print("Error: La edad debe ser mayor a 18 años.")
                    continue
                mylib.actualizar_cliente(clientes, telefono, nombre, apellido, edad)
            else:
                print("Error: No se encontró ningún cliente con ese número de telefono.")
        elif opcion == "4":
            telefono = input("Ingrese número de teléfono del cliente a eliminar: ")
            encontrados = mylib.buscar_por_telefono(clientes, telefono)
            if encontrados:
                mylib.eliminar_cliente(clientes, telefono)
            else:
                print("Error: No se encontró ningún cliente con ese número de telefono.")
        elif opcion == "5":
            print("Gracias por usar el sistema de gestión de clientes.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()