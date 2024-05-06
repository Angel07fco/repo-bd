# Definición de variables globales
clientes = {}
id_cliente = 1

# Función para agregar un nuevo cliente
def agregar_cliente(nombre, apellido, edad, telefono):
    global id_cliente
    for cliente_id, cliente in clientes.items():
        if cliente["telefono"] == telefono:
            print("Error: Ya existe un cliente con este número telefónico.")
            return
    cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "telefono": telefono
    }
    clientes[id_cliente] = cliente
    id_cliente += 1
    print("Cliente agregado correctamente.")

# Función para mostrar todos los clientes
def mostrar_clientes():
    if clientes:
        print("Lista de clientes:")
        for cliente_id, cliente in clientes.items():
            print(f"ID: {cliente_id}, Cliente: {cliente}")
    else:
        print("No hay clientes registrados.")

# Función para actualizar un cliente existente
def actualizar_cliente(cliente_id, nombre, apellido, edad, telefono):
    for id_cliente, cliente in clientes.items():
        if id_cliente == cliente_id:
            if cliente["telefono"] == telefono:
                print("Error: Ya existe un cliente con este número telefónico.")
                return
            cliente["nombre"] = nombre
            cliente["apellido"] = apellido
            cliente["edad"] = edad
            cliente["telefono"] = telefono
            print("Cliente actualizado correctamente.")
            return
    print("Error: No se encontró ningún cliente con ese ID.")

# Función para eliminar un cliente existente
def eliminar_cliente(cliente_id):
    if cliente_id in clientes:
        del clientes[cliente_id]
        print("Cliente eliminado correctamente.")
    else:
        print("Error: No se encontró ningún cliente con ese ID.")

# Función principal del programa
def main():
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
            agregar_cliente(nombre, apellido, edad, telefono)
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            cliente_id = int(input("Ingrese ID del cliente a actualizar: "))
            if cliente_id in clientes:
                nombre = input("Ingrese nuevo nombre del cliente: ")
                apellido = input("Ingrese nuevo apellido del cliente: ")
                edad = int(input("Ingrese nueva edad del cliente: "))
                if edad < 18:
                    print("Error: La edad debe ser mayor a 18 años.")
                    continue
                telefono = input("Ingrese nuevo número de teléfono del cliente: ")
                actualizar_cliente(cliente_id, nombre, apellido, edad, telefono)
            else:
                print("Error: No se encontró ningún cliente con ese ID.")
        elif opcion == "4":
            cliente_id = int(input("Ingrese ID del cliente a eliminar: "))
            eliminar_cliente(cliente_id)
        elif opcion == "5":
            print("Gracias por usar el sistema de gestión de clientes.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Llamada a la función principal
if __name__ == "__main__":
    main()