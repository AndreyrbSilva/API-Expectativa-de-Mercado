import requests
from app.models.expectativas_anual import ExpectativaAnual

class ExpectativaAnualService:
    
    def __init__(self, url_api, pre_processor):
        self.url_api = url_api
        self.pre_processor = pre_processor
        
    def obtain_and_preprocessor(self):
        resposta = requests.get(self.url_api)
        resposta.raise_for_status()
        dados_brutos = resposta.json()
        dados = dados_brutos.get("value", [])
        
        processados = [self.pre_processor.preprocess(item) for item in dados]
        return processados