# Busca de Voos usando a API Tequila e Twilio

Este script em Python, `flight_search.py`, foi criado para facilitar buscas de voos usando a API Tequila da Kiwi.com. Ele fornece funções para obter códigos IATA de aeroportos para uma determinada cidade e verificar detalhes de voos entre locais e datas especificados.

## Pré-requisitos

- Python 3.x instalado
- Pacotes Python necessários: `requests`

## Começando

1. Obtenha uma chave de API da Tequila se cadastrando no [Portal de Desenvolvedores da Kiwi.com](https://tequila.kiwi.com/portal/).

2. Substitua `"YOUR TEQUILA API KEY"` no script pela sua chave real da API Tequila.

```python
TEQUILA_API_KEY = "YOUR TEQUILA API KEY"
```

## Uso

### Obtendo o Código IATA para uma Cidade

```python
from flight_search import FlightSearch

# Inicialize a FlightSearch
flight_search = FlightSearch()

# Obtenha o código IATA para uma cidade
cidade = "Paris"
codigo_iata = flight_search.obter_iata(cidade)
print(f"Código IATA para {cidade}: {codigo_iata}")
```

### Verificando Detalhes do Voo

```python
from flight_search import FlightSearch

# Inicialize a FlightSearch
flight_search = FlightSearch()

# Especifique os detalhes do voo
cidade_origem = "Paris"
codigo_destino = "NYC"  # Código IATA para a cidade de destino
data_inicial = "2023-11-01"
retorno = "2023-11-10"

# Verifique os detalhes do voo
dados_voo = flight_search.checar_detalhes_viagem(cidade_origem, codigo_destino, data_inicial, retorno)

if dados_voo:
    print("Detalhes do voo:")
    print(f"Preço: R${dados_voo.preço}")
    print(f"De: {dados_voo.cidade_origem}, {dados_voo.aeroporto_origem}")
    print(f"Para: {dados_voo.cidade_destino}, {dados_voo.aeroporto_destino}")
    print(f"Data de Partida: {dados_voo.data_saida}")
    print(f"Data de Retorno: {dados_voo.data_retorno}")
```

Certifique-se de substituir `cidade_origem` e `codigo_destino` pelas cidades desejadas e seus códigos IATA correspondentes obtidos usando a função `obter_iata`.

---

Sinta-se à vontade para personalizar e aprimorar este README de acordo com os requisitos do seu projeto.
