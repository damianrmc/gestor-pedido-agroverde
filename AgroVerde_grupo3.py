
productos_disponibles = {
    1: {"Producto": "Zanahoria", "Cantidad": 500},
    2: {"Producto": "Lechuga", "Cantidad": 300,},
    3: {"Producto": "Ruibarbo", "Cantidad": 40},
}

clientes = []
pedido = []

print("Bienvenido a AgroVerde, el sistema de pedidos de productos agrícolas frescos.")

while True:
    print("\n1. Cliente")
    print("2. Interno")
    print("3. Salir")

    opcion = input("Ingrese su opción: ")
    if opcion == '1':
        print("\nBienvenido cliente, por favor regístrese.")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = input("Ingrese su teléfono: ")
        direccion = input("Ingrese su dirección: ")
        
        cliente = {
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "direccion": direccion
        }
        clientes.append(cliente)
        print(f"\nCliente registrado: {nombre} {apellido}")

        while True:
            print("\n¿Qué acción desea realizar?")
            print("1. Ver productos")
            print("2. Hacer pedido")
            print("3. Salir")
            accion = input("Ingrese su opción: ")
            if accion == '1':
                print("\nProductos disponibles:")
                for key, producto in productos_disponibles.items():
                    print(f"{key}. {producto['Producto']} - Cantidad: {producto['Cantidad']}")





    


# if else primero cliente(1) o interno(2)

# Cliente - luego tiene que registrarse (nombre, apellido, teléfono, dirección), elegir acción (1. Ver productos, 2. Hacer pedido, 3. Salir)

# interno - 1. inventario 2. pedidos 3. ver cliente 4. salir
# inventario - ver productos, agregar productos, eliminar productos, salir
# pedidos - ver pedidos, eliminar pedidos, editar pedido, salir






# bienvenido a nuestro sistema de pedidos AgroVerde




# ingresar nueva compra





# for para mostrar lo que hay en el inventario






# su pedido está listo para ser enviado a su domicilio