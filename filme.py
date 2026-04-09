#import datetime

class Filme:
    contador = 1
    

    def __init__(self,nome,sinopse,elenco,dtlancamento):
        self.id = Filme.contador
        self.nome = nome
        self.sinopse = sinopse
        self.elenco = elenco
        self.dtlancamento = dtlancamento
        Filme.contador += 1

    
    def to_dict(self):
        return {
            "nome": self.nome,
            "sinopse": self.sinopse,
            "elenco": self.elenco,
            "dtlancamento": self.dtlancamento
        }