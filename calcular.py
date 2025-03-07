def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print("Suma de 5 + 3 =", suma(5, 3))
    print("Resta de 5 - 3 =", resta(5, 3))
    print("División de 6 / 2 =", division(6, 2))
