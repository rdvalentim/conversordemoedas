# Alunos Ederson Schulze e Ramon Valentim

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

# Função de validação de entrada para valores individuais
def validar_entrada(valor: str) -> float:
    try:
        valor_float = float(valor)
        if valor_float <= 0:
            raise ValueError("O valor deve ser positivo.")
        return valor_float
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return None

# Função de validação para uma lista de valores
def validar_lista_entradas(valores: list) -> list:
    valores_float = []
    for valor in valores:
        valor_validado = validar_entrada(valor)
        if valor_validado is not None:
            valores_float.append(valor_validado)
        else:
            print(f"Valor '{valor}' ignorado por ser inválido.")
    return valores_float

# Função para exibir opções e realizar a conversão
def conversor():
    moedas = ["USD", "BRL", "EUR", "JPY", "GBP"]  # lista das moedas
    print("Conversor de Moedas")
    
    # Inserir o valor ou lista de valores
    valores = input("Digite os valores para converter (separados por vírgula): ").split(',')
    valores = validar_lista_entradas(valores)
    if not valores:
        print("Nenhum valor válido inserido.")
        return
    
    print("Moedas disponíveis:", moedas)
    moeda_origem = input("Escolha a moeda de origem: ").upper()
    moeda_destino = input("Escolha a moeda de destino: ").upper()

    # Verifica se as moedas estão na lista
    if moeda_origem not in moedas or moeda_destino not in moedas:
        print("Moeda inválida. Escolha uma das opções disponíveis.")
        return

    # Obtem a taxa de câmbio
    taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)
    if taxa is None:
        print("Erro ao obter a taxa de câmbio.")
        return

    # Converter e exibir os valores
    valores_convertidos = converter_lista_valores(valores, taxa)
    for i, valor_convertido in enumerate(valores_convertidos):
        print(f"{valores[i]} {moeda_origem} é equivalente a {valor_convertido} {moeda_destino}")

# Função de ordem superior para converter uma lista de valores usando map
def converter_lista_valores(valores: list, taxa: float):
    return list(map(lambda valor: converter_valor(valor, taxa), valores))

# Execução principal
if __name__ == "__main__":
    conversor()
