def agregar_libro(biblioteca, titulo, autor, genero):
    libro = {"titulo": titulo, "autor": autor, "genero": genero}
    biblioteca.append(libro)
    print("Libro agregado exitosamente.")

def buscar_por_autor(biblioteca, autor):
    encontrados = [libro for libro in biblioteca if libro["autor"].lower() == autor.lower()]
    return encontrados

def mostrar_libros(biblioteca):
    if biblioteca:
        print("Libros disponibles en la biblioteca:")
        for libro in biblioteca:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
    else:
        print("No hay libros disponibles en la biblioteca.")

def eliminar_libro(biblioteca, titulo):
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            biblioteca.remove(libro)
            print("Libro eliminado exitosamente.")
            return
    print("El libro no se encontró en la biblioteca.")