def sumar_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: Las matrices deben tener las mismas dimensiones para sumarse.")
        return None
    filas, columnas = len(A), len(A[0])
    return [[A[i][j] + B[i][j] for j in range(columnas)] for i in range(filas)]

def multiplicar_matrices(A, B):
    if len(A[0]) != len(B):
        print("Error: El número de columnas de A debe coincidir con el número de filas de B.")
        return None
    filas_A, columnas_A = len(A), len(A[0])
    columnas_B = len(B[0])
    resultado = []
    for i in range(filas_A):
        fila_res = []
        for j in range(columnas_B):
            suma = sum(A[i][k] * B[k][j] for k in range(columnas_A))
            fila_res.append(suma)
        resultado.append(fila_res)
    return resultado

def hadamard_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: Las matrices deben tener las mismas dimensiones para el producto de Hadamard.")
        return None
    filas, columnas = len(A), len(A[0])
    return [[A[i][j] * B[i][j] for j in range(columnas)] for i in range(filas)]

def kronecker(A, B):
    """Calcula el producto de Kronecker (no requiere validación de dimensiones)."""
    resultado = []
    for fila_A in A:
        for fila_B in B:
            nueva_fila = []
            for elem_A in fila_A:
                for elem_B in fila_B:
                    nueva_fila.append(elem_A * elem_B)
            resultado.append(nueva_fila)
    return resultado