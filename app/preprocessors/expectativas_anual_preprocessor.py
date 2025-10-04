from app.models.expectativas_anual import ExpectativaAnual

class ExpectativaAnualProcessor:
    
    def preprocess(self, data):
        data_str = data.get("Data")
        Indicador = data.get("Indicador")
        IndicadorDetalhe = data.get("IndicadorDetalhe")
        DataReferencia = data.get("DataRefencia")
        Media = float(data.get("Media", 0))
        Mediana = float(data.get("Mediana", 0))
        DesvioPadrao = float(data.get("DesvioPadrao", 0))
        Minimo = float(data.get("Minimo", 0))
        Maximo = float(data.get("Maximo", 0))
        numeroRespondentes = data.get("numeroRespondentes")
        baseCalculo = int(data.get("baseCalculo", 0))
        
        return ExpectativaAnual(data_str, Indicador, IndicadorDetalhe, DataReferencia, Media, Mediana, 
                                DesvioPadrao, Minimo, Maximo, numeroRespondentes, baseCalculo)