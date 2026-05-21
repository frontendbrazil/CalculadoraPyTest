from __future__ import annotations


def adicao(x: float, y: float) -> float:
    return x + y


def subtracao(x: float, y: float) -> float:
    return x - y


def produto(x: float, y: float) -> float:
    return x * y


def divisao(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Não é permitido dividir por zero.")
    return x / y


def exponenciacao(base: float, expoente: float) -> float:
    return base ** expoente


def raiz_quadrada(valor: float) -> float:
    if valor < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de número negativo.")
    return valor ** 0.5
