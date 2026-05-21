from __future__ import annotations


def combinar(a: float, b: float) -> float:
    return a + b


def retirar(a: float, b: float) -> float:
    return a - b


def multiplicar_por(a: float, b: float) -> float:
    return a * b


def dividir_por(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Valor inválido: divisão por zero.")
    return a / b


def elevar(a: float, b: float) -> float:
    return a ** b


def extrair_raiz(valor: float) -> float:
    if valor < 0:
        raise ValueError("Não é possível extrair raiz quadrada de número negativo.")
    return valor ** 0.5
