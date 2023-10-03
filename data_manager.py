import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/8d6cf860306b62ae386695145accec52/flightDeals/prices'

class DataManager:
    
    def __init__(self):
        self.viagens = {}

    def obter_paises(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        dados = response.json()
        self.viagens = dados['prices']
        return self.viagens

    def atualizar_iataCode(self):
        for city in self.viagens:
            body = {'price':{'iataCode': city['iataCode']}}
            response = requests.put(
                url=f'{SHEETY_PRICES_ENDPOINT}/{city["id"]}', 
                json=body)
            
            print(response.text)
