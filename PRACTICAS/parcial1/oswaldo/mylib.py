# Función para agregar un nuevo cliente
def agregar_cliente(clientes, nombre, apellido, edad, telefono):
    cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "telefono": telefono
    }
    clientes.append(cliente)
    print("Cliente agregado correctamente.")

# Función para mostrar todos los clientes
def mostrar_clientes(clientes):
    if clientes:
        print("Lista de clientes:")
        for cliente in clientes:
            print(f"Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}, Edad: {cliente['edad']}, Telefono: {cliente['telefono']}")
    else:
        print("No hay clientes registrados.")

# Función para buscar un cliente por su número de telefono
def buscar_por_telefono(clientes, telefono):
    encontrados = [cliente for cliente in clientes if cliente["telefono"].lower() == telefono.lower()]
    return encontrados

# Función para actualizar un cliente existente
def actualizar_cliente(clientes, telefono, nombre, apellido, edad):
    for cliente in clientes:
        if cliente["telefono"] == telefono:
            cliente["nombre"] = nombre
            cliente["apellido"] = apellido
            cliente["edad"] = edad
            print("Cliente actualizado correctamente.")
            return
    print("Error: No se encontró ningún cliente con ese número de teléfono.")

# Función para eliminar un cliente existente
def eliminar_cliente(clientes, telefono):
    for cliente in clientes:
        if cliente["telefono"].lower() == telefono.lower():
            clientes.remove(cliente)
            print("Cliente eliminado exitosamente.")
            return
    print("El cliente no se encontró.")