import mylib

def main():
    biblioteca = []

    while True:
        print("\nBienvenido a la Biblioteca")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Buscar por autor")
        print("4. Mostrar todos los libros")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            genero = input("Ingrese el género del libro: ")
            mylib.agregar_libro(biblioteca, titulo, autor, genero)
        elif opcion == "2":
            titulo = input("Ingrese el título del libro que desea eliminar: ")
            mylib.eliminar_libro(biblioteca, titulo)
        elif opcion == "3":
            autor = input("Ingrese el autor del libro que desea buscar: ")
            encontrados = mylib.buscar_por_autor(biblioteca, autor)
            if encontrados:
                print("Libros encontrados:")
                for libro in encontrados:
                    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
            else:
                print("No se encontraron libros de ese autor.")
        elif opcion == "4":
            mylib.mostrar_libros(biblioteca)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()