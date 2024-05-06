import mylib

def main():
    productos = []

    while True:
        print("\nBienvenido al sistema de gestión de inventario de la papeleria HUEJUTLA")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre del producto: ")
            encontrados = mylib.buscar_por_producto(productos, nombre)
            if encontrados:
                print("Error: Ya existe un producto registrado con ese nombre.")
            else:
                cantidad = input("Ingrese cantidad del producto: ")
                precio = float(input("Ingrese precio del producto: "))
                mylib.agregar_producto(productos, nombre, cantidad, precio)
        elif opcion == "2":
            mylib.mostrar_productos(productos)
        elif opcion == "3":
            nombre = input("Ingrese nombre del producto a actualizar: ")
            encontrados = mylib.buscar_por_producto(productos, nombre)
            if encontrados:
                cantidad = input("Ingrese cantidad del producto: ")
                precio = float(input("Ingrese precio del producto: "))
                mylib.actualizar_producto(productos, nombre, cantidad, precio)
            else:
                print("Error: No se encontró ningún producto con ese nombre.")
        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a eliminar: ")
            encontrados = mylib.buscar_por_producto(productos, nombre)
            if encontrados:
                mylib.eliminar_producto(productos, nombre)
            else:
                print("Error: No se encontró ningún producto con ese nombre.")
        elif opcion == "5":
            print("Gracias por usar el sistema de gestión de inventario de la papeleria HUEJUTLA.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()