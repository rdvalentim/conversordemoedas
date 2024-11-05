# Conversor de Moedas
Trabalho - Programação Funcional
Este projeto é um conversor de moedas desenvolvido em Python, com o objetivo de aplicar conceitos de programação funcional. O programa permite ao usuário selecionar duas moedas e inserir um valor para conversão, aplicando uma taxa de câmbio obtida de uma API para realizar a conversão.

## Funcionalidades
- Entrada de um valor para conversão.
- Seleção de duas moedas para a conversão (por exemplo, USD para EUR).
- Aplicação de uma taxa de câmbio atualizada obtida de uma API.
- Validação das entradas do usuário, garantindo que o valor seja numérico e positivo.
- Exibição do valor convertido de forma precisa.

## Conceitos de Programação Funcional Aplicados
`Funções Puras:` Todas as funções no código são puras, ou seja, não dependem nem alteram o estado global. <br>
`Imutabilidade:` Os valores originais de entrada não são modificados; as funções retornam novos valores a cada cálculo. <br>
`Funções de Ordem Superior:` A função converter_lista_valores utiliza map para converter uma lista de valores, e filter é utilizado na validação de entradas, demonstrando o uso de funções de ordem superior. <br>
`Reutilização de Código:` As funções para validação, obtenção de taxa de câmbio e conversão são projetadas para serem reutilizáveis, promovendo modularidade e manutenibilidade. <br>

## Como rodar a aplicação
- Para rodar a aplicação você deve estar na pasta do repositório e digitar "python converson.py"
