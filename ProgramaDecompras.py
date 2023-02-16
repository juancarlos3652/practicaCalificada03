lista_compras = []
while True:
    # Mostramos las opciones disponibles al usuario
    print("Opciones:")
    print("1. Agregar producto al final de la lista")
    print("2. Eliminar primer producto de la lista")
    print("3. Mostrar todos los productos de la lista")
    print("4. Salir")
    # Pedimos al usuario que seleccione una opción
    opcion = input("Seleccione una opción (1-4): ")
    # Evaluamos la opción seleccionada por el usuario
    if opcion == "1":
        # Pedimos al usuario que introduzca el nombre del producto
        producto = input("Introduzca el nombre del producto: ")
        # Agregamos el producto al final de la lista
        lista_compras.append(producto)
        # Mostramos un mensaje de confirmación
        print(" ")
        print("================================================================")
        print(f"Producto '{producto}' agregado a la lista de compras")
        print("================================================================")
        print(" ")
    elif opcion == "2":
        # Verificamos si la lista de compras está vacía
        if len(lista_compras) == 0:
            print(" ")
            print("================================================================")
            print("La lista de compras está vacía")
            print("================================================================")
            print(" ")
        else:
            # Eliminamos el primer producto de la lista
            producto_eliminado = lista_compras.pop(0)
            # Mostramos un mensaje de confirmación
            print(" ")
            print("================================================================")
            print(f"Producto '{producto_eliminado}' eliminado de la lista de compras")
            print("================================================================")
            print(" ")
    elif opcion == "3":
        # Mostramos todos los productos de la lista
        print(" ")
        print("Lista de compras:")
        print("================================================================")
        for producto in lista_compras:
            print(producto)
        print("================================================================")    
        print(" ")
    elif opcion == "4":
        # Salimos del bucle principal y del programa
        print(" ")
        print("================================================================")
        print("¡Hasta luego!")
        print("================================================================")
        print(" ")
        break
    else:
        # Opción no válida, mostramos un mensaje de error
        print("Opción no válida, seleccione una opción válida!! (1-4)")
        print(" ")