"""Práctica: Generación de la Serie de Fibonacci."""

# Posición máxima que acepta el programa de prueba (más arriba tarda demasiado)
LIMITE_N: int = 30


# ======== FUNCIÓN PRINCIPAL (reutilizable) ========
def fibonacci(n: int) -> int:
    """Retorna el número de Fibonacci en la posición n (fibonacci(6) -> 8)."""
    if not isinstance(n, int):
        raise TypeError("El parámetro 'n' debe ser de tipo int")
    if n < 0:
        raise ValueError("El parámetro 'n' debe ser mayor o igual a 0")

    # Casos base: son las hojas del árbol de llamadas y detienen la recursión
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Caso recursivo: cada llamada se divide en dos ramas, (n - 1) y (n - 2),
    # hasta llegar a los casos base. Las ramas repiten cálculos: fibonacci(n - 2)
    # también se calcula dentro de fibonacci(n - 1), por eso el árbol crece
    # de forma exponencial.
    return fibonacci(n - 1) + fibonacci(n - 2)


# ======== PROGRAMA DE PRUEBA ========
def main() -> None:
    print("=== Serie de Fibonacci ===")
    print("Calcula el número que ocupa la posición n en la serie.")
    print(f"Acepta posiciones de 0 a {LIMITE_N}.")
    while True:
        entrada = input("\nEscribe una posición n (o 'salir' para terminar): ").strip()
        if entrada.lower() == "salir":
            print("Programa terminado.")
            break

        try:
            n = int(entrada)
        except ValueError:
            print("  Escribe un número entero.")
            continue

        if n < 0:
            print("  La posición no puede ser negativa.")
            continue
        if n > LIMITE_N:
            print(f"  Escribe una posición de 0 a {LIMITE_N}.")
            continue

        print(f"  fibonacci({n}) = {fibonacci(n)}")


if __name__ == "__main__":
    main()
