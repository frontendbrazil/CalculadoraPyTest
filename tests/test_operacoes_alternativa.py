import pytest

from calculadora.operacoes_alternativa import (
    adicao,
    subtracao,
    produto,
    divisao,
    exponenciacao,
    raiz_quadrada,
)


def test_adicao_positiva():
    assert adicao(2, 3) == 5


def test_adicao_com_negativos():
    assert adicao(-2, -3) == -5


def test_subtracao_positiva():
    assert subtracao(10, 4) == 6


def test_subtracao_com_negativo():
    assert subtracao(-5, -3) == -2


def test_exponenciacao_com_expoente_zero():
    assert exponenciacao(5, 0) == 1


def test_exponenciacao_com_expoente_negativo():
    assert exponenciacao(2, -3) == 0.125


def test_raiz_quadrada_valida():
    assert raiz_quadrada(16) == 4


def test_raiz_quadrada_negativa_deve_lancar_erro():
    with pytest.raises(ValueError) as exc_info:
        raiz_quadrada(-9)

    assert str(exc_info.value) == "Não é possível calcular a raiz quadrada de número negativo."
