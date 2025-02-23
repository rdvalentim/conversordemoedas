import pytest
from conversordemoedas.conversor import conversor

def test_conversao_valida(monkeypatch):
    # Simulando a entrada corretamente
    monkeypatch.setattr('builtins.input', lambda prompt: "10,USD,BRL")
    assert conversor(10, 'USD', 'BRL') == 50  # Ajuste conforme necessário
