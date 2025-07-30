def carrito_compras():
    """
    Simula un carrito de compras con opciones para agregar, eliminar, mostrar productos y calcular
    """

    carrito = []


    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar carrito")
        print("4. Calcular total")
        print("5. Salir")

        opcion = input("Selecciones una opcion (1-5): ")

        if opcion == '1':
            producto = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                carrito.append((producto, precio))
                print(f"✅ '{producto}' agregado.")
            except ValueError:
                print("❌ Precio inválido.")

        elif opcion == '2':
            producto = input("Nombre del producto a eliminar: ")
            encontrado = False
            for item in carrito:
                if item[0].lower() == producto.lower():
                    carrito.remove(item)
                    encontrado = True
                    print(f"❌ '{producto}' eliminado.")
                    break
                if not encontrado:
                    print(f"⚠️ '{producto}' no está en el carrito.") 

        elif opcion == '3':
            if not carrito:
                print("🛒 El carrito está vacío.")
            else:
                print("📋 Productos en el carrito:")
                for prod, precio in carrito:
                    print(f"-{prod}: ${precio:.2f}")

        elif opcion == '4':
            total = sum(precio for _, precio in carrito)
            print(f"💰 Total a pagar: ${total:.2f}")

        elif opcion == '5':
            print("👋 ¡Gracias por usar el carrito!")
            break

        else:
            print("❌ Opción inválida.")   

carrito_compras()             
                                      