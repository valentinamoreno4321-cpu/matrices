import entrada
import operaciones_matrices
import menu

def main():
    while True:
        opcion = menu.mostrar_menu()

        if opcion == 5:
            print("\nSaliendo del programa.")
            break

        print("\nIngrese la primera matriz:")
        A = entrada.ingresar_matriz()

        print("\nIngrese la segunda matriz:")
        B = entrada.ingresar_matriz()

        resultado = None

        if opcion == 1:
            resultado = operaciones_matrices.sumar_matrices(A, B)
            titulo = "Resultado de la Suma:"
        elif opcion == 2:
            resultado = operaciones_matrices.multiplicar_matrices(A, B)
            titulo = "Resultado de la Multiplicación:"
        elif opcion == 3:
            resultado = operaciones_matrices.hadamard_matrices(A, B)
            titulo = "Resultado del Producto de Hadamard:"
        elif opcion == 4:
            resultado = operaciones_matrices.kronecker(A, B)
            titulo = "Resultado del Producto de Kronecker:"

        if resultado is not None:
            print(f"\n{titulo}")
            entrada.mostrar_matriz(resultado)
        else:
            print("No se pudo realizar la operación por dimensiones incompatibles.")

if __name__ == "__main__":
    main()