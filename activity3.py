# facturacion de supermercado

inventario = {}

def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    existencias = int(input("Ingrese la cantidad de existencias: "))
    precio_unitario = float(input("Ingrese el precio unitario: "))
    inventario[codigo] = {"nombre": nombre, "existencias": existencias, "precio_unitario": precio_unitario}

def realizar_compra():
    codigo = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    if codigo in inventario:
        inventario[codigo]["existencias"] += cantidad
        print("Compra realizada.")
    else:
        print("El producto no está en el inventario.")
def realizar_venta():
    codigo = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    if codigo in inventario:
        if inventario[codigo]["existencias"] >= cantidad:
            inventario[codigo]["existencias"] -= cantidad
            print("Venta realizada.")
        else:
            print("No hay suficientes existencias para realizar la venta.")
    else:
        print("El producto no está en el inventario.")

while True:
    print("\n1. Agregar producto\n2. Realizar compra\n3. Realizar venta\n4. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        realizar_compra()
    elif opcion == "3":
        realizar_venta()
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

