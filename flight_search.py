import requests
from flight_data import FlightData


ENDPOINT='https://api.tequila.kiwi.com'
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_API_KEY = "YOUR TEQUILA API KEY"


header = {'apikey': TEQUILA_API_KEY}

class FlightSearch:
    def obter_iata(self, city):
        
        params = {
            "term": city,
            "location_types": "city"
        }
        response=requests.get(url=TEQUILA_ENDPOINT, headers=header, params=params)
        data=response.json()['locations']
        code=data[0]['code']
        return code

    
    def checar_detalhes_viagem(self, cidade_origem, code_destino, data_inicial, retorno):
        params={
            'fly_from': cidade_origem,
            'fly_to': code_destino,
            'date_from': data_inicial,
            'date_to': retorno,
            'curr':'BRL'
        }
        
        response=requests.get(
            url=f'{ENDPOINT}/v2/search', 
            headers=header, 
            params=params
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {code_destino}.")
            return None
        
        flight_data=FlightData(
            preço=data["price"],
            cidade_origem=data["cityFrom"],
            aeroporto_origem=data["flyFrom"],
            cidade_destino=data["cityTo"],
            aeroporto_destino=data["flyTo"],
            data_saida=data["local_departure"].split("T")[0],
            data_retorno=data["route"][1]["local_departure"].split("T")[0]
        )
        
        print(f"{flight_data.cidade_destino}: R${flight_data.preço}")
        return flight_data
    

