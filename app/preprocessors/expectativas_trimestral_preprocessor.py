from app.models.expectativas_trimestral import ExpectativaTrimestral

class ExpectativasTrimestralProcessor:
    def preprocess(self, data):
        data_str = data.get("Data")
        Indicador = data.get("Indicador")
        DataReferencia = data.get("DataReferencia")
        Media = float(data.get("Media", 0))
        Mediana = float(data.get("Mediana", 0))
        DesvioPadrao = float(data.get("DesvioPadrao", 0))
        Minimo = float(data.get("Minimo", 0))
        Maximo = float(data.get("Maximo", 0))
        numeroRespondentes = int(data.get("numeroRespondentes", 0))
        baseCalculo = int(data.get("baseCalculo", 0))

        return ExpectativaTrimestral(Indicador, data_str, DataReferencia, Media, Mediana,
                                     DesvioPadrao, Minimo, Maximo, numeroRespondentes, baseCalculo)