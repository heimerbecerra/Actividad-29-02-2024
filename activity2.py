# hacer programa con productos,escogerlos y fracturarlos
cons_pcomputador = 15
cons_ptableta = 5
cons_pvideobeam = 10
cons_ptelevisor = 100

cantidad_computadores = 0
cantidad_tabletas = 0
cantidad_videobeam = 0
cantidad_televisiones = 0

while True:
    print("\nSeleccione una opción:")
    print("1. Computador de escritorio SAMSUNG")
    print("2. Tabletas SAMSUNG")
    print("3. Videobeam SONY")
    print("4. Televisores SAMSUNG")
    print("5. Facturar")

    opcion = input("Ingrese el número de opción o 'FACTURAR' para finalizar: ")

    if opcion == '1':
        cantidad_computadores += 1
    elif opcion == '2':
        cantidad_tabletas += 1
    elif opcion == '3':
        cantidad_videobeam += 1
    elif opcion == '4':
        cantidad_televisiones += 1
    elif opcion.upper() == 'FACTURAR':
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

total_pagar = (cantidad_computadores * cons_pcomputador) + \
              (cantidad_tabletas * cons_ptableta) + \
              (cantidad_videobeam * cons_pvideobeam) + \
              (cantidad_televisiones * cons_ptelevisor)

print("\nFACTURA")
print("--------")
print(f"Cantidad de Computadores: {cantidad_computadores}")
print(f"Cantidad de Tabletas: {cantidad_tabletas}")
print(f"Cantidad de Videobeam: {cantidad_videobeam}")
print(f"Cantidad de Televisores: {cantidad_televisiones}")
print(f"CORRELE A PAGARRRRRR SERIAN: ${total_pagar}")
