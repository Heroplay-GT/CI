"""Calculadora simple para el parcial de Calidad de Software.

Contiene funciones pequeñas y un `main()` para demostración.
"""


def sumar(a, b):
    """Suma dos números"""
    return a + b


def restar(a, b):
    """Resta dos números"""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b


def dividir(a, b):
    """Divide dos números. Lanza ValueError si b == 0"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def potencia(base, exponente):
    """Calcula la potencia de un número"""
    return base ** exponente


def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0


def main():
    """Función principal"""
    print("Calculadora Simple")
    print(f"5 + 3 = {sumar(5, 3)}")
    print(f"5 - 3 = {restar(5, 3)}")
    print(f"5 * 3 = {multiplicar(5, 3)}")
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"2^3 = {potencia(2, 3)}")
    print(f"¿4 es par? {es_par(4)}")


if __name__ == "__main__":
    main()
