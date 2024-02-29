import os
os.system





def contar_numeros_en_rango(numeros):
    contador = 0
    for numero in numeros:
        if 10 <= numero <= 20:
            contador += 1
    return contador

def main():
    try:
        cantidad_numeros = int(input("¿Cuantos Numeros Quieres Ingresar? "))
        numeros = []
        for i in range(cantidad_numeros):
            numero = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)

        numeros_en_rango = contar_numeros_en_rango(numeros)
        print(f"La Cantidad De Numeros En El rango de 10 a 20 es: {numeros_en_rango}")
    
    except ValueError:
        print("Error: Por Favor ingrese Solo Números.")

if __name__ == "__main__":
    main()
