import pytest
from conversordemoedas import conversor  # type: ignore # Ajuste para o nome real da função

def test_conversor_valida():
    assert conversor(10, 'USD', 'BRL') == 50  # Exemplo de teste, ajuste conforme necessário
