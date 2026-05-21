import pytest
from calculadora.operacoes import (somar, subtrair, multiplicar, dividir, potencia, raiz_quadrada)

def test_soma_positiva():
    assert somar(2, 3) == 5
    
def test_soma_negativa():
    assert somar(-2, -3) == -5
    
def test_subtracao_positiva():
    assert subtrair(10,4) == 6
    
def test_subtracao_negativa():
    assert subtrair(-5, -3) == -2
    
def test_potencia_expoente_zero():
    assert potencia(5, 0) == 1
    
def test_potencia_expoente_negativo():
    assert potencia(2, -3) == 0.125
    
def test_raiz_quadrada_valida():
    assert raiz_quadrada(16) == 4

def test_raiz_numero_negativo_levanta_excecao():
    with pytest.raises(ValueError) as e:
        raiz_quadrada(-9)
    assert str(e.value) == "Não é possível calcular a raiz quadrada de um número negativo."