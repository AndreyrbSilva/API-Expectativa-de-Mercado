from app.models.expectativas_selic import ExpectativasSelic

class ExpectativasSelicProcessor:
    def preprocess(self, data):
        data_str = data.get("Data")
        Indicador = data.get("Indicador")
        Reuniao = data.get("Reuniao")
        Media = float(data.get("Media", 0))
        Mediana = float(data.get("Mediana", 0))
        DesvioPadrao = float(data.get("DesvioPadrao", 0))
        Minimo = float(data.get("Minimo", 0))
        Maximo = float(data.get("Maximo", 0))
        numeroRespondentes = int(data.get("numeroRespondentes", 0))
        baseCalculo = int(data.get("baseCalculo", 0))

        return ExpectativasSelic(data_str, Indicador, Reuniao, Media, Mediana, DesvioPadrao, Minimo, Maximo, numeroRespondentes, baseCalculo)
