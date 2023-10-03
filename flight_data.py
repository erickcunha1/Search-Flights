
class FlightData:

    def __init__(self, 
                preço, 
                cidade_origem, 
                aeroporto_origem, 
                cidade_destino, 
                aeroporto_destino, 
                data_saida, 
                data_retorno
            ):
        
        self.preço = preço
        self.cidade_origem = cidade_origem
        self.aeroporto_origem = aeroporto_origem
        self.cidade_destino = cidade_destino
        self.aeroporto_destino = aeroporto_destino
        self.data_saida = data_saida
        self.data_retorno = data_retorno