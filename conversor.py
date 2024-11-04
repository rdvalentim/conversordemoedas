#ALUNOS EDERSON SCHULZE E RAMON VALENTIM

import requests

def obter_taxa_de_cambio(moeda_origem: str, moeda_destino: str) -> float:
    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}")
        response.raise_for_status()
        taxa_cambio = response.json()["rates"][moeda_destino]
        return taxa_cambio
    except Exception as e:
        print("Erro ao obter taxa de câmbio:", e)
        return None

def converter_valor(valor: float, taxa: float) -> float:
    return round(valor * taxa, 2)

# Função de validação de entrada
def validar_entrada(valor: str) -> float:
    try:
        valor_float = float(valor)
        if valor_float <= 0:
            raise ValueError("O valor deve ser positivo.")
        return valor_float
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return None

# Função para exibir opções e realizar a conversão
def conversor():
    moedas = ["USD", "BRL", "EUR", "JPY", "GBP"]  # lista simplificada de moedas
    print("Conversor de Moedas")
    
    # Entrada do usuário
    valor = input("Digite o valor para converter: ")
    valor = validar_entrada(valor)
    if valor is None:
        return  # encerra se o valor não for válido
    
    print("Moedas disponíveis:", moedas)
    moeda_origem = input("Escolha a moeda de origem: ").upper()
    moeda_destino = input("Escolha a moeda de destino: ").upper()

    # Verifica se as moedas estão na lista
    if moeda_origem not in moedas or moeda_destino not in moedas:
        print("Moeda inválida. Escolha uma das opções disponíveis.")
        return

    # Obter a taxa de câmbio
    taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)
    if taxa is None:
        print("Erro ao obter a taxa de câmbio.")
        return

    # Converter e exibir o valor
    valor_convertido = converter_valor(valor, taxa)
    print(f"{valor} {moeda_origem} é equivalente a {valor_convertido} {moeda_destino}")

# Função de ordem superior para converter uma lista de valores usando map
def converter_lista_valores(valores: list, taxa: float):
    return list(map(lambda valor: converter_valor(valor, taxa), valores))

# Execução principal
if __name__ == "__main__":
    conversor()
