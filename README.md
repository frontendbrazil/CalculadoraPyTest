# CalculadoraPyTest

Este projeto contém uma calculadora simples com operações matemáticas básicas e testes automatizados.

## Estrutura do projeto

- `calculadora/operacoes.py` - implementação original das operações
- `calculadora/operacoes_alternativa.py` - versão alternativa com nomes diferentes
- `calculadora/rotinas.py` - outra versão alternativa com estilo distinto
- `tests/test_operacoes.py` - testes para `operacoes.py`
- `tests/test_operacoes_alternativa.py` - testes para `operacoes_alternativa.py`
- `tests/test_rotinas.py` - testes para `rotinas.py`

## Como executar

No diretório do projeto, use:

```bash
python -m pytest -q
```

Isso executará todos os testes e confirmará que todas as variações da calculadora funcionam corretamente.
