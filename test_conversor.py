import pytest
from conversordemoedas.conversor import conversor

def test_conversor_valida():
    assert conversor(10, 'USD', 'BRL') == 50  # Exemplo de teste, ajuste conforme necessário
