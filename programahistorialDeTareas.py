tareas = []
while True:
    print("Opciones:")
    print("1. Agregar tarea al inicio de la lista")
    print("2. Eliminar última tarea de la lista")
    print("3. Mostrar todas las tareas en orden inverso")
    print("4. Mostrar la cantidad total de tareas")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")
    if opcion == "1":
        tarea = input("Introduzca la tarea: ")
        # Agregamos la tarea al inicio de la lista
        tareas.insert(0, tarea)
        # Mostramos un mensaje de confirmación
        print(" ")
        print("================================================================")
        print(f"Tarea '{tarea}' agregada al inicio de la lista")
        print("================================================================")
        print(" ")
    elif opcion == "2":
        # Verificamos si la lista de tareas está vacía
        if len(tareas) == 0:
            print(" ")
            print("================================================================")
            print("La lista de tareas está vacía")
            print("================================================================")
            print(" ")
        else:
            # Eliminamos la última tarea de la lista
            tarea_eliminada = tareas.pop()
            # Mostramos un mensaje de confirmación
            print(" ")
            print("================================================================")
            print(f"Tarea '{tarea_eliminada}' eliminada de la lista")
            print("================================================================")
            print(" ")
    elif opcion == "3":
        # Mostramos todas las tareas en orden inverso
        print(" ")
        print("================================================================")
        print("Tareas en orden inverso:")
        tareas.reverse()
        for tarea in tareas:
            print(tarea)
        print("================================================================")    
        print(" ")
    elif opcion == "4":
        # Mostramos la cantidad total de tareas en la lista
        cantidad_tareas = len(tareas)
        print(" ")
        print("================================================================")
        print(f"Hay un total de {cantidad_tareas} tareas en la lista")
        print("================================================================")
        print(" ")
    elif opcion == "5":
        # Salimos del bucle principal y del programa
        print("================================================================")
        print("¡Hasta luego!")
        print("================================================================")
        break
    else:
        # Opción no válida, mostramos un mensaje de error
        print("Opción no válida. Por favor, seleccione una opción válida (1-5)")