# Función para agregar un nuevo producto
def agregar_producto(productos, nombre, cantidad, precio):
    producto = {
        "producto": nombre.lower(),
        "cantidad": cantidad,
        "precio": precio
    }
    productos.append(producto)
    print("Producto agregado correctamente.")

# Función para mostrar todos los productos
def mostrar_productos(productos):
    if productos:
        print("Lista de productos:")
        for producto in productos:
            print(f"Producto: {producto['producto'].title()}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
    else:
        print("No hay productos registrados.")

# Función para buscar un prodctco por nombre del producto
def buscar_por_producto(productos, nombre):
    encontrados = [producto for producto in productos if producto["producto"].lower() == nombre.lower()]
    return encontrados

# Función para actualizar un producto existente
def actualizar_producto(productos, nombre, cantidad, precio):
    for producto in productos:
        if producto["producto"].lower() == nombre.lower():
            producto["cantidad"] = cantidad
            producto["precio"] = precio
            print("Producto actualizado correctamente.")
            return

# Función para eliminar un cliente existente
def eliminar_producto(productos, nombre):
    for producto in productos:
        if producto["producto"].lower() == nombre.lower():
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            return