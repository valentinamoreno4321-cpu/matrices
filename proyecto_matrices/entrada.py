def ingresar_matriz():
    """Permite al usuario ingresar una matriz por teclado con validación de errores."""
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            if filas <= 0:
                print("Error: el número de filas debe ser mayor a 0.")
                continue
            columnas = int(input("Ingrese el número de columnas: "))
            if columnas <= 0:
                print("Error: el número de columnas debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero válido.")

    matriz = []
    for i in range(filas):
        while True:
            try:
                entrada = input(f"Ingrese la fila {i+1} separada por espacios: ")
                fila = [float(x) for x in entrada.split()]
                if len(fila) != columnas:
                    print(f"Error: debe ingresar exactamente {columnas} valores numéricos.")
                else:
                    matriz.append(fila)
                    break
            except ValueError:
                print("Error: debe ingresar solo números válidos.")
    return matriz

def mostrar_matriz(A):
    """Imprime una matriz de forma legible en consola."""
    if not A:
        print("[]")
        return
    for fila in A:
        print([round(x, 2) if isinstance(x, float) and x == int(x) else x for x in fila])