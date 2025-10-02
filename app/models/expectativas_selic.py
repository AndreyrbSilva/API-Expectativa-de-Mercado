class ExpectativasSelic:

    def __init__(self, Indicador, Data, Reuniao, Media, Mediana, DesvioPadrao, Minimo, Maximo, numeroRespondentes, baseCalculo):
        self.Indicador = Indicador
        self.Data = Data
        self.Reuniao = Reuniao
        self.Media = Media
        self.Mediana = Mediana
        self.DesvioPadrao = DesvioPadrao
        self.Minimo = Minimo 
        self.Maximo = Maximo 
        self.numeroRespondentes = numeroRespondentes
        self.baseCalculo = baseCalculo

    def to_dict(self):
        return{
            "Indicador": self.Indicador,
            "Data": self.Data,
            "Reuniao": self.Reuniao,
            "Media": self.Media,
            "Mediana": self.Mediana,
            "DesvioPadrao": self.DesvioPadrao,
            "Minimo": self.Minimo,
            "Maximo": self.Maximo,
            "numeroRespondentes": self.numeroRespondentes,
            "baseCalculo": self.baseCalculo
        }
