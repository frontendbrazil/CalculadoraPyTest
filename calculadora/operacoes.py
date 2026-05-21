def somar(a: float, b: float) -> float:
    return a + b

def subtrair(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(base: float, exp: float) -> float:
    return base ** exp

def raiz_quadrada(valor: float) -> float:
    if valor < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return valor ** 0.5