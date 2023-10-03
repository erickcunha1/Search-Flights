from data_manager import DataManager
from flight_search import FlightSearch
import requests
from notification_manager import NotificationManager

dados = DataManager()
procurar_voos = FlightSearch()
notification_manager = NotificationManager()

viagens = dados.obter_paises()

for linha in viagens:
    if linha["iataCode"] == '':    
        codigo=procurar_voos.obter_iata(linha['city'])
        linha['iataCode'] = codigo


for destination in viagens:
    flight = procurar_voos.checar_detalhes_viagem(
        cidade_origem='BSB',
        code_destino=destination["iataCode"],
        data_inicial='27/03/2023',
        retorno='27/09/2023'
    )

    if flight.preço < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Alerta de preço baixo! Apenas R${flight.preço} ir de {flight.cidade_origem}-{flight.aeroporto_origem} \
            para {flight.cidade_destino}-{flight.aeroporto_destino}, de {flight.data_saida} até {flight.data_retorno}."
        )
