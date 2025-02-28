
inventario = {}

def agregar_producto():
    producto = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    if producto in inventario:  
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"Producto {producto} agregado con éxito!")

def eliminar_producto():
    producto = input("Ingresa el nombre del producto a eliminar: ")
    if producto in inventario:  
        del inventario[producto]
        print(f"Producto {producto} eliminado con éxito!")
    else:
        print(f"El producto {producto} no está en el inventario.")

def mostrar_inventario():
    if len(inventario) == 0:  
        print("El inventario está vacío.")
    else:
        print("Inventario de productos:")
        for producto, cantidad in inventario.items(): 
            print(f"{producto}: {cantidad} unidades")

def actualizar_producto():
    producto = input("Ingresa el nombre del producto a actualizar: ")
    if producto in inventario:  
        nueva_cantidad = int(input(f"Ingresa la nueva cantidad para {producto}: "))
        inventario[producto] = nueva_cantidad
        print(f"Producto {producto} actualizado con éxito a {nueva_cantidad} unidades.")
    else:
        print(f"El producto {producto} no está en el inventario.")

def main():
    while True: 
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Actualizar producto")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            actualizar_producto()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")


main()
