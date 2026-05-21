import pytest

from calculadora.rotinas import (
    combinar,
    retirar,
    multiplicar_por,
    dividir_por,
    elevar,
    extrair_raiz,
)


def test_combinacao_basica():
    assert combinar(2, 3) == 5


def test_combinacao_negativos():
    assert combinar(-2, -3) == -5


def test_retirada_basica():
    assert retirar(10, 4) == 6


def test_retirada_negativa():
    assert retirar(-5, -3) == -2


def test_elevar_por_zero():
    assert elevar(5, 0) == 1


def test_elevar_por_expoente_negativo():
    assert elevar(2, -3) == 0.125


def test_extrair_raiz_valida():
    assert extrair_raiz(16) == 4


def test_extrair_raiz_negativa_gera_erro():
    with pytest.raises(ValueError) as exc_info:
        extrair_raiz(-9)

    assert str(exc_info.value) == "Não é possível extrair raiz quadrada de número negativo."
